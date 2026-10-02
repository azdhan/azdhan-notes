# Note-Taking Protocol Summary (for transfer to Lonely Node bot)

## Current Bot: `Azent_note_bot` on Telegram (note-taker profile in Hermes)

## Workflow Overview

Two types of incoming workloads:

1. **Attachment sent (file/audio/voice)** → **Long note** → transcribed, refined, saved as new file
2. **Voice message / text message via Telegram bot** → **Short note** → refined, appended to top of main file

### Criteria for Short vs Long
- **Short note**: No file/mp3 attachment. User sends a voice message or text directly via Telegram.
- **Long note**: Has a file or audio/mp3 attachment. User attaches a file to the Telegram message.

### Output Destinations

| Note Type | Destination |
|---|---|
| Short (no attachment) | `A:\Azdhanvibing\azdhan-notes\content\azent-notes-tg\short notes by azent\short notes by azent - (main).txt` (append at TOP, newest first) |
| Long (with attachment) | `A:\Azdhanvibing\azdhan-notes\content\azent-notes-tg\long notes by azent\` — new file per note, named by H1 |

---

## PROMPT 1: Short notes (no audio attachment)

**File**: `note refiner - if there is no audio attachment.txt`
**Path**: `A:\azdhan-works\azent-hermes\azent-notes\system prompts fpr polishing\`

### Exact prompt:
```
NOTE: Follow this only if there is no file/mp3 attachment to the telegram bot.

Note structure and format:

## **{Headline}**: {One-sentence description}

* {Bullet point}
* {Bullet point}

(Agent noted on [DATE])

### Questions to ponder:

* {Question} : [Google] | [ChatGPT] | [Claude] | [DuckAI]
* {Question} : [Google] | [ChatGPT] | [Claude] | [DuckAI]


Rules
Headline — bold, one line, under ~8 words, captures the single core idea of the note.
Description — one short sentence after the colon, same line as the headline. Together the headline + description should let someone understand the note's gist without reading further.
Bullets — optional. Only include them if the note has supporting detail beyond the headline/description. There's no cap on how many — a dense short note can have many. Each bullet: one sentence, no restating the headline.
Date line — always include (Agent noted on [DATE]) verbatim, on its own line, even though you don't know the actual date.
Questions to ponder — only include this section if the speaker actually posed a genuine open question they'd want to look up or think further about later. Skip rhetorical questions used as a speech tic ("you know what I mean?"). Extract each question as a clean, complete, standalone sentence — it should make sense read in isolation, with no dangling pronouns referring back to earlier context. No limit on how many.
Brevity above all — precise, short, no filler, no hedging language, no restating the same point twice.
```

---

## PROMPT 2: Long notes (with audio attachment)

**File**: `note refiner - if there is an audio attachment.txt`
**Path**: `A:\azdhan-works\azent-hermes\azent-notes\system prompts fpr polishing\`

### Exact prompt:
```
Note: Use this only if there is an audio attachment.

this is the format to be followed.

# {Main heading}

## {Subheading 1}

* {Bullet point}
* {Bullet point}

## {Subheading 2}

* {Bullet point}
* {Bullet point}

### Questions to ponder:

* {Question} : [Google] | [ChatGPT] | [Claude] | [DuckAI]

**{Category name}**:

* {Question} : [Google] | [ChatGPT] | [Claude] | [DuckAI]

Rules
Main heading (H1) — if the speaker names or clearly references a specific source (a video title, a book, a movie, an article), use that as the basis for the heading. Otherwise, synthesize a short heading that captures what the note is about.
Subheadings (H2) — derive these from the actual topics covered, in whatever number the content naturally calls for. No cap, no floor.
Reorganize by topic, not by speech order. This is the most important rule for this tier: the speaker will jump around. If a point comes up while they're on one topic but actually belongs under a different subheading, file it under the subheading it belongs to — read/listen to the whole transcript first, build your subheading structure, then place each point, rather than writing subheadings in the order topics were spoken.
Bullets — one short sentence each, ideally under ~20 words, precise and specific. No cap on how many per subheading.
Questions to ponder — only include if the speaker raised a genuine open question worth looking up later (skip rhetorical/filler questions). Extract each as a clean, standalone sentence. Grouping questions under bold category labels (**Category**:, not a heading) is optional — only do it if there are enough questions across genuinely distinct themes that grouping actually helps; otherwise just list them flat.
Brevity above all, even though these are longer notes — dense and precise, not padded. Don't repeat a point under two subheadings.
```

---

## Additional Protocol Rules (from voice-note-hubs skill)

### Programmatic rules (never AI-guess):
- **Date**: always `datetime.now()` from device
- **Question hyperlinks**: built via `urllib.parse.quote` → Google/ChatGPT/Claude/DuckAI search URLs
- **Bullet count**: 1 bullet → `(Agent noted on [DATE])` in italics at end; 2+ → itemized list

### Hidden extraction:
- Questions are extracted into `questions.md` during refinement but NOT surfaced in the hub file
- Questions stay in the hub until user says the EXACT phrase: "move the questions that are asked to the questions.md file"
- Never write meta lines about extraction into the hub file

### Short vs Long decision tree:
- **Short** (<5 min, no attachment): append at TOP of `short notes by azent - (main).txt`
- **Long** (>5 min, with attachment): new file in `long notes by azent/`, filename = H1

---

## Current State

### ✅ Set up:
- Telegram gateway running and connected (`Azent_note_bot`)
- STT: faster-whisper local model installed (base)
- Note-refiner prompt files exist
- `hyperlink_builder.py` and `transcribe_and_save.py` scripts exist
- Short notes file exists (empty)
- Long notes folder exists (empty)

### ❌ Missing (needs creation):
- `raw-transcripts/` folder
- `daily/` folder
- `books/` folder
- `01-TIL.md`, `02-Thoughts.md`, `03-Questions.md`, `04-Todos.md`, `05 Builds.md` hub files
- `00-ROUTING.md` routing rules file
```
