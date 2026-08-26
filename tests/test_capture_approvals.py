import json
from datetime import date
from pathlib import Path

from scripts.apply_capture_approvals import apply_approvals
from scripts.telegram_routing_batch import proposal_paths, render_markdown


def pending_document() -> dict:
    return {
        "version": 2,
        "date": "2026-08-26",
        "generated_at": "2026-08-26T12:00:00Z",
        "approval_surface": "codex",
        "proposals": [
            {
                "id": 1,
                "capture": "A possible newsletter opening.",
                "category": "newsletter",
                "suggested_destination": "02 Projects/Newsletter Becoming the Person Your Goals Belong To/",
                "status": "pending",
                "calendar_status": "not_requested",
            },
            {
                "id": 2,
                "capture": "Unclear thought.",
                "category": "ambiguous",
                "suggested_destination": "manual review",
                "status": "pending",
                "calendar_status": "not_requested",
            },
        ],
    }


def test_approval_routes_only_explicitly_approved_capture(tmp_path: Path):
    proposal_date = date(2026, 8, 26)
    json_path, markdown_path = proposal_paths(tmp_path, proposal_date)
    json_path.parent.mkdir(parents=True)
    document = pending_document()
    json_path.write_text(json.dumps(document), encoding="utf-8")
    markdown_path.write_text(render_markdown(document), encoding="utf-8")

    apply_approvals(tmp_path, proposal_date, {1}, {2})

    updated = json.loads(json_path.read_text(encoding="utf-8"))
    assert [proposal["status"] for proposal in updated["proposals"]] == ["approved", "rejected"]
    target = tmp_path / "02 Projects/Newsletter Becoming the Person Your Goals Belong To/01 Brain Dump for Newsletter Becoming the Person Your Goals Belong To.md"
    assert "newsletter opening" in target.read_text(encoding="utf-8")
    assert not (tmp_path / "manual review").exists()
