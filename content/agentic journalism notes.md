module link: [web](https://cashlessconsumer.zo.space/agentic-journalism/course) \ [YT](https://www.youtube.com/watch?v=HShHdrZEecE&list=PLLAhCw1oiarY&index=2) (videos are embedded, not needed to watch videos saperately)
# intro
this course can be replicated with any capable ai agent. 
Intro prompt that was given to the  ai agent: 
```
You are my newsroom agent. I am the editor of record. From now on: you draft, I decide. Summarise what you are good at, what you refuse to do without my approval, and what you will always escalate to me.
```

TO ORGANISE THE FOLDERS: 
```
Create the folder Documents/research/<my-first-case>/ with the report, press, legal, data and evidence subfolders. Add an AGENTS.md charter at the root that says: evidence ledger is mandatory, no personal data on published pages, every external publish needs my approval.
```

TO GENERATE THE SKILLS ON THE REUSED TASKS: 
```
Pick one workflow I have done twice this month on my beat. Package it as a skill: Skills/<name>/SKILL.md with frontmatter (name; a description of when to use it) and numbered steps. Bake in the local specifics no generic pack would have — portal names, URL patterns, file formats, my readers' language. Mark anything private (source identities, credentials) as never-included. Show me the file before you save it.
```

TO BUILD A DAILY MONITOR: 
```
Build me a monitor for this public page: <URL of a page on your beat>. Every day at 9 AM: fetch it, store the sha256 and a timestamped snapshot in my workspace, compare with the previous run, and alert me ONLY if the hash changed — with the diff summarised in two lines. On Zo, post it to my channel; on Hermes, schedule it as a job and let it deliver the diff to your messaging app.
```

BUILDING CORPUS: 
```
Pick 25 public documents from <a notifications/orders page on your beat — court orders, board circulars, department orders, audit reports>. Download them politely, extract text with pdftotext, OCR the scanned ones, and save each as markdown named <date>_<title>.md. Keep a JSONL state file so re-runs skip completed files. When done, give me an index table: title, date, extraction method, one-line summary.
```




# some projects srikanth created
- [hyd mananagaram](https://cashlessconsumer.zo.space/mananagaram) \  