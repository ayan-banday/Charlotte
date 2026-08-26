---
date created: 2026-08-26
date updated: 2026-08-26
---
# Capture Routing Batch

## Purpose

Turn `capture_queue.jsonl` into a reviewable proposal log during the evening batch. The batch classifies captures and suggests destinations, but it does not write project notes, week files, or Google Calendar events.

## Run

```bash
python3 scripts/route_capture_batch.py capture_queue.jsonl \
  --output "01 Daily Logs/Routing Proposals YYYY-MM-DD.json"
```

## Approval gate

Every proposal starts with both approvals set to `false`. A proposal may execute only after Ash approves it in Telegram and confirms it in the IDE with the relevant reflection or routing command. Rejected and ambiguous proposals remain untouched and require manual handling.

## Categories

Self-management captures suggest the current ISO week file. Newsletter captures suggest the newsletter project. Project captures suggest the relevant project brain dump. Domain captures suggest the Skills Library. Ambiguous captures go to manual review.

## Invariants

The script is deterministic, idempotent for the same input, and proposal-only. Credential setup for Telegram, Google Calendar, and Google Drive is intentionally outside this skill.
