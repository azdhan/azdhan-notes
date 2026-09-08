![image-1](images/image-1.png)

## A Guide to Acquire Video from Streaming Sources

*Full session script — instructor notes, timing, and commands*

Audience: beginners with no prior command-line experience. Format: four sessions, one hour each. Scope: openly accessible content, one's own uploads, and content the learner already holds legitimate, authenticated access to.

### Session 1 — FetchV, Straight Into Practice

*Materials needed: laptop with Chrome installed, stable internet connection, 2–3 open-access sample links prepared in* *advance (e.g. a public lecture on YouTube, an institutional video page using HLS/m3u8)*

#### Installing FetchV (10 min)

- Open the Chrome Web Store and search for "FetchV."

- Click Add to Chrome and walk through the permissions dialog line by line before accepting — this is a good moment to explain, in plain language, what "read and change data on the sites you visit" actually allows an extension to do.

- Pin the extension icon to the toolbar so it stays visible.

*Instructor note: keep this brief and concrete — the goal is a habit (always check permissions), not a lecture on browser* *security.*

#### Guided Practice (30 min)

Work through three short, contrasting examples so learners see the range of what FetchV can detect:

- Example A — direct MP4: open a prepared open-access video page, click the FetchV icon, and download at a chosen resolution.

- Example B — HLS/m3u8 stream: open an institutional or public streaming page and show how FetchV lists the .m3u8 manifest as a downloadable option.

- Example C — learner's own pick: have each participant try one open-access link of their own choice and download it. After each download, open the resulting file to confirm it plays correctly, and briefly compare file size across the resolution options offered.

#### Troubleshooting Common Issues (15 min)

- Video not detected: reload the page, let the video start playing fully before opening the extension, or try in a fresh tab.

- Format not compatible with the default player: open the file in VLC instead.

- Extension icon greyed out: confirm the page hasn't blocked extensions (some browser-internal pages do).

#### Assignment (5 min)

Before the next session, try FetchV on two videos of your own choosing and note any issue you ran into — we will use these as troubleshooting examples.

### Session 2 — Terminal + yt-dlp Basics

*Materials needed: macOS and/or Windows laptop, admin rights to install software*

#### What a Terminal Is (10 min)

Frame it simply: a terminal is another way to tell the computer what to do, by typing instead of clicking. Show where to find it on each system:

- macOS: Spotlight (Cmd+Space) → type "Terminal" → Enter.

- Windows: Start Menu → type "PowerShell" → Enter.

#### Installing yt-dlp (15 min)

**macOS (via Homebrew):** if Homebrew is not yet installed, run:

brew install yt-dlp brew install ffmpeg

**Windows (via winget):**

winget install yt-dlp winget install ffmpeg

Alternative for Windows without winget: download the standalone yt-dlp.exe from the official GitHub releases page, place it in a folder, and add that folder to the system PATH. Verify the install on either system with:

yt-dlp --version *ffmpeg is required on both systems to merge separate video/audio streams and to convert containers — without it, some* *downloads will fail or stay split into two files.*

#### First Commands (20 min)

Same syntax on macOS and Windows — only the way the terminal opens and file paths are written differs.

yt-dlp

List available formats before choosing one:

yt-dlp -F

Download a specific format or quality:

yt-dlp -f "bestvideo+bestaudio" yt-dlp -f 22

Control where the file is saved and how it is named:

```
yt-dlp -o "%(title)s.%(ext)s"
```

*Path note: macOS uses forward slashes (/Users/name/Downloads); Windows uses backslashes (C:\Users\name\Downloads).* *The -o template itself is identical.*

#### Comparing With FetchV (15 min)

Re-download one of the Session 1 examples with yt-dlp and compare: available quality options, resulting file size, and speed. Use this to build intuition for when the terminal route is worth the extra setup (more control, batch downloads, scripting) versus when the extension is simpler (one-off, casual downloads).

### Session 3 — Cookies and Authenticated Content

*Materials needed: yt-dlp already installed (Session 2), an account with content the learner is personally authorized to* *access (own channel, or an active legitimate subscription)*

#### Why Some Videos Require a Login (10 min)

Explain the distinction plainly: some content sits behind a login not because it is protected by DRM, but because it is private, age-restricted, or limited to members/subscribers. A browser session already has the credentials to view it; yt-dlp needs those same credentials, passed as a cookies file, to download it.

#### Installing "Get cookies.txt LOCALLY" (15 min)

- Install the extension from the Chrome Web Store, reviewing permissions as in Session 1.

- While logged into the relevant site, click the extension icon and export cookies.txt.

- Save the file somewhere easy to reference from the terminal, e.g. the Desktop.

*Alternative worth mentioning: yt-dlp can also read cookies directly from an already-open browser session, without a separate* *export step — see the closing note below.*

#### Case A — Own Private or Unlisted Content (15 min)

Practice with a video the learner uploaded themselves and set to private or unlisted (their own channel):

yt-dlp --cookies cookies.txt

#### Case B — Legitimate Subscription Content (15 min)

Same command, different context: content from a paid or member subscription the learner currently and legitimately holds (e.g. their own Patreon membership, a private Vimeo account they are a member of).

yt-dlp --cookies cookies.txt

*Emphasize explicitly: this only applies to a learner's own active, paid access — not to sharing or reusing someone else's login,* *and not to DRM-protected commercial streaming platforms, which are out of scope for this course.*

#### Cookie File Security (5 min)

- A cookies.txt file is equivalent to a saved login — treat it like a password.

- Never share it or upload it anywhere.

- Delete it once the session's downloads are done.

*Optional mention for more comfortable learners:* --cookies-from-browser chrome *lets yt-dlp read cookies directly* *from the browser, skipping the export file entirely.*

### Session 4 — Organization and Wrap-Up

*Materials needed: downloads accumulated from Sessions 1–3, optional external drive or cloud storage account for the* *backup discussion*

#### File Naming, Subtitles, and Metadata (15 min)

Build a consistent output template so files are easy to find later:

```
yt-dlp -o "%(uploader)s/%(title)s.%(ext)s"
```

Add subtitles and embed metadata directly into the file:

yt-dlp --write-sub --embed-metadata

#### Basic Backup Principles (15 min)

Keep this conceptual and beginner-level: a local disk is not a backup by itself. Introduce the idea of a second copy

in a different location (external drive or a cloud sync folder) without requiring any specific tool.

*For a technically comfortable audience this is where a tool like rclone could be introduced later — out of scope for this* *beginner run.*

#### Open Workshop (20 min)

Each participant picks their own use case from what was covered (FetchV, yt-dlp, or cookies-based download) and downloads and organizes at least one file end to end, with the instructor circulating to help.

#### Closing (10 min)

- Recap the three tools covered and when to reach for each.

- Share the yt-dlp GitHub repository and its options reference for continued self-study.

- Open floor for final questions.

*Note: this course covers tools for saving video that is openly accessible or that the learner is already authorized to access (own* *uploads, permitted streams, active subscriptions). It does not cover circumventing DRM-protected commercial streaming* *services.*