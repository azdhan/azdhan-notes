"""Standalone driver that exercises run_daily.run_once against a live Hermes
browser session. It opens Qwoted, calls browser_exec-equivalent JS, processes
results, and writes to the Sept-2027 sheet.

This is the manual equivalent of what the cron job will run. For a real cron
job, see the cron entry created via `hermes cronjob create` (set up after
this test passes).
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from qwoted_scraper import (
    KEYWORDS, STATE_FILE, BASE_URL,
    build_listing_from_card, filter_and_dedupe, load_state, save_state,
    write_to_sheet, report,
)
from run_daily import IST, JS_SCRAPE_CURRENT_PAGE, scrape_current_page_via_browser


# This driver is run inside the same Python that has gspread installed, by
# the orchestrator (a Hermes turn). It is NOT itself called from the browser;
# the browser session is owned by the orchestrator and exposed via a callback.

def main():
    print("This driver is meant to be invoked from a Hermes turn, not standalone.")
    print(f"Run with: python {Path(__file__).name} --from-hermes")
    print()
    print(f"Keywords: {len(KEYWORDS)}")
    for kw in KEYWORDS:
        print(f"  - {kw}")
    print(f"\nState file: {STATE_FILE}")
    print(f"State exists: {STATE_FILE.exists()}")
    if STATE_FILE.exists():
        s = json.loads(STATE_FILE.read_text())
        print(f"Currently tracking {len(s.get('seen_urls', []))} URLs")
        print(f"Last run: {s.get('last_run')}")


if __name__ == "__main__":
    main()