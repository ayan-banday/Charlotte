#!/usr/bin/env python3
"""Apply explicit Codex decisions to a day's pending Charlotte proposals."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

try:  # Supports both ``python scripts/...`` and imports from the test suite.
    from .telegram_routing_batch import proposal_paths, render_markdown
except ImportError:  # pragma: no cover - direct-script execution path
    from telegram_routing_batch import proposal_paths, render_markdown


DESTINATIONS = {
    "self-management": "00 Self-Management/Weeks/Week {iso_week:02d}.md",
    "newsletter": "02 Projects/Newsletter Becoming the Person Your Goals Belong To/01 Brain Dump for Newsletter Becoming the Person Your Goals Belong To.md",
    "project": "02 Projects/Udyaan/01 Brain Dump for Udyaan.md",
    "domain": "Skills Library/Infrastructure & Tools/capture-routing-review.md",
}


def parse_ids(raw: str) -> set[int]:
    return {int(value) for value in raw.split(",") if value.strip()}


def append_capture(path: Path, capture: str, proposal_date: date) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {path.stem}\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n- {capture} _(approved from {proposal_date.isoformat()} routing batch)_\n")


def apply_approvals(vault: Path, proposal_date: date, approved: set[int], rejected: set[int]) -> None:
    if approved & rejected:
        raise SystemExit("A proposal cannot be both approved and rejected.")
    json_path, markdown_path = proposal_paths(vault, proposal_date)
    document = json.loads(json_path.read_text(encoding="utf-8"))
    proposals = {proposal["id"]: proposal for proposal in document["proposals"]}
    unknown = (approved | rejected) - proposals.keys()
    if unknown:
        raise SystemExit(f"Unknown proposal IDs: {sorted(unknown)}")
    for proposal_id in rejected:
        proposal = proposals[proposal_id]
        if proposal["status"] == "pending":
            proposal["status"] = "rejected"
    for proposal_id in approved:
        proposal = proposals[proposal_id]
        if proposal["status"] != "pending":
            continue
        destination_template = DESTINATIONS.get(proposal["category"])
        if destination_template is None:
            proposal["status"] = "blocked"
            continue
        destination = destination_template.format(iso_week=proposal_date.isocalendar().week)
        append_capture(vault / destination, proposal["capture"], proposal_date)
        proposal["status"] = "approved"
        proposal["applied_destination"] = destination
        if proposal.get("calendar_status") == "requested":
            proposal["calendar_status"] = "calendar_pending"
    json_path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(document), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    parser.add_argument("--date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--approve", default="", help="Comma-separated proposal IDs")
    parser.add_argument("--reject", default="", help="Comma-separated proposal IDs")
    args = parser.parse_args()
    approved, rejected = parse_ids(args.approve), parse_ids(args.reject)
    apply_approvals(args.vault, args.date, approved, rejected)
    print(f"[charlotte-routing] applied {len(approved)} approval(s), {len(rejected)} rejection(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
