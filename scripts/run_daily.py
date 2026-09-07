#!/usr/bin/env python3
"""
Daily orchestrator for Qwoted scraping.

Drives the Hermes browser session to fetch each keyword, runs the cards
through qwoted_scraper for parsing / filtering / dedup, and writes the day's
relevant listings to the Sept-2027 Google Sheet.

This script is INTENDED to be invoked by the Hermes cron scheduler (hermes
cronjob) at 7pm IST daily. It can also be run manually from inside a Hermes
browser session for ad-hoc testing.

Run:  python run_daily.py
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Add sibling dir to import path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from qwoted_scraper import (  # noqa: E402
    BASE_URL,
    CLIENTS,
    KEYWORDS,
    STATE_FILE,
    Listing,
    build_listing_from_card,
    client_for_listing,
    filter_and_dedupe,
    is_still_active,
    load_state,
    parse_posted_relative,
    parse_relative_to_date,
    report,
    save_state,
    write_to_sheet,
)

IST = timezone(timedelta(hours=5, minutes=30))


# ---------- Browser-side scraping ----------

# This function is meant to be executed inside a Hermes browser_exec context.
# It collects the listings visible on the current page and returns them as JSON.
# The orchestrator feeds each keyword's URL into the browser, then calls this
# function via JS evaluation.

JS_SCRAPE_CURRENT_PAGE = r"""
(function() {
    // Find every listing card. Each card has the structure we observed for
    // the medical query: a publication heading, a title link, a "Posted:" /
    // "Deadline:" inline label, and an anchor we can lift the URL from.
    //
    // We anchor on the "Posted:" StaticText node and walk DOM siblings to
    // recover the publication, title, and href for the card. This is more
    // robust than parsing the full innerText.

    const pubs = ['SWNS','Business Insider','Newsweek','Conde Nast Traveller India',
                  'Life Science Daily News',"Men's Health",'Travel + Leisure',
                  'RealClearPolitics','BDO Pro','DrBicuspid.com','Behavioral Health Business',
                  'Lose It!','Forbes','Better Report','Inc. Magazine','8 News NOW',
                  'Daily Mail US','Upcoming Book'];

    // Strategy: find every element whose innerText starts with "Posted:" and
    // walk up to its enclosing card container. Then look for the publication
    // header and the title link inside that card.

    const cards = [];
    const all = document.querySelectorAll('*');
    const seenCards = new Set();

    function findPostedNodes() {
        const results = [];
        for (const el of all) {
            const txt = (el.innerText || '').trim();
            // Match the "Posted: ..." label only — the literal first line
            if (txt.startsWith('Posted:') && txt.split('\n').length <= 5) {
                results.push(el);
            }
        }
        return results;
    }

    function nearestCard(node) {
        let cur = node;
        while (cur && cur !== document.body) {
            const cls = (cur.className || '').toString();
            // Heuristic: walk up until we find a container with multiple
            // anchor tags and a reasonable size.
            const anchors = cur.querySelectorAll('a[href]').length;
            if (anchors >= 1 && cur.offsetHeight > 80) {
                return cur;
            }
            cur = cur.parentElement;
        }
        return null;
    }

    const postedNodes = findPostedNodes();
    for (const pn of postedNodes) {
        const card = nearestCard(pn);
        if (!card || seenCards.has(card)) continue;
        seenCards.add(card);

        // Find publication heading
        let pub = '';
        for (const el of card.querySelectorAll('h1,h2,h3,h4,h5,h6,strong,b')) {
            const t = (el.innerText || '').trim();
            if (t && t.length < 80 && !pub) {
                pub = t;
                break;
            }
        }

        // Find title link — first <a> whose href contains /source_requests/
        // and is NOT the search page itself.
        let title = '';
        let url = '';
        const anchors = card.querySelectorAll('a[href]');
        for (const a of anchors) {
            const href = a.getAttribute('href') || '';
            if (!href.includes('/source_requests/')) continue;
            if (href.includes('/search')) continue;
            const t = (a.innerText || '').trim();
            if (t.length > 15) {
                title = t;
                url = href.startsWith('http') ? href : new URL(href, location.href).href;
                break;
            }
        }

        // Posted / Deadline labels
        const fullText = card.innerText || '';
        let posted = '', deadline = '';
        for (const line of fullText.split('\n')) {
            if (line.startsWith('Posted:') && !posted) posted = line.replace('Posted:','').trim();
            if (line.startsWith('Deadline:') && !deadline) deadline = line.replace('Deadline:','').trim();
        }

        // Description = first line ending with "..."
        let description = '';
        for (const line of fullText.split('\n')) {
            if (line.trim().endsWith('...')) { description = line.trim(); break; }
        }

        if (title && url) {
            cards.push({pub, title, description, posted, deadline, url});
        }
    }
    return JSON.stringify(cards);
})()
"""


def scrape_current_page_via_browser(browser_exec_fn) -> list[dict]:
    """Run the page-scraper JS in the browser and return raw card dicts."""
    raw = browser_exec_fn(JS_SCRAPE_CURRENT_PAGE)
    if not raw:
        return []
    # browser_exec returns a string like "...\n{\"success\": true, ...}"
    # Extract the JSON we returned
    import re
    m = re.search(r'"output":\s*"(.*?)"\s*,\s*"workspace"', raw, re.DOTALL)
    if m:
        json_str = m.group(1).encode().decode('unicode_escape')
    else:
        json_str = raw
    try:
        return json.loads(json_str)
    except Exception:
        return []


# ---------- Orchestration note ----------
#
# All scraping lives in the single JS helper above (JS_SCRAPE_CURRENT_PAGE).
# It captures title, publication, posted/deadline, description AND url in one
# pass, since the title anchor's href is the listing URL.
#
# Earlier versions paired two passes (cards + url anchors) which was brittle.


# ---------- Main orchestration ----------

def run_once(browser_exec_fn) -> dict:
    """
    Run one full pass: navigate to each keyword's search page, scrape cards,
    dedupe, write to sheet.

    `browser_exec_fn` is a callable that takes a JS string and returns the
    raw output from the Hermes browser_exec tool. In the Hermes session this
    is provided by the parent orchestrator; in a standalone test it can be a
    stub.
    """
    now = datetime.now(IST)
    fetch_iso = now.date().isoformat()
    print(f"[qwoted] {now.isoformat()} IST — starting daily run")

    state = load_state()
    all_new_listings: list[Listing] = []

    for keyword in KEYWORDS:
        url = BASE_URL + keyword.replace(' ', '+')
        print(f"\n[kw] {keyword!r} -> {url}")
        # 1. Navigate
        nav_result = browser_exec_fn(f'new_tab("{url}")\nwait_for_load()')
        if not nav_result:
            print(f"  ! navigation failed for keyword={keyword}")
            continue
        # 2. Wait briefly for SPA to render
        time.sleep(2)
        # 3. Scrape cards (one pass returns everything)
        cards = scrape_current_page_via_browser(browser_exec_fn)
        print(f"  cards={len(cards)}")
        for c in cards:
            listing = build_listing_from_card(
                publication=c.get("pub", ""),
                title=c.get("title", ""),
                description=c.get("description", ""),
                url=c.get("url", ""),
                posted_text=c.get("posted", ""),
                deadline_text=c.get("deadline", ""),
                keyword=keyword,
                now=now,
            )
            if listing is None:
                continue  # expired
            if not listing.clients:
                continue  # no client match
            all_new_listings.append(listing)
        # throttle to be polite
        time.sleep(1)

    # Dedupe against state
    new_only = filter_and_dedupe(all_new_listings, state)
    print(f"\n[summary] candidates after client filter: {len(all_new_listings)}; new (not seen): {len(new_only)}")

    # Write to sheet
    if new_only:
        result = write_to_sheet(new_only, fetch_date_iso=fetch_iso)
        print(f"[sheet] wrote {result['appended_rows']} rows at {result['range']}")

    # Update state
    for n in new_only:
        if n.url:
            state["seen_urls"].append(n.url)
    state["last_run"] = now.isoformat()
    save_state(state)

    report(new_only, state)
    return {
        "candidates": len(all_new_listings),
        "new": len(new_only),
        "written": len(new_only),
    }


def main(argv: list[str]) -> int:
    # When run inside the Hermes session, the orchestrator passes a callable.
    # In a standalone test, we exit early with a helpful message.
    print("run_daily.py is intended to be invoked by the Hermes cron scheduler.")
    print("To run it manually: launch a Hermes browser session and call run_once(browser_exec_fn).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))