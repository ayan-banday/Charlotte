---
name: voice-correct
description: Log voice corrections and feed style updates back into active writing rules.
---

# Voice Correct

Use this skill when generated copy is flagged as off-voice and needs correction capture.

## What It Does

1. Compares corrected text vs generated text.
2. Logs correction evidence in `jani-voice` correction notes.
3. Extracts rule updates from the correction.
4. Applies those rules in the next draft.

## Trigger Conditions

- "this doesn't sound like me"
- "correct this"
- user replaces generated text with their own version
- explicit request to log a voice correction

## Output Standard

- Keep correction entries short and specific.
- Store exact before/after snippets.
- Convert repeated correction patterns into reusable writing rules.
