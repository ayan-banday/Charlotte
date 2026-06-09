---
date created: 2026-06-09
date updated: 2026-06-09
loaded: on demand (when a trigger fires) — never in the hot tier
purpose: The one self-recursion mechanism. Charlotte processes, then SUGGESTS. Ash decides what's saved.
---

# The Curator

One mechanism, not a pile of protocols. It runs automatically, fans out parallel subagents, and **proposes** — it does not save new content on its own. It replaces the old reflection/consolidation/sync protocols.

## The save rule (above everything)
**Nothing new is saved unless Ash says to, or the Curator suggests it and he approves.** Big raw files (transcripts, long pastes) are **never** auto-saved. The recursion — the thinking, the extracting, the proposing — is automatic. The saving is always his.

## Triggers
- **Big paste / "save this verbatim" / a transcript lands** → DIGEST (mid-session). The Chronicler saves the raw file *only on command*; otherwise the Curator just works through it and proposes.
- **"curate" / "consolidate" / session end** → full pass (DIGEST + DRIFT + TIDY).
- **Nightly headless** (`run-curator.cmd`, OFF by default — manual first) → full pass, lookback = since last run; writes proposals to the Inbox only, saves nothing on its own.

## The three jobs (run as parallel Task subagents)
Each subagent gets a tight brief and read-mostly tools (Read/Grep/Glob/git). They return a short structured proposal. The main thread applies only the AUTO set and writes the rest to `System/Curator Inbox.md`.

### DIGEST — deepen the model of Ash
Inputs: the session transcript, any new `CALENDAR/History/` files, the current `CALENDAR/Weeks/Week [ISO].md`.
Hunt (Hermes' lens): has he revealed persona, desires, preferences, personal details, work style, or how he wants Charlotte to behave? What's the *real data* under a meeting/call transcript he was thinking through?
Output: **suggest** durable personal signal for `MEMORY.md ## Profile` / `System/Patterns.md` / `Recall.md`, and where session work should be saved. Measure caps; consolidate at 80% before proposing. **Never auto-write the person.**

### DRIFT — refine skills and voice from how he actually worked
Inputs: the session transcript **+ `git diff`** over `ATLAS/Skills/**`, `ATLAS/Workflows/**`, `System/SOUL.md`, `System/VOICES.md`, drafts.
Detect: where Ash overrode a loaded skill, rewrote a Charlotte draft, corrected the voice, or said "stop doing X" / "do it this way." 
Output: **propose** a refinement ("you keep doing it this way — lock it in?") in Hermes' preference order — update the loaded skill → an umbrella → a support file → a new skill only if nothing fits. Skill refinement = a "Refinements" note + `version` bump. Voice changes → propose into the Inbox; never auto-touch SOUL/VOICES or `ash-*-voice`.

### TIDY — keep the system clean (the only AUTO job)
Operates only on **already-saved** content. Self-compact `Recall.md`, condense capped sections, keep `AIOS/Vault Map.md` + `AIOS/Skill Map.md` honest after file changes, flag (don't move) stale `Patterns.md` lines. Absorbs the old "keep-in-sync" meta-protocols.

## The gate
- **AUTO (committed, git-revertible):** TIDY's housekeeping only — map sync, compacting/condensing existing notes, cap enforcement on already-saved content. Never creates new knowledge, never saves a raw file.
- **SUGGEST → `System/Curator Inbox.md` (Ash applies what he wants):** every new fact / Profile line / Pattern, every skill refinement, every voice change, every transcript save. This is the default for anything that introduces new content.

Everything is git-tracked, so even an applied change is one `git revert` away. Run manually as "curate" until the proposals are trustworthy; only then consider the nightly.

## Chronicler (the save-on-command half)
On "save this verbatim": write the raw conversation/transcript **untouched** to `CALENDAR/History/YYYY-MM-DD-<slug>.md`, summary block on top, raw below (see the `chronicler` skill). The big file leaves the working context immediately — grep it later, don't hold it. This is Charlotte's answer to context bloat: work through it, save on command, recall by search.
