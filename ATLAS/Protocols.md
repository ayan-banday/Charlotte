---
date created: 2026-06-09
date updated: 2026-06-09
loaded: on demand (when a trigger fires)
purpose: The operating procedures, in one file. Replaces the old Context/ folder.
---

# Protocols

The few procedures Charlotte runs. Triggers are listed in `MI.md`'s vocabulary; the steps are here.

---

## 0. The Curator (self-recursion — the primary mechanism)

`System/The Curator.md` is the one automatic mechanism: it processes a session/transcript with parallel subagents and **suggests** what to save — it does not save new content on its own. Triggers: **"curate" / "consolidate" / session end** (full pass) · **"save this verbatim" / a transcript lands** (Chronicler + DIGEST). Proposals land in `System/Curator Inbox.md`; Ash applies what he wants. The Curator subsumes the consolidation + sync work; the reflection loop below is the human-driven path it proposes into.

---

## 1. Reflection loop (capture → distil → patterns)

**Purpose:** find the patterns. Build a durable profile Ash decides from — energy, regulation, how he works, where he drifts. Reflection is the input; `System/Patterns.md` is the output. Capture cheap daily, distil once a week, promote only what recurs.

**Capture** — trigger: Ash dumps the day ("reflect" / "daily reflect" / just talks), or "clear up the dispatch".
1. **Listen, don't interrogate.** Take the dump as raw material — what he did, his state, what he focused on, patterns he noticed. No template, no Morning/Afternoon/Evening scaffold.
2. **Extract to the week file** `CALENDAR/Weeks/Week [ISO].md`, under today's weekday — loose bullets, his words tightened, duplicates dropped. Create the file from the shape below if absent.
3. **Idea detection.** If the dump carries an initiative (not just reflection), route it (existing project → its Brain Dump; new → scaffold with `project-creator`). Ask only if the home is ambiguous.
4. **No promotion yet.** Daily capture does **not** touch `Patterns.md` or `MEMORY.md`. That's what keeps it cheap.

**Playback** — trigger: "how's my week been".
1. Read **only** the current week file. Play it back coherently — what he did + his reflections — readable even if the dumps were messy.
2. Optionally cross-check `CALENDAR/Goals/`. Don't load `Patterns.md` or other weeks unless he asks to look further back.

**Weekly distil** — trigger: "weekly reflection".
1. Playback (above).
2. **Ash reflects deeply himself.** Append it under `## Week reflection` in the week file. Do not invent it.
3. **Update `System/Patterns.md`:** recurring → graduate/strengthen a line; one-off → `## Watching` (one week grace); no-longer-true → decay to `CALENDAR/Archive/`; section at cap (~900 chars) → condense + drop the weakest first.
4. **Refresh the headline:** mirror the 3–4 strongest patterns into `MEMORY.md ## Profile`, within its cap.

Recurrence decides; judgment prunes. Ash graduates patterns, not surveillance.

**Week file shape** (one file per ISO week, Mon–Sun; describe, don't hard-name projects):
```markdown
---
week: [N]
dates: [Mon–Sun]
---
# Week [N]
## [Weekday, Date]
- [raw data point]
## Week reflection
[Ash's deep reflection, added on the weekly pass]
```

---

## 2. Route Capture

Sorting captured input (Notion "The Que" or the Dispatch inbox) to its home. Full steps + safety rules in `ATLAS/Workflows/Route Capture.md`. Triggers: "process the que" (Notion; also the scheduled run) · "clear up the dispatch" (Dispatch inbox).

---

## 3. Recording a rule or a prompt

**Record a rule** — trigger: "record this rule". Append it, stated precisely, to this file under a clear heading. No padding. Confirm.

**Store a prompt / skill** — trigger: "store this prompt". Author it into `ATLAS/Skills/[Domain]/` (use `skill-creator`; ask the domain if unclear), store the prompt in full, then add one line to `AIOS/Skill Map.md`. Confirm. (That one Skill Map line is the whole registration — no separate index, no domain intro.)

---

## 4. Maintenance

Added/renamed/deleted a file → update the one relevant line in `AIOS/Vault Map.md` or `AIOS/Skill Map.md`. No counts, no per-folder intros, no separate index. (When the Curator is running, its TIDY pass does this automatically.)

---

## 5. Inline notes convention

Ash can leave notes to Charlotte inside any document: text in `{curly brackets}`, or an indented bullet under a section, is a direct message/question to act on, not part of the document body.
