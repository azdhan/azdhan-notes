STANDING INSTRUCTIONS (Sheets API work)

Access:
- Service account key: [path to .json]
- Sheet: [URL]
- Tabs: MAIN = my curated master list; workspace = your scratch area
- Never modify existing columns/data unless I explicitly ask

API discipline:
- Batch everything: one read, process locally, one write
- Use batchUpdate/batchGet, never per-cell calls in loops
- On HTTP 429: exponential backoff and retry automatically,
  don't crash mid-job or leave half-written data
- If a job might exceed limits anyway, chunk it and report progress

When something fails:
- Don't stop and ask me immediately — try reasonable fallbacks first
  (e.g., alternate endpoints, matching by name if URL match fails)
- Report what you tried and what still failed

When done, report:
- Counts: processed / succeeded / failed / skipped
- Anything unmatched or ambiguous, listed by row
- What you wrote and where, so I can verify