---
date created: 2026-06-08
date updated: 2026-06-08
notion_db: "https://www.notion.so/62d6ff4f6a37454380db0e5feab30e48"
sibling_of: "[[Process Idea Batches]]"
---

# Process The Que

**Problem:** Ash wants frictionless capture. He opens Notion, types the thought as the title, and walks away. Once a day this routine reads every New item in The Que, routes it, and marks it done. He never manually moves anything.

**Outcome:** New items routed or flagged. Self-management data in the week file. Log entry written. No item processed twice.

**Runs:** Automatically at 21:00 daily via scheduled task. Also: manually on "process the que."

**Sibling of:** `[[Process Idea Batches]]` (Dispatch version — still active for direct-session dumps).

---

## Prerequisites

- Notion database "The Que" exists (URL in this file's frontmatter)
- File Structure Registry is current with active projects and newsletters

---

## Workflow Steps

### Step 1: Query for New items

Query The Que database for all rows where **Status = New**. If none: write a one-line log entry ("No new items") and stop. The routine is idempotent by design — only New rows are ever touched.

Determine today's **ISO week number** and **weekday** before processing any items.

---

### Step 2: Route each item (one at a time)

**Mark each item the instant it is handled** — set Status before moving to the next. A crash mid-run must not be able to double-route.

Classify the thought into exactly one category:

---

#### AUTO-ROUTE → Self-management

**Signs:** what he did, his state, energy, timing, obstacles, physical (sleep, meds, walks), patterns he noticed. This is the first-priority category — when in doubt between self-management and something else, route here.

1. Open `/00 Self-Management/Weeks/Week [ISO].md`. If the file doesn't exist yet, create it from the shape in `/00 Self-Management/00 Introduction to Self-Management.md`.
2. Append the thought as a loose bullet under today's weekday heading. Tighten and de-duplicate the words. Faithful, concise. Never invent.
3. **Immediately** set: Status = Processed, Type = Self-management, Routed To = "Week [ISO] / [Weekday]", Processed = today's date.

**Do NOT touch `Patterns.md` or `MEMORY.md`.** Daily extraction is capture only. Patterns graduate on the weekly pass via `/Context/Reflection Protocol.md`.

---

#### AUTO-ROUTE → Newsletter

**Signs:** he names a specific newsletter that matches a project in the registry.

1. Locate `/02 Projects/Newsletter [Name]/01 Brain Dump for Newsletter [Name].md` via the File Structure Registry. If the path can't be resolved, treat as Flag (below).
2. Append the thought as a bullet.
3. **Immediately** set: Status = Processed, Type = Newsletter, Routed To = the resolved path, Processed = today's date.

---

#### FLAG → Needs Ash

All other cases:

- Project-specific idea (could go to a project brain dump — needs his call)
- Skill or workflow candidate (always his call)
- Anything ambiguous, multi-home, or where the path can't be resolved

**Set: Status = Needs Ash, Type = best-guess or Ambiguous, leave Routed To blank.**

Never guess on judgment calls that belong to Ash. This is the equivalent of "suggest and wait" in the Dispatch workflow. Ash reviews Needs Ash rows whenever he likes. To re-process, he flips Status back to New.

---

### Step 3: Write the run log

Append to `/01 Daily Logs/Que Routing Log.md` (create the file if it doesn't exist):

```
## [YYYY-MM-DD HH:MM]
- New items found: [N]
- Routed → Week file: [N]
- Routed → Newsletter: [N]
- Flagged → Needs Ash: [N]
- Errors: [N]
  [Describe each error: which item, what path failed, what was done]
```

If a destination path couldn't be resolved, that item counts as an error AND gets flagged to Needs Ash with Type = Ambiguous.

---

## Safety rules

1. **Only ever query Status = New.** Ignore everything else. This is what makes daily runs idempotent.
2. **Mark immediately.** Set Status before moving to the next item. Never batch-update at the end.
3. **Path can't be resolved → Needs Ash + Ambiguous.** Never create a wrong file.
4. **Faithful + concise.** Tighten his words, never invent content.
5. **Self-management is priority one.** Route it first within each batch.

---

## Decision boundary

| Category | Confidence needed | Action |
|---|---|---|
| Self-management | Obvious language (state, energy, timing, what he did) | Auto-route → week file |
| Named newsletter (matches registry) | Named explicitly | Auto-route → brain dump |
| Project brain dump | Plausible but needs judgment | Flag → Needs Ash |
| Skill / workflow candidate | Always a judgment call | Flag → Needs Ash |
| Anything unclear | — | Flag → Needs Ash |

---

## When to use

**Manual trigger:** "process the que" → Charlotte reads this file and executes it against The Que.
**Automated:** runs daily at 21:00 via Windows Task Scheduler.

This is the Notion-sourced sibling of `[[Process Idea Batches]]`. Both coexist. The Que is the primary capture surface going forward. Dispatch remains for direct-session dumps.

