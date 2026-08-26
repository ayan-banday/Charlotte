---
date created: 2026-08-26
date updated: 2026-08-26
---
# Telegram Capture Connector

## Purpose

Describe the GitHub-hosted connector contract for walk-time captures. The 17:30 Asia/Kolkata batch imports unseen Telegram messages and preserves them in that day's routing-proposal JSON. It then sends a concise review to Telegram.

## Contract

- Input: Telegram message text plus received timestamp and message ID.
- Storage: `01 Daily Logs/Routing Proposals YYYY-MM-DD.json` plus its Markdown companion.
- Output: a 17:30 Telegram review directing Ash to Codex for approval.
- Downstream: `reflect for today` is the sole approval surface; it creates no calendar event until explicitly approved and configured.

## Credential boundary

Store `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` as GitHub Environment secrets named `charlotte-automation`. Never commit tokens, webhook URLs containing secrets, or `.env` files to this vault.
