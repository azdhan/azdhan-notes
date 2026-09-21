# Note automation — code + prompts

Project folder for azent voice-note automation.

## Prompts (load before AI call)
- `A:\azdhan-works\azent-hermes\azent-notes\system prompts fpr polishing\note refiner - if there is no audio attachment.txt` (short <5 min, no attachment)
- `...\note refiner - if there is an audio attachment.txt` (long >5 min, with attachment)

- Only two cases: no attachment = short (<5 min); attachment = long (>5 min). No routing words (til:, q:, build:, book:), no prefixes — decided by attachment presence only.

## Save targets
- Short (no attachment): append at top of `A:\Azdhanvibing\azdhan-notes\content\azent-notes-tg\short notes by azent\short notes by azent - (main).txt`
- Long (attachment): new file in `A:\Azdhanvibing\azdhan-notes\content\azent-notes-tg\long notes by azent\` named by H1.

## Programmatic (code, not AI)
- Date: `date` from device (programmatic).
- Question hyperlinks: build URLs from question text:
  - Google: `https://www.google.com/search?q=` + urllib.parse.quote(question)
  - ChatGPT: `https://chat.openai.com/?q=` + quote (or search endpoint)
  - Claude / DeepSeek: equivalent search slugs.
- Format: single bullet → `(Agent noted on [DATE])` at end in italics; multi-bullet → itemized list.
