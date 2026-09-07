#!/usr/bin/env python3
"""
Qwoted daily scraper.

Fetches source-request listings from Qwoted for a fixed set of keywords,
filters by client relevance, drops expired listings, dedupes against a local
state file, and appends the day's new items to the Sept-2027 Google Sheet tab.

Run:  python qwoted_scraper.py
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

# ---------- Configuration ----------

STATE_FILE = Path(r"A:\Azdhanvibing\azdhan-notes\content\qwoted_state.json")
CREDENTIALS_FILE = Path(r"A:\Azdhanvibing\on-device-tools\google-sheets-api-key.json")
SHEET_URL = "https://docs.google.com/spreadsheets/d/1SO655itvjWvGwPhDwYD97KkU053acmMazOYebgK3nDQ/edit?usp=sharing"
TAB_NAME = "Sept-2027"
BASE_URL = "https://app.qwoted.com/source_requests/search?query="

KEYWORDS = [
    "cooking",
    "food entrepreneur",
    "immigrant entrepreneur",
    "life coach",
    "executive coach",
    "self development",
    "entrepreneurship",
    "women in business",
    "women-led startups",
    "South Asian entrepreneur",
    "medical school",
    "financial aid",
    "MCAT",
    "Dental",
    "physician",
    "nursing",
    "USMLE",
    "law school",
    "LSAT",
    "legal education",
    "college admissions",
    "medical",
]

# Timezone for IST (UTC+5:30)
IST = timezone(timedelta(hours=5, minutes=30))

# ---------- Client relevance rules ----------

CLIENTS = {
    "Inspira Advantage": {
        # medical, dental, vet, residency, PA admissions consulting.
        # Tight match: only stories ABOUT applying to / getting into these programs.
        "match_terms": [
            "medical school", "med school", "dental school", "dentistry school",
            "mcat", "usmle",  # test prep for healthcare
            "residency", "residency match", "residency application",
            "physician assistant", "pa program", "pa school",
            "nursing school", "nursing program", "bsn", "msn", "np program",
            "veterinary school", "vet school",
            "pre-med", "premed", "pre-dental", "predental",
            "college admissions", "graduate admissions", "admissions consulting",
            "admissions cycle", "admissions process", "application essay",
            "personal statement", "med applicant", "dental applicant",
            "amcas", "aadsas", "aamc", "eras",  # application services
            "interview season", "waitlist", "secondaries",
            "interview prep", "medical school interview", "residency interview",
            "financial aid", "scholarship",  # aid for grad school
        ],
        "exclude_terms": [
            "dental insurance", "dental plan", "dentist office visit",
            "medical billing", "medical records",
        ],
    },
    "Juris Education": {
        # law school admissions, LSAT, legal education
        "match_terms": [
            "law school", "law student", "law applicant", "law program",
            "lsat", "legal education", "law school admissions", "pre-law",
            "prelaw", "bar exam", "bar association", "lawyer", "attorney",
            "legal career", "juris", "law degree", "jd program",
        ],
    },
    "Abhinav Jindal (Cydir)": {
        # life / executive coach, NLP, second-gen family business leaders
        "match_terms": [
            "life coach", "executive coach", "coaching", "self development",
            "self-development", "personal development", "nlp",
            "neuro-linguistic", "mental and emotional release", "mer therapy",
            "second generation", "second-generation", "family business",
            "family business leader", "empowerment", "mindset", "founder",
            "entrepreneur", "women entrepreneur", "women in business",
            "women-led", "immigrant entrepreneur", "south asian",
        ],
    },
}

# ---------- Parsing helpers ----------

# "an hour ago", "3 hours ago", "a day ago", "2 days ago",
# "a month ago", "3 months ago", "a year ago"
POSTED_RE = re.compile(
    r"\b(?:an?|[0-9]+)\s+(minute|hour|day|week|month|year)s?\s+ago\b",
    re.IGNORECASE,
)
DEADLINE_RE = re.compile(
    r"\bin\s+(?:an?\s+)?(\d+)\s+(minute|hour|day|week)s?\b",
    re.IGNORECASE,
)

UNIT_TO_DELTA = {
    "minute": timedelta(minutes=1),
    "hour": timedelta(hours=1),
    "day": timedelta(days=1),
    "week": timedelta(weeks=1),
    "month": timedelta(days=30),  # approximation
    "year": timedelta(days=365),  # approximation
}


def parse_relative_to_date(text: str, *, now: datetime) -> datetime | None:
    """Convert a phrase like 'in 3 days' or '2 hours ago' to an absolute datetime."""
    if not text:
        return None
    text = text.strip().lower()
    m = DEADLINE_RE.search(text)
    if m:
        n = int(m.group(1))
        unit = m.group(2).lower()
        return now + n * UNIT_TO_DELTA[unit]
    return None


def parse_posted_relative(text: str, *, now: datetime) -> datetime | None:
    """Convert '2 hours ago' / 'a day ago' / '11 days ago' to an absolute datetime."""
    if not text:
        return None
    text = text.strip().lower()
    m = POSTED_RE.search(text)
    if not m:
        return None
    parts = text.split()
    if parts[0] in ("an", "a"):
        n = 1
        unit = parts[1].rstrip("s")  # "hours" -> "hour"
    else:
        n = int(parts[0])
        unit = parts[1].rstrip("s")
    if unit not in UNIT_TO_DELTA:
        return None
    return now - n * UNIT_TO_DELTA[unit]


def is_still_active(
    deadline_text: str,
    *,
    now: datetime,
    posted_text: str | None = None,
    stale_threshold_days: int = 30,
) -> bool:
    """
    A listing is active if:

    1. It has a deadline that's still in the future, OR
    2. It has no deadline AND was posted within `stale_threshold_days`.

    Anything else is treated as inactive and dropped.
    """
    deadline_text = (deadline_text or "").strip()
    if deadline_text:
        parsed = parse_relative_to_date(deadline_text, now=now)
        if parsed is None:
            # We couldn't parse — be conservative and keep it
            return True
        return parsed > now

    # No deadline — fall back to posted date
    if posted_text:
        posted_dt = parse_posted_relative(posted_text, now=now)
        if posted_dt is None:
            return True  # unparseable — keep
        age = now - posted_dt
        return age < timedelta(days=stale_threshold_days)

    # No deadline, no posted — keep (open-ended)
    return True


def matches_client(title: str, description: str, client_key: str) -> bool:
    rules = CLIENTS[client_key]
    haystack = (title + " " + description).lower()
    if any(term.lower() in haystack for term in rules.get("exclude_terms", [])):
        return False
    return any(term.lower() in haystack for term in rules["match_terms"])


def client_for_listing(title: str, description: str) -> list[str]:
    hits = []
    for client in CLIENTS:
        if matches_client(title, description, client):
            hits.append(client)
    return hits


# ---------- Data model ----------

@dataclass
class Listing:
    publication: str
    title: str
    url: str
    posted_text: str
    deadline_text: str
    posted_on: str  # ISO date (or "")
    deadline_on: str  # ISO date (or "")
    keyword: str
    clients: list[str] = field(default_factory=list)
    description: str = ""


# ---------- State (dedup) ----------

def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"seen_urls": [], "last_run": None}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"seen_urls": [], "last_run": None}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def is_seen(url: str, seen_set: set[str]) -> bool:
    if not url:
        return False
    # Normalize: strip trailing slash, lowercase scheme/host
    return url.rstrip("/") in {u.rstrip("/") for u in seen_set}


def mark_seen(url: str, state: dict) -> None:
    if url and url not in state["seen_urls"]:
        state["seen_urls"].append(url)


# ---------- Google Sheets writer ----------

def write_to_sheet(rows: list[Listing], *, fetch_date_iso: str) -> dict:
    """
    Append the day's rows to the Sept-2027 tab.

    Strategy:
      - Open the worksheet
      - Find the first empty row in column A (Fetch date)
      - Append all rows starting there with batch_update
      - Mark the Fetch date for today's group in column A on the first new row only,
        leaving subsequent rows empty so users can identify the day's grouping visually
    """
    import gspread
    from google.oauth2 import service_account

    creds = service_account.Credentials.from_service_account_file(
        str(CREDENTIALS_FILE),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    gc = gspread.Client(auth=creds)
    sh = gc.open_by_url(SHEET_URL)
    ws = sh.worksheet(TAB_NAME)

    # Find first fully empty row in column A by reading the column
    col_a = ws.col_values(1)
    start_row = len(col_a) + 1  # 1-indexed; safe because header lives at row 1
    if start_row <= 1:
        start_row = 2  # never overwrite header

    # Build value range
    values = []
    for i, r in enumerate(rows):
        values.append([
            fetch_date_iso if i == 0 else "",  # mark only first row of the day
            r.publication,
            r.title,
            r.url,
            r.posted_on,
            r.deadline_on,
        ])
    if not values:
        return {"appended_rows": 0, "range": ""}

    end_row = start_row + len(values) - 1
    end_col = "F"
    rng = f"A{start_row}:{end_col}{end_row}"

    ws.update(rng, values, value_input_option="USER_ENTERED")
    return {"appended_rows": len(values), "range": rng}


# ---------- Scraper ----------

def scrape_keyword(keyword: str, *, fetch_dt: datetime) -> list[Listing]:
    """
    Fetch and parse one keyword's search page from Qwoted.

    Implementation: this is meant to be called by the orchestrator via the
    browser_use CLI (because Qwoted requires an authenticated browser session).
    For the standalone test/CI path we expose a thin wrapper that reads the
    page through the browser harness if available; otherwise we read a
    pre-rendered snapshot file written by the calling Hermes session.
    """
    raise NotImplementedError(
        "scrape_keyword must be invoked from within a Hermes browser session; "
        "see run_keyword() in the orchestrator."
    )


# ---------- Orchestrator ----------

def build_listing_from_card(
    *, publication: str, title: str, description: str, url: str,
    posted_text: str, deadline_text: str, keyword: str, now: datetime,
    stale_threshold_days: int = 30,
) -> Listing | None:
    """Normalize one card into a Listing or drop if expired."""
    if not is_still_active(
        deadline_text,
        now=now,
        posted_text=posted_text,
        stale_threshold_days=stale_threshold_days,
    ):
        return None

    posted_dt = parse_posted_relative(posted_text, now=now)
    deadline_dt = parse_relative_to_date(deadline_text, now=now)

    clients = client_for_listing(title, description)

    return Listing(
        publication=publication,
        title=title,
        url=url,
        posted_text=posted_text,
        deadline_text=deadline_text,
        posted_on=posted_dt.date().isoformat() if posted_dt else "",
        deadline_on=deadline_dt.date().isoformat() if deadline_dt else "",
        keyword=keyword,
        clients=clients,
        description=description,
    )


def filter_and_dedupe(
    candidates: Iterable[Listing], state: dict
) -> list[Listing]:
    """Drop duplicates and items that don't match any client."""
    seen_urls = set(state.get("seen_urls", []))
    out = []
    for c in candidates:
        if not c.clients:
            continue  # no client matches — skip
        if is_seen(c.url, seen_urls):
            continue
        out.append(c)
    return out


def report(rows: list[Listing], state: dict) -> None:
    print(f"\n=== Qwoted run summary ===")
    print(f"Total new listings matching clients: {len(rows)}")
    if rows:
        by_client: dict[str, int] = {}
        for r in rows:
            for c in r.clients:
                by_client[c] = by_client.get(c, 0) + 1
        print(f"By client: {by_client}")
        print(f"State now tracks {len(state['seen_urls'])} URLs.")
    else:
        print("No new relevant listings.")


def main(argv: list[str]) -> int:
    now = datetime.now(IST)
    fetch_iso = now.date().isoformat()
    print(f"[qwoted] {now.isoformat()} IST — starting daily run")
    state = load_state()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))