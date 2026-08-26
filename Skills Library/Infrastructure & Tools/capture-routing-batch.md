---
date created: 2026-08-26
date updated: 2026-08-26
---
# Capture Routing Batch

## Purpose

Turn newly imported Telegram captures into a reviewable proposal log during the 17:30 Asia/Kolkata GitHub batch. The batch classifies captures and suggests destinations, but it does not write project notes, week files, or Google Calendar events.

## Run

```bash
python scripts/telegram_routing_batch.py --vault .
```

## Approval gate

Every proposal starts as `pending`. A proposal may execute only after Ash approves it in Codex through `reflect for today`; Telegram is review delivery only. Rejected and ambiguous proposals remain untouched and require manual handling.

## Categories

Self-management captures suggest the current ISO week file. Newsletter captures suggest the newsletter project. Project captures suggest the relevant project brain dump. Domain captures suggest the Skills Library. Ambiguous captures go to manual review.

## Invariants

The script is deterministic, idempotent for the same input, and proposal-only. Credential setup for Telegram, Google Calendar, and Google Drive is intentionally outside this skill.
