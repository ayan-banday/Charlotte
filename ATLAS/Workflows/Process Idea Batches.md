---
date created: 2026-05-11
date updated: 2026-06-07 — Repointed self-management routing to Weeks/Week [ISO].md. Dropped the
  rigid daily-reflection template — extraction is now loose data points. Dispatch routing/clearing
  unchanged.
---

# Process Idea Batches

**Problem:** Ideas accumulate in Dispatch faster than they're routed. Need a system to continuously sort captured input to its right home (week file, projects, domains) without manual searching.

**Outcome:** Cleared Dispatch. Self-data extracted to the current week file. Other ideas routed or flagged. Ash keeps control over ambiguous routing.

**Time investment:** 5–15 minutes per batch.

---

## Prerequisites

- Input is captured in `/00 Inbox/00 Dispatch.md`
- File Structure Registry is current with active projects and domains

---

## Workflow Steps

### Step 1: Read the batch & fix today's date

Open `/00 Inbox/00 Dispatch.md`. Determine the current weekday and ISO week number.

**Sort what you see:**
- Self-management (what he did, state, energy, obstacles, patterns he noticed) → extract to the week file
- Newsletter mentions (he names the newsletter) → auto-route
- Project-specific ideas → suggest, wait
- Domain ideas (skills, workflows) → suggest, wait
- Ambiguous → leave in Dispatch

**Priority:** self-management first.

---

### Step 2: Extract self-management → the current week file

**Path:** `/00 Self-Management/Weeks/Week [ISO].md`, under today's weekday heading.

Pull the real **data points** — what he did, timing, state, patterns noticed — as loose bullets in his words, tightened and de-duplicated. Faithful, concise. **No** Morning/Afternoon/Evening + worked/didn't + two-mechanisms scaffold. If the week file doesn't exist, create it from the shape in `/00 Self-Management/00 Introduction to Self-Management.md`.

**Do NOT** touch `Patterns.md` or `MEMORY.md` here. Patterns graduate only on the weekly pass, on recurrence (see `/Context/Reflection Protocol.md`). Daily extraction is capture only — that's what keeps it cheap.

Example: a dump on Wednesday of Week 23 →

```markdown
## Wednesday, June 3
- Woke ~6:30, meditated, read in the sun (went great)
- Walk → breakfast → time slipped, no clear work block
- Published a Substack piece; not marketing it; no focus project pulling the work
```

---

### Step 3: Route the rest

**Newsletter ideas** (he names the newsletter) → auto-route to `/02 Projects/Newsletter [Name]/01 Brain Dump for Newsletter [Name].md`. Check the registry for the path. Auto-confirm.

**Everything else** → suggest and wait:
- Skills candidate: "Belongs in [Domain] as a skill?"
- Project idea: "Add to [Project]'s brain dump?"
- Workflow idea: "Record as a workflow?"
- Ambiguous: "Could go a few places — where?"

If Ash is uncertain, it stays in Dispatch until clarity emerges.

---

### Step 4: Clear & confirm (mandatory)

**Remove every routed item from `/00 Inbox/00 Dispatch.md` immediately.** Dispatch holds only items awaiting a decision.

- Remove: self-management extracted to the week file, auto-routed newsletter/project items.
- Keep: suggestions pending approval, ambiguous items flagged for context.

**Update the Dispatch header:** today's date, what was routed and where, what's pending.

**Confirmation report:**
- Self-management extracted to: Week [ISO], [weekday] (REMOVED)
- Auto-routed to newsletters: [count] (REMOVED)
- Auto-routed to projects: [count] (REMOVED)
- Suggested, pending: [count] (REMAINS)
- Remaining in Dispatch: [count]

---

## Decision points

- **Auto-route** when the destination is unambiguous (self-management language; a named, registered newsletter).
- **Suggest & wait** when there are multiple homes or it needs his judgment.
- **Flag ambiguous** when it needs more context.

---

## Soft-coded

Works for any new newsletter or project (auto-detected from the registry) and any self-management input. Add new projects to the registry and the workflow handles them.

---

## When to use

Trigger: "**clear up the dispatch**" or "**process dispatch**" — or any time Ash dumps the day.

This is the capture half of the self-management loop. The distil half (playback → reflect → update `Patterns.md`) runs weekly via `/Context/Reflection Protocol.md`.
