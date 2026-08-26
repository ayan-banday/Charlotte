#!/usr/bin/env python3
"""Safely initialise Charlotte's Telegram update cursor without importing backlog."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

try:  # Supports both ``python scripts/...`` and imports from the test suite.
    from .telegram_routing_batch import (
        TelegramError,
        ensure_polling_is_safe,
        get_updates,
        save_state,
        telegram_request,
    )
except ImportError:  # pragma: no cover - direct-script execution path
    from telegram_routing_batch import TelegramError, ensure_polling_is_safe, get_updates, save_state, telegram_request


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    args = parser.parse_args()
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise SystemExit("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be configured as environment secrets.")
    try:
        ensure_polling_is_safe(telegram_request, token)
        updates = get_updates(telegram_request, token, None)
        matching = [
            update for update in updates
            if str(update.get("message", {}).get("chat", {}).get("id")) == str(chat_id)
        ]
        if not matching:
            raise TelegramError("No message from TELEGRAM_CHAT_ID found. Send /start to the bot and retry.")
        last_update_id = max(update["update_id"] for update in updates if isinstance(update.get("update_id"), int))
        save_state(args.vault.resolve() / "01 Daily Logs/.telegram-capture-state.json", last_update_id)
        telegram_request(token, "sendMessage", {"chat_id": chat_id, "text": "Charlotte 5:30 p.m. capture batch is connected."})
    except TelegramError as error:
        raise SystemExit(f"[charlotte-telegram] {error}") from error
    print("[charlotte-telegram] cursor initialised without importing historical messages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
