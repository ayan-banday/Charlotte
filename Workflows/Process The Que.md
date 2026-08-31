---
date created: 2026-06-08
date updated: 2026-08-30 — Rebuilt for the current Notion Queue and approval-first Obsidian routing.
notion_queue: "https://app.notion.com/p/2e6cf3b6ca8b812eb07bf472a1fad313"
uses: "[[Process Idea Batches]]"
---

# Process The Queue

**Problem:** The Queue is the daily Notion capture surface. It holds raw thoughts, reflections, learning, and ideas that need a durable Obsidian home.

**Outcome:** Ash sees a complete, readable routing preview first. Approved material is then moved into Obsidian, while the raw Queue remains untouched.

## Triggers

- “reflect”
- “daily reflect”
- “reflect for today”
- “process the queue”
- “process dispatch” or “clear up the dispatch”

Dispatch and Queue mean the same raw-capture concept. Use the spelling **Queue** in new output.

## Workflow

### 1. Load the raw Queue

Use the Notion MCP to fetch the current Queue page. Read its text and at most its direct children. Do not follow into a child’s descendants.

### 2. Build the readable batch

Run `[[Process Idea Batches]]` Steps 1–3. Present:

- Self-management data.
- Plan-versus-reality comparison.
- Learning and strategy material.
- Active-project material.
- Parked ideas for The Void.
- Any item that needs a destination decision.

### 3. Route with Ash in the loop

Show the preview and wait for Ash’s approval or redirects. On explicit approval, run `[[Process Idea Batches]]` Step 5.

For a clearly scoped instruction such as “execute” after a preview, treat the preview’s destinations as approved.

### 4. Prevent duplicate imports

Before writing, read `00 Inbox/Queue Routing Log.md`. Compare the source date and normalized items with the prior log. Do not import an already logged item again unless Ash explicitly asks to reprocess it.

### 5. Report completion

Return the exact destinations, the inserted readable bullets, and anything still awaiting direction.

## Route map

| Queue material | Obsidian destination |
|---|---|
| Actions, timing, state, energy, social context | `00 Self-Management/Weeks/Week [ISO].md` under today |
| Venture framing, VC literacy, market-research evidence | `02 Projects/Venture-Scale Opportunity/01 Brain Dump for Venture-Scale Opportunity.md` |
| Active project material | The named project’s `01 Brain Dump` |
| Inactive content ecosystem or personal-brand work | `00 Inbox/The Void.md` |
| Unclear or multi-home material | Preview only, pending Ash’s direction |

## Safety rules

1. Never delete or rewrite raw Queue content.
2. Never infer that an unmentioned planned item failed.
3. Capture daily facts only. Promote patterns during weekly reflection, not during routing.
4. Preserve hypotheses as hypotheses. Do not commit a wedge, ICP, or strategy without Ash’s explicit decision.
5. The Notion Queue is input; Obsidian is the durable routed record.
