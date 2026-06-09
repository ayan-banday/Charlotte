---
date created: 2026-06-09
date updated: 2026-06-09
notion_db: "https://www.notion.so/62d6ff4f6a37454380db0e5feab30e48"
purpose: Sort captured input to its home. One workflow, two sources (Notion Que / Dispatch).
---

# Route Capture

**Problem:** Ash captures thoughts frictionlessly — typed into Notion "The Que" (walk-away) or dumped into the Dispatch inbox (in-session). This routine reads new items, routes each to its home, and marks it done. He never manually moves anything.

**Outcome:** new items routed or flagged; self-management data in the week file; nothing processed twice.

## Source (pick one per run)
- **Notion Que** — trigger: "process the que", and the daily scheduled run. Items are rows with `Status`. Query **only `Status = New`** (this makes runs idempotent). Mark each row the instant it's handled — set `Status` before the next item; never batch at the end.
- **Dispatch** — trigger: "clear up the dispatch". Items are bullets in `EFFORTS/Inbox/00 Dispatch.md`. Remove each routed item immediately; Dispatch holds only items awaiting a decision.

Determine today's **ISO week** and **weekday** before processing.

## Route each item (one at a time)

**AUTO → Self-management** *(priority one — when in doubt, route here)*
Signs: what he did, state, energy, timing, obstacles, physical (sleep, meds, walks), patterns he noticed.
→ Append as a loose bullet under today's weekday in `CALENDAR/Weeks/Week [ISO].md` (create from the shape in `ATLAS/Protocols.md` if absent). Tighten and de-duplicate; never invent.
→ **Do NOT touch `Patterns.md` or `MEMORY.md`** — patterns graduate on the weekly distil only.
→ Notion: set `Status = Processed, Type = Self-management, Routed To = "Week [ISO] / [Weekday]", Processed = today`.

**AUTO → Newsletter**
Signs: he names a specific newsletter matching a project.
→ Append to `EFFORTS/Active/Newsletter [Name]/01 Brain Dump for Newsletter [Name].md` (resolve via the Vault Map; if the path can't resolve, Flag instead).
→ Notion: set `Status = Processed, Type = Newsletter, Routed To = the path, Processed = today`.

**FLAG → Needs Ash** *(all other cases — his judgment)*
Project-specific idea, skill/workflow candidate, anything ambiguous/multi-home/unresolved path.
→ Notion: set `Status = Needs Ash, Type = best-guess or Ambiguous, Routed To = blank`. Dispatch: leave it in place, flagged.
Never guess on judgment calls that belong to Ash.

## Log (Notion runs)
Append to `CALENDAR/Daily/Que Routing Log.md` (create if absent):
```
## [YYYY-MM-DD HH:MM]
- New items found: [N]
- Routed → Week file: [N]   - Routed → Newsletter: [N]   - Flagged → Needs Ash: [N]
- Errors: [N]  [which item, what path failed, what was done]
```
A path that can't resolve counts as an error AND gets flagged Needs Ash with `Type = Ambiguous`.

## Safety rules
1. Notion: only ever query `Status = New`. 2. Mark immediately, never batch. 3. Path can't resolve → Needs Ash + Ambiguous; never create a wrong file. 4. Faithful + concise; never invent. 5. Self-management is priority one.
