import json
from pathlib import Path

from scripts.route_capture_batch import build_proposals


def test_build_proposals_classifies_without_writing_vault(tmp_path: Path):
    queue = tmp_path / "capture_queue.jsonl"
    queue.write_text(
        json.dumps({"text": "I felt tired today and could not focus"}) + "\n"
        + json.dumps({"text": "Idea for this week's newsletter"}) + "\n"
        + json.dumps({"text": "Need to test the Udyaan offer"}) + "\n"
        + json.dumps({"text": "Maybe create a new skill"}) + "\n"
        + json.dumps({"text": "Something I cannot classify"}) + "\n",
        encoding="utf-8",
    )

    proposals = build_proposals(queue)

    assert [proposal["category"] for proposal in proposals] == [
        "self-management",
        "newsletter",
        "project",
        "domain",
        "ambiguous",
    ]
    assert all(proposal["approval"] == {"telegram": False, "ide": False} for proposal in proposals)
    assert all(proposal["writes"] == [] for proposal in proposals)
    assert not (tmp_path / "00 Self-Management").exists()


def test_build_proposals_accepts_content_and_preserves_source_line(tmp_path: Path):
    queue = tmp_path / "capture_queue.jsonl"
    queue.write_text('\n{"content": "a short thought"}\n', encoding="utf-8")

    proposals = build_proposals(queue)

    assert proposals == [
        {
            "source_line": 2,
            "capture": "a short thought",
            "category": "ambiguous",
            "action": "review",
            "approval": {"telegram": False, "ide": False},
            "writes": [],
            "suggested_destination": "manual review",
        }
    ]
