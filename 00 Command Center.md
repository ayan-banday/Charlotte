---
date created: 2026-08-26
date updated: 2026-08-26
---
# Charlotte Command Center

The Command Center is Ash’s daily orientation surface. **Obsidian shows what to work on; Charlotte and the IDE execute the workflow; Google Calendar remains the commitment store.**

## Today

- Review the day’s commitment events in Google Calendar.
- Choose one active project and open its introduction note.
- Ask Charlotte for the workflow named in that project’s `## Key Workflows` section.
- Commit meaningful changes so `vault-index.json` and Graphify refresh.

## Active Projects

- [[02 Projects/Udyaan/00 Introduction to Udyaan|Udyaan]] — primary Q3/Q4 project; G9 packaging R&D.
- [[02 Projects/Newsletter Becoming the Person Your Goals Belong To/00 Introduction to Newsletter Becoming the Person Your Goals Belong To|Newsletter]] — ideation and publishing workflow.
- [[02 Projects/Deep Generalist for Jani/00 Introduction to Deep Generalist for Jani|Deep Generalist for Jani]] — Phase 1 encoding.
- [[02 Projects/[Template] Project Name/00 Introduction to [Template] Project Name|Project template]] — Option A: intro plus brain dump only.

## Calendar and Gantt

Google Calendar is the source of truth for commitments. Create events only after a routing proposal is approved. Each event should contain a deliverable, a time block, and a description with the expected output.

Install the **Task Gantt** community plugin manually in Obsidian. If dated task views are needed, configure the plugin to read the project’s dated markdown tasks. Do not add a second task database or move commitments into Obsidian. The optional Gantt Calendar plugin may be installed later if it improves navigation.

> Obsidian plugin installation is intentionally manual. Credentials and calendar wiring belong to Ash’s Cursor/Codex connectors, not this repository.

## Capture and Routing

Walk-time captures land in `capture_queue.jsonl`. The evening batch creates proposals only. No project note, week file, or calendar event is written until Ash approves the proposal through both Telegram and the IDE reflection flow.

- Manual workflow: [[Workflows/Process Idea Batches|Process Idea Batches]]
- Queue batch: [[Skills Library/Infrastructure & Tools/capture-routing-batch|Capture Routing Batch]]
- Daily reflection: [[Context/Daily Reflection Rule|Daily Reflection Rule]]

## Sync Status

After a commit, `.githooks/post-commit` runs `scripts/charlotte-sync.sh`. The hook regenerates [[vault-index.json]] and updates Graphify when the local CLI is installed. If Graphify is unavailable, the index still refreshes and the hook reports the skipped semantic update.

## Quick Commands

```text
new project
write a newsletter
process captures
reflect for today
weekly reflection
```
