import json
from datetime import date
from pathlib import Path

from scripts.telegram_routing_batch import TelegramError, run_batch


def message(update_id: int, message_id: int, chat_id: str, text: str) -> dict:
    return {
        "update_id": update_id,
        "message": {"message_id": message_id, "date": 1_778_000_000, "chat": {"id": chat_id}, "text": text},
    }


class FakeTelegram:
    def __init__(self, updates: list[dict], webhook_url: str = ""):
        self.updates = updates
        self.webhook_url = webhook_url
        self.sent: list[dict] = []

    def __call__(self, _token: str, method: str, payload=None):
        if method == "getWebhookInfo":
            return {"url": self.webhook_url}
        if method == "getUpdates":
            offset = (payload or {}).get("offset")
            return [item for item in self.updates if offset is None or item["update_id"] >= offset]
        if method == "sendMessage":
            self.sent.append(payload)
            return {"message_id": 999}
        raise AssertionError(method)


def test_batch_writes_dated_json_markdown_and_cursor(tmp_path: Path):
    telegram = FakeTelegram([message(10, 4, "42", "Newsletter idea"), message(11, 5, "99", "ignore")])

    additions = run_batch(tmp_path, "token", "42", date(2026, 8, 26), telegram)

    assert additions == 1
    payload = json.loads((tmp_path / "01 Daily Logs/Routing Proposals 2026-08-26.json").read_text())
    assert payload["proposals"][0]["status"] == "pending"
    assert payload["proposals"][0]["telegram"]["message_id"] == 4
    assert "Open Codex" in telegram.sent[0]["text"]
    assert json.loads((tmp_path / "01 Daily Logs/.telegram-capture-state.json").read_text())["last_update_id"] == 11


def test_batch_is_idempotent_for_prior_updates(tmp_path: Path):
    telegram = FakeTelegram([message(10, 4, "42", "Newsletter idea")])

    run_batch(tmp_path, "token", "42", date(2026, 8, 26), telegram)
    assert run_batch(tmp_path, "token", "42", date(2026, 8, 26), telegram) == 0
    payload = json.loads((tmp_path / "01 Daily Logs/Routing Proposals 2026-08-26.json").read_text())
    assert len(payload["proposals"]) == 1


def test_batch_refuses_active_webhook(tmp_path: Path):
    telegram = FakeTelegram([], webhook_url="https://existing.example/webhook")

    try:
        run_batch(tmp_path, "token", "42", date(2026, 8, 26), telegram)
    except TelegramError as error:
        assert "active webhook" in str(error)
    else:
        raise AssertionError("Expected active webhook to block the batch")

    assert not (tmp_path / "01 Daily Logs").exists()
