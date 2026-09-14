---
tags: [azent_notes]
type: guide
---

# Azent Notes via Telegram — How to Use

#azent_notes

## The mental model

- You talk on Telegram. Hermes files.
- `raw-transcripts/` = log, you never open it.
- `azent-refined-notes/` = what you read. Only 5 hub files + `books/` + `daily/`.

## How to send

1. Open your Hermes chat on Telegram.
2. Record a voice note.
3. Put the routing word as the caption or first sentence. If no caption, the agent auto-splits.
4. Send. No follow-up needed.

## Routing words

| Say / write | Goes to |
|---|---|
| `til: ...` | `01-TIL.md` |
| `thought: ...` | `02-Thoughts.md` |
| `q: ...` | `03-Questions.md` |
| `todo: ...` | `04-Todos.md` |
| `build: ...` | `05-Builds.md` |
| `book: <Title> ...` | `books/<Title>.md` |
| nothing | split across hubs + `daily/YYYY-MM-DD.md` |

Rule: explicit prefix always wins. No prefix = agent decides.

## Examples

- `til: TRAI QoS is measured per LSA` → TIL only.
- `thought: compliance is becoming the product in telecom` → Thoughts only.
- `q: why is QoS per LSA and not per cell?` → Questions only, as `- [ ] Q-YYYYMMDD-NN`.
- `todo: summarize stakeholder comments tomorrow` → Todos only.
- `build: offline mesh chat for hostel` → Builds only.
- `book: Atomic Habits — identity beats goals, page 34` → `books/Atomic-Habits.md` under today's date. First mention creates the file.
- No prefix, rambly 3-min note → agent splits learnings/thoughts/questions/todos + logs all in `daily/`.

## Book notes workflow

1. First note: `book: <Exact Title> — your thought`. File is created.
2. Daily 20-min notes: `book: <Same Title> — ...` or just "same book as yesterday". Appended under `### YYYY-MM-DD`.
3. Distilled ideas get promoted to `## Key ideas` with a date. Raw thoughts stay in `## Log`.
4. Never rename the book mid-way. Pick one title form and stick to it.

## What the agent does every time

1. Saves verbatim transcript to `raw-transcripts/YYYY-MM-DD-HHmm.md`.
2. Appends refined bullets to the right hub(s).
3. Appends to `daily/YYYY-MM-DD.md` with `## HH:MM` + links to raw and hubs.
4. Every refined bullet ends with `[[YYYY-MM-DD]]`.
5. Every file keeps `#azent_notes` + `tags: [azent_notes]`.
6. Questions deduped: repeat = `+1 on [[date]]`, not a new line.

## Where to look in Obsidian

- Search tag `#azent_notes` to see everything from this system.
- Daily review: open `daily/today`.
- Weekly review: open the 5 hubs, check `03-Questions.md` open items and `04-Todos.md` unchecked items.
- Book review: open `books/<Title>.md`.

## Fixing mistakes

- Wrong file: reply "move that last note from Builds to Todos".
- Wrong split: reply "that last voice note was only a thought, remove from TIL".
- Merge duplicates: reply "merge duplicate questions in 03-Questions.md".
- The agent never deletes raw transcripts, so nothing is lost.

## Tips for accuracy

- Say the routing word first, then pause, then talk.
- One idea per voice note when possible. Long mixed notes are fine but split less cleanly.
- Say book titles the same way every time.
- For questions, phrase the actual question in one sentence.
- Don't edit hub files by hand intraday — let the agent append, you curate weekly.

## Demo script

1. Send: `til: test note, QoS is per LSA` → check `01-TIL.md`.
2. Send: `q: test question, why per LSA?` → check `03-Questions.md`.
3. Send: `book: Test Book — first thought on page 1` → check `books/Test-Book.md`.
4. Send a ramble with no prefix → check `daily/YYYY-MM-DD.md` + hubs.
5. In Obsidian, search `#azent_notes` → all four should appear.

## Troubleshooting

- Note didn't appear: check `raw-transcripts/` for today's timestamp. If raw exists but refined doesn't, tell Hermes "file the pending raw note from HH:MM".
- Went to wrong hub: correct once with "move…", the routing file already teaches the pattern.
- Book created twice (e.g. `Atomic-Habits` vs `Atomic Habits`): tell Hermes "merge books/X into books/Y, keep one file".
- Tag missing: tell Hermes "add #azent_notes to …". All new files must carry it.
