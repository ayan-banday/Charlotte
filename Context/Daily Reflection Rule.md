---
date created: 2026-04-29
date updated: 2026-09-10 — Added the factual timeline as the standard daily reflection view.
---

# Daily Reflection Rule

**Trigger:** “reflect”, “daily reflect”, “reflect for today”, “show me my day”,
“process the queue”, “process dispatch”, or a direct day dump.

---

## What Charlotte does

1. **Load the Queue.** For a reflection request, fetch the current Notion Queue through the MCP. For a direct day dump, treat the conversation as the raw Queue batch.

2. **Play back the day before analysing it.** Start every daily reflection with a factual timeline:

   | Time | What happened |
   |---|---|
   | [exact time or range] | [activity, interaction, output, food/travel/rest, or explicitly named gap] |

   Use every usable timestamp and enough concrete detail for Ash to recognise his day. Keep uncertain timing explicitly uncertain and show unrecorded periods as gaps. Do not add a state, interpretation, or meaning column. Mark only material items inline as **Experiment**, **Recurring thought**, **Idea**, or **Decision**.

3. **Compare context.** After the timeline, show plan versus reality and extract factual self-management, learning, strategy, active-project material, and parked ideas. Compare self-management with today’s week plan and strategy with the relevant active project, RGS, and monthly goals.

4. **Preview routes before writing.** Show every proposed week-file, project, and The Void route. Preserve the detailed timeline in the week-file route. Ash approves, redirects, or leaves an item pending. An explicit “execute” after a preview approves those displayed routes.

5. **Route approved data to Obsidian.** Use `[[Process The Queue]]`; retain the raw Notion Queue and append a route record to `00 Inbox/Queue Routing Log.md`.

6. **No promotion yet.** Daily capture does **not** touch `Patterns.md` or `MEMORY.md`. Patterns graduate only on the weekly pass, on recurrence.

---

## Core pattern

Capture cheap, daily. Distil once a week. Promote only what recurs.

The Queue is raw tape. Obsidian is the durable routed record. `Patterns.md` is built from the week, not the day.
