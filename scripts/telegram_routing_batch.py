#!/usr/bin/env python3
"""Import Telegram captures and create Charlotte's dated routing proposals.

This script is deliberately proposal-only. It never writes project notes, week
files, or calendar events. It is designed for the GitHub Actions evening batch.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:  # Supports both ``python scripts/...`` and imports from the test suite.
    from .route_capture_batch import make_proposal
except ImportError:  # pragma: no cover - direct-script execution path
    from route_capture_batch import make_proposal

STATE_RELATIVE_PATH = Path("01 Daily Logs/.telegram-capture-state.json")


class TelegramError(RuntimeError):
    """A safe-to-report Telegram integration failure."""


def _api_url(token: str, method: str) -> str:
    return f"https://api.telegram.org/bot{token}/{method}"


def telegram_request(token: str, method: str, payload: dict[str, Any] | None = None) -> Any:
    data = None
    headers: dict[str, str] = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(_api_url(token, method), data=data, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as error:
        raise TelegramError(f"Telegram {method} request failed: {error.reason}") from error
    if not body.get("ok"):
        raise TelegramError(f"Telegram {method} failed: {body.get('description', 'unknown error')}")
    return body["result"]


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "last_update_id": None}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, last_update_id: int | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"version": 1, "last_update_id": last_update_id}, indent=2) + "\n",
        encoding="utf-8",
    )


def ensure_polling_is_safe(request: Callable[..., Any], token: str) -> None:
    webhook = request(token, "getWebhookInfo")
    if webhook.get("url"):
        raise TelegramError(
            "Telegram bot has an active webhook. Refusing to compete with its existing delivery mode."
        )


def get_updates(request: Callable[..., Any], token: str, last_update_id: int | None) -> list[dict[str, Any]]:
    payload: dict[str, Any] = {"timeout": 0, "allowed_updates": ["message"]}
    if last_update_id is not None:
        payload["offset"] = last_update_id + 1
    result = request(token, "getUpdates", payload)
    if not isinstance(result, list):
        raise TelegramError("Telegram getUpdates returned an invalid payload.")
    return [update for update in result if isinstance(update, dict)]


def normalized_captures(updates: list[dict[str, Any]], chat_id: str) -> list[dict[str, Any]]:
    captures: list[dict[str, Any]] = []
    for update in updates:
        message = update.get("message")
        if not isinstance(message, dict) or str(message.get("chat", {}).get("id")) != str(chat_id):
            continue
        text = message.get("text")
        if not isinstance(text, str) or not text.strip() or text.lstrip().startswith("/"):
            continue
        captures.append(
            {
                "text": text.strip(),
                "telegram": {
                    "message_id": message.get("message_id"),
                    "update_id": update.get("update_id"),
                    "received_at": datetime.fromtimestamp(
                        message.get("date", 0), tz=timezone.utc
                    ).isoformat().replace("+00:00", "Z"),
                },
            }
        )
    return captures


def proposal_paths(vault: Path, run_date: date) -> tuple[Path, Path]:
    stem = f"Routing Proposals {run_date.isoformat()}"
    return vault / "01 Daily Logs" / f"{stem}.json", vault / "01 Daily Logs" / f"{stem}.md"


def load_proposal_document(path: Path, run_date: date) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "version": 2,
        "date": run_date.isoformat(),
        "generated_at": None,
        "approval_surface": "codex",
        "proposals": [],
    }


def add_proposals(document: dict[str, Any], captures: list[dict[str, Any]]) -> int:
    existing_message_ids = {
        proposal.get("telegram", {}).get("message_id") for proposal in document["proposals"]
    }
    additions = 0
    for capture in captures:
        if capture["telegram"]["message_id"] in existing_message_ids:
            continue
        proposal = make_proposal(capture, len(document["proposals"]) + 1)
        proposal.pop("approval", None)
        proposal["id"] = len(document["proposals"]) + 1
        proposal["telegram"] = capture["telegram"]
        proposal["approval_surface"] = "codex"
        proposal["status"] = "pending"
        proposal["calendar_status"] = "not_requested"
        document["proposals"].append(proposal)
        additions += 1
    return additions


def render_markdown(document: dict[str, Any]) -> str:
    lines = [
        "---",
        f"date: {document['date']}",
        "approval surface: Codex",
        "---",
        "",
        f"# Routing Proposals {document['date']}",
        "",
        "Generated by the 17:30 Asia/Kolkata GitHub batch. Telegram receives this review; "
        "approval occurs only in Codex through `reflect for today`.",
        "",
    ]
    for proposal in document["proposals"]:
        lines.extend(
            [
                f"## {proposal['id']}. {proposal['status'].title()}",
                "",
                proposal["capture"],
                "",
                f"- Category: {proposal['category']}",
                f"- Proposed destination: `{proposal['suggested_destination']}`",
                f"- Calendar: {proposal.get('calendar_status', 'not_requested')}",
                f"- Telegram message: {proposal.get('telegram', {}).get('message_id', 'unknown')}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def send_review(request: Callable[..., Any], token: str, chat_id: str, document: dict[str, Any], additions: int) -> None:
    pending = [proposal for proposal in document["proposals"] if proposal["status"] == "pending"]
    lines = [f"Charlotte 5:30 p.m. batch complete: {additions} new capture(s), {len(pending)} pending."]
    for proposal in pending[:12]:
        excerpt = proposal["capture"].replace("\n", " ")[:120]
        lines.append(f"{proposal['id']}. {proposal['category']}: {excerpt}")
    if len(pending) > 12:
        lines.append(f"…and {len(pending) - 12} more.")
    lines.append("Open Codex and say ‘reflect for today’ to approve or reject them.")
    request(token, "sendMessage", {"chat_id": chat_id, "text": "\n".join(lines)[:4000]})


def run_batch(vault: Path, token: str, chat_id: str, run_date: date, request: Callable[..., Any] = telegram_request) -> int:
    state_path = vault / STATE_RELATIVE_PATH
    state = load_state(state_path)
    ensure_polling_is_safe(request, token)
    updates = get_updates(request, token, state.get("last_update_id"))
    captures = normalized_captures(updates, chat_id)
    json_path, markdown_path = proposal_paths(vault, run_date)
    document = load_proposal_document(json_path, run_date)
    additions = add_proposals(document, captures)
    document["generated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(document), encoding="utf-8")
    last_update_id = max((update.get("update_id") for update in updates if isinstance(update.get("update_id"), int)), default=state.get("last_update_id"))
    save_state(state_path, last_update_id)
    send_review(request, token, chat_id, document, additions)
    return additions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    parser.add_argument("--date", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise SystemExit("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be configured as environment secrets.")
    try:
        additions = run_batch(args.vault.resolve(), token, chat_id, args.date)
    except TelegramError as error:
        raise SystemExit(f"[charlotte-telegram] {error}") from error
    print(f"[charlotte-telegram] wrote proposals for {additions} new capture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
