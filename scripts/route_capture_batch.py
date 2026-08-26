#!/usr/bin/env python3
"""Create reviewable routing proposals from Charlotte capture_queue.jsonl.

This batch is deliberately proposal-only. Approval and downstream writes belong to
Ash’s Telegram and IDE flows, so a run can never silently modify the vault.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

CATEGORY_RULES = (
    ("self-management", ("energy", "tired", "focused", "focus", "sleep", "today", "reflect", "felt")),
    ("newsletter", ("newsletter", "issue", "subscriber", "substack")),
    ("project", ("udyaan", "project", "customer", "offer", "prototype", "build")),
    ("domain", ("skill", "workflow", "prompt", "system", "learn")),
)


def _text(record: dict) -> str:
    for key in ("text", "content", "title", "capture"):
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def classify(text: str) -> str:
    lowered = text.casefold()
    for category, keywords in CATEGORY_RULES:
        if any(re.search(rf"\b{re.escape(keyword)}\b", lowered) for keyword in keywords):
            return category
    return "ambiguous"


def make_proposal(record: dict, line_number: int) -> dict:
    text = _text(record)
    category = classify(text)
    proposal = {
        "source_line": line_number,
        "capture": text,
        "category": category,
        "action": "review",
        "approval": {"telegram": False, "ide": False},
        "writes": [],
    }
    if category == "self-management":
        proposal["suggested_destination"] = "00 Self-Management/Weeks/Week <ISO>.md"
    elif category == "newsletter":
        proposal["suggested_destination"] = "02 Projects/Newsletter Becoming the Person Your Goals Belong To/"
    elif category == "project":
        proposal["suggested_destination"] = "02 Projects/Udyaan/01 Brain Dump for Udyaan.md"
    elif category == "domain":
        proposal["suggested_destination"] = "Skills Library/"
    else:
        proposal["suggested_destination"] = "manual review"
    return proposal


def build_proposals(queue_path: Path) -> list[dict]:
    proposals = []
    for line_number, line in enumerate(queue_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        if not isinstance(record, dict):
            raise ValueError(f"line {line_number}: capture must be a JSON object")
        proposals.append(make_proposal(record, line_number))
    return proposals


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", type=Path, nargs="?", default=Path("capture_queue.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("capture-routing-proposals.json"))
    args = parser.parse_args()
    proposals = build_proposals(args.queue)
    payload = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": args.queue.as_posix(),
        "approval_required": True,
        "proposals": proposals,
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[charlotte-routing] wrote {len(proposals)} proposals to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
