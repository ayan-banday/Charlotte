---
date created: 2026-08-26
date updated: 2026-08-26
---
# Telegram Capture Connector

## Purpose

Describe the connector contract for walk-time captures. The connector receives a message from Ash, appends one JSON object per line to the repository’s `capture_queue.jsonl`, and returns a concise acknowledgement.

## Contract

- Input: Telegram message text plus received timestamp and message ID.
- Storage: append-only `capture_queue.jsonl` at the vault root.
- Output: acknowledgement containing the queue position or message ID.
- Downstream: the evening routing batch reads the queue and creates proposals only.

## Credential boundary

Ash configures the Telegram bot token in the Cursor/Codex connector. Never commit tokens, webhook URLs containing secrets, or `.env` files to this vault.
