---
name: chronicler
description: Save a conversation or transcript verbatim, on command, with a summary on top. Trigger on "save this verbatim", "save this", "chronicle this", or after Ash drops a meeting/call transcript and says to keep it. Never auto-save — only on command.
version: 1.0.0
---

# Chronicler

Save ideas, conversations, and transcripts before they're lost — **only when Ash says to.** This is the save-on-command half of the Curator. Big raw files are never saved automatically.

## When triggered
1. **Write the raw content untouched** to `CALENDAR/History/YYYY-MM-DD-<slug>.md`. Do not edit, summarize, or trim the body. `<slug>` = a few words naming the source (e.g. `jani-discovery-call`).
2. **Layer a summary on top** of the same file (summary above the divider, raw below). Use this fixed shape:

```markdown
---
date: YYYY-MM-DD
kind: transcript | conversation | reflection
source: <who / what>
---
# <slug> — YYYY-MM-DD

## Summary
<2–4 line overview>

## Takeaways
- <durable point>

## Topics
- <topic>

## Next steps
- <action, if any>

---

## Raw (verbatim — do not edit)
<the content, exactly as given>
```

3. **Drop it from working context.** Once saved, the raw text lives on disk — don't keep holding it in the session. Recall it later by grepping `CALENDAR/History/`.

## Rules
- Save only on command. Never auto-save a transcript or large paste.
- The raw block is never edited. A wrong summary is harmless — recall greps the raw.
- AI-derived content (the summary) stays clearly separated from Ash's raw words by the divider.
- If Ash didn't ask to save — don't. Work through it with him and let the Curator *suggest* what's worth keeping.
