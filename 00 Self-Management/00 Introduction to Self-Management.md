---
date created: 2026-04-29
date updated: 2026-09-27 — Added Week 40 fortnight plan for September 28–October 11; continues the two-week reflection cadence.
---

# Self-Management

**Purpose:** Find the patterns. Build a personality profile Ash can decide from — energy, regulation, how he works, where he drifts. Reflection is the input; `Patterns.md` is the output.

**Why it changed.** The old system wrote the same handful of insights 4–6 times each, across days, weeks, and files. It was so heavy the habit collapsed. The new loop captures cheap, distils once a fortnight, and keeps only what recurs.

---

## The three layers

1. **`Patterns.md`** — the durable profile. Hard-capped, self-condensing, decaying. The *only* self-file read day to day, and only when relevant (Charlotte greps it like `Recall.md`; Ash is never asked). Recurrence is the test: repeats → pattern; once → `## Watching` → dropped if it doesn't return. Stale patterns move to `Archive/`.
2. **`Weeks/Week [ISO].md`** — raw data points for the current fortnight, extracted from Ash's dumps. One file per two-week cycle, named after the starting ISO week (e.g. `Week 38.md` covers Weeks 38–39, Monday of the first week through Sunday of the second). Retained on disk, **not** auto-read. Pulled only for playback or a deliberate lookback.
3. **`Goals/` + `[C] RGS.md`** — the strategy layer. Yearly anchor + monthly priorities. Untouched by the reflection loop.

---

## The loop

**1. Dump (low overhead).** Ash talks: what he's doing, what's happening, what he's focused on, patterns he notices. No template, no schedule. Trigger: a dump, or "clear up the dispatch."

**2. Extract.** Charlotte pulls the real data points into `Weeks/Week [ISO].md` under the day — loose bullets, faithful to his words, ruthlessly de-duplicated. No Morning/Afternoon/Evening + worked/didn't + two-mechanisms scaffold. If the fortnight file doesn't exist yet, create it from the shape below.

**3. Playback.** Ash asks *"how's my week been?"* → Charlotte reads that one fortnight file and plays it back coherently: what he did + his reflections, readable even if the input was messy. This is the only time week files load.

**4. Manual reflection.** Ash reflects deeply on the fortnight himself. Charlotte appends it under `## Week reflection` in the file. She does not invent it.

**5. Update Patterns.** After his reflection, Charlotte updates `Patterns.md`: recurring things graduate/strengthen, one-offs land in `## Watching`, patterns that are no longer true decay to `Archive/`, the per-section cap forces condensing. Then she refreshes the 3–4 strongest lines into `MEMORY.md ## Profile` (always-on headline), honouring its char cap.

---

## Week file shape

Soft-coded. One file per two-week cycle (Monday of week one – Sunday of week two), named after the starting ISO week. Evergreen — describe, don't hard-name projects.

```markdown
---
week: [N]
dates: [Mon–Sun, Mon–Sun]
---

# Week [N]

## [Weekday, Date]
- [raw data point]
- [raw data point]

## Week reflection
[Ash's deep reflection, added on the fortnightly pass]
```

---

## Triggers (see root CLAUDE.md)

- **Dump / "clear up the dispatch"** → extract to the current fortnight file (`/Workflows/Process Idea Batches.md`).
- **"how's my week been"** → playback the current fortnight file.
- **"weekly reflection"** → playback → Ash reflects → Charlotte updates `Patterns.md` + the `## Profile` headline.

Charlotte is the thinking partner. `Patterns.md` is the memory. The week files are the raw tape.
