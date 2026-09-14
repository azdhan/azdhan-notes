---
tags: [azent_notes]
type: routing
---

# Routing Rules (agent instructions)

#azent_notes

1. Raw transcript (verbatim) -> `../raw-transcripts/YYYY-MM-DD-HHmm.md` with `tags: [azent_notes]` + `#azent_notes`. Logs only, user does not read these.
2. Refined notes -> this folder (`azent-refined-notes/`). This is what the user sees.
3. Explicit prefix wins: `til:` -> `01-TIL.md`, `thought:` -> `02-Thoughts.md`, `q:` -> `03-Questions.md`, `todo:` -> `04-Todos.md`, `build:` -> `05-Builds.md`, `book: <Title>` -> `books/<Title>.md` (create if missing, with `#azent_notes` + date log sections).
4. No prefix -> split across hubs as appropriate + append to `daily/YYYY-MM-DD.md`.
5. Append-only. Never rewrite history. Every hub bullet ends with a `[[YYYY-MM-DD]]` backlink.
6. Every file created by this process must contain `#azent_notes` (body) and `tags: [azent_notes]` (frontmatter).
7. Questions: `- [ ] Q-YYYYMMDD-NN: ... #open` with context + source + status. Dedupe repeats with `+1 on [[date]]`.
8. Book files: `# Title`, `## Key ideas`, then `## Log` with `### YYYY-MM-DD` sections.
9. Daily files live in `daily/YYYY-MM-DD.md`, with `## HH:MM` entries linking to raw + hubs.
