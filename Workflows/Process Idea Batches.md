---
date created: 2026-05-11
date updated: 2026-08-30 — Rebuilt as the Obsidian routing protocol used by Process The Queue.
---

# Process Idea Batches

**Problem:** Raw captures are useful only after they become readable, attributable information in the right Obsidian homes.

**Outcome:** A normalized batch, a routing preview, and approved Obsidian writes. The source capture remains intact.

## Input

Use a normalized batch from the Notion Queue or a direct day dump. Treat the Queue as raw capture, never as the durable knowledge home.

## Steps

### 1. Normalize before routing

Separate the raw material into:

- Self-management: actions, timing, state, energy, obstacles, social context, and patterns.
- Learning and strategy: claims, evidence, questions, and applied insights.
- Active-project material.
- Parked ideas with no active project.
- Ambiguous material.

Preserve the underlying meaning. Group duplicates and turn fragments into readable bullets; do not invent facts.

### 2. Compare the relevant context

- Self-management: read the current ISO week file and today’s plan, if present.
- Project material: read the active project introduction and its immediate brain dump.
- Strategic work: read the current RGS and month goals when a captured item concerns an active strategic barrier.

Show the comparison as completed, unverified, or changed. A missing Queue mention is unverified, never assumed failed.

### 3. Prepare a routing preview

Use this format before any write:

```markdown
## Queue routing preview — YYYY-MM-DD

### Self-management → Week [ISO], [weekday]
- [readable factual bullets]

### Active project → [project brain dump]
- [claim, evidence, question, or next test]

### The Void → [heading]
- [parked idea]

### Needs direction
1. [item] → proposed destination and reason
```

### 4. Ask for placement confirmation

Show all proposed routes. Ash can approve all, reject an item, or redirect it. Do not write ambiguous routes without a destination decision.

### 5. Write and log approved routes

- Append self-management data under today’s weekday in the current week file.
- Append project material to that project’s `01 Brain Dump` unless Ash explicitly asks for a dedicated artifact.
- Append inactive ideas to `00 Inbox/The Void.md` with a reopening condition.
- Append one entry to `00 Inbox/Queue Routing Log.md` with source date, destinations, and whether the Notion raw source was retained.

Do not edit or delete the raw Notion Queue. The routing log is the idempotency record.

## Decision boundaries

| Material | Default destination | Confidence needed |
|---|---|---|
| Day actions, state, energy, timing | Current week file | Clear factual capture |
| Active venture hypothesis or market-research work | Venture-Scale Opportunity brain dump | Matches active project scope |
| Active project work | That project’s brain dump | Existing project clearly named or matched |
| Inactive content, brand, or future ideas | The Void | No active project or commitment |
| Multi-home or unclear material | Needs direction | Ash decides |
