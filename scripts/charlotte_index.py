#!/usr/bin/env python3
"""Build Charlotte's small, machine-readable vault index.

The index intentionally contains paths and routing metadata only. It is safe for an
agent to load at session start without reading the full Obsidian vault.
"""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

INDEX_VERSION = 1
CORPUS_DIRS = ("02 Projects", "Skills Library", "Workflows", "System", "Context")
TRIGGER_HINTS = re.compile(r"trigger|manual|when to use|say|phrase|event", re.I)
QUOTED_PHRASE = re.compile(r'[\"“]([^\"”]+)[\"”]')
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip().lower()] = value.strip().strip("'\"")
    return values


def _project_status(text: str) -> str:
    values = _frontmatter(text)
    raw = values.get("status", "")
    if not raw:
        match = re.search(r"\*\*Status:\*\*\s*([^\n]+)", text, re.I)
        raw = match.group(1).strip() if match else ""
    lowered = raw.lower()
    if any(word in lowered for word in ("archive", "parked", "retired", "complete", "completed")):
        return "parked" if "parked" in lowered else "archived" if "archive" in lowered or "retired" in lowered else "complete"
    return "active"


def _keywords(project_name: str, text: str) -> list[str]:
    # A project may opt into precise Calendar keywords in frontmatter.
    match = re.search(r"^gcal_keywords:\s*\[([^\]]*)\]", text, re.I | re.M)
    if match:
        return [item.strip().strip("'\"") for item in match.group(1).split(",") if item.strip()]
    words = re.findall(r"[a-z0-9]+", project_name.lower())
    stop_words = {"a", "an", "and", "for", "from", "the", "to", "your"}
    return [word for word in words if word not in stop_words][:1]


def _key_workflows(text: str) -> list[str]:
    heading = re.search(r"^##\s+Key Workflows\s*$", text, re.I | re.M)
    if not heading:
        return []
    remainder = text[heading.end() :]
    next_heading = re.search(r"^##\s+", remainder, re.M)
    section = remainder[: next_heading.start()] if next_heading else remainder
    found: list[str] = []
    for match in WIKILINK.finditer(section):
        name = " ".join(match.group(1).split()).strip()
        if name and name.lower() not in {"workflow name", "workflows index"} and name not in found:
            found.append(name)
    return found


def _workflow_name(path: Path) -> str:
    return re.sub(r"^\[C\]\s*", "", path.stem).strip()


def _trigger_section(text: str) -> str:
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.I | re.M))
    for index, heading in enumerate(headings):
        title = heading.group(1).lower()
        if "when to use" in title or "trigger" in title:
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            return text[heading.end() : end]
    return text


def _clean_trigger(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip(" .,:;—–-\t\n")
    value = re.sub(r"^(?:or|and)\s+", "", value, flags=re.I)
    return value.lower()


def _workflow_triggers(path: Path, text: str) -> list[str]:
    name = _workflow_name(path)
    section = _trigger_section(text)
    candidates: list[str] = []
    for line in section.splitlines():
        if not TRIGGER_HINTS.search(line):
            continue
        for quoted in QUOTED_PHRASE.findall(line):
            trigger = _clean_trigger(quoted)
            if 2 <= len(trigger) <= 100 and trigger not in candidates:
                candidates.append(trigger)
    # A workflow title is a useful canonical command when the file declares no
    # quoted phrase, and does not duplicate an explicitly declared trigger.
    canonical = _clean_trigger(name)
    if not candidates and canonical and not name.lower().endswith("index"):
        candidates.append(canonical)
    return candidates


def _workflow_files(root: Path) -> list[Path]:
    directory = root / "Workflows"
    if not directory.is_dir():
        return []
    return sorted(
        (
            path
            for path in directory.glob("*.md")
            if not path.name.lower().startswith("00 introduction")
            and not path.name.startswith("[C]")
        ),
        key=lambda path: path.name.lower(),
    )


def _skill_files(root: Path) -> list[Path]:
    directory = root / "Skills Library"
    if not directory.is_dir():
        return []
    return sorted(
        (
            path
            for path in directory.rglob("*.md")
            if not path.name.lower().startswith("00 introduction")
            and path.name.lower() not in {"skills index.md", "[c] skills index.md"}
        ),
        key=lambda path: _relative(root, path).lower(),
    )


def _project_files(root: Path) -> list[Path]:
    directory = root / "02 Projects"
    if not directory.is_dir():
        return []
    return sorted(
        (
            path
            for path in directory.iterdir()
            if path.is_dir()
            and not path.name.startswith("[Template]")
            and any(path.glob("00 Introduction*.md"))
        ),
        key=lambda path: path.name.lower(),
    )


def _first_match(paths: Iterable[Path]) -> Path | None:
    return next(iter(sorted(paths, key=lambda p: p.name.lower())), None)


def build_index(root: Path, updated_at: str | None = None) -> dict:
    root = root.resolve()
    workflow_entries = []
    triggers: dict[str, str] = {}
    for path in _workflow_files(root):
        workflow_triggers = _workflow_triggers(path, _read(path))
        relative = _relative(root, path)
        workflow_entries.append(
            {"name": _workflow_name(path), "path": relative, "triggers": workflow_triggers}
        )
        for trigger in workflow_triggers:
            triggers[trigger] = relative

    projects = []
    for folder in _project_files(root):
        intro = _first_match(folder.glob("00 Introduction*.md"))
        if intro is None:
            continue
        brain_dump = _first_match(folder.glob("01 Brain Dump*.md"))
        text = _read(intro)
        projects.append(
            {
                "name": folder.name,
                "status": _project_status(text),
                "folder": _relative(root, folder),
                "intro": _relative(root, intro),
                "brain_dump": _relative(root, brain_dump) if brain_dump else "",
                "workflows": _key_workflows(text),
                "gcal_keywords": _keywords(folder.name, text),
            }
        )

    skills = [
        {"name": path.stem, "path": _relative(root, path)} for path in _skill_files(root)
    ]
    if updated_at is None:
        updated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "version": INDEX_VERSION,
        "updated_at": updated_at,
        "sync_source": "git-commit",
        "projects": projects,
        "workflows": workflow_entries,
        "triggers": dict(sorted(triggers.items())),
        "skills": skills,
    }


def write_index(root: Path, output: Path | None = None) -> Path:
    root = root.resolve()
    destination = (output or root / "vault-index.json").resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = build_index(root)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=destination.parent, delete=False) as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(destination)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Output path; defaults to <root>/vault-index.json")
    args = parser.parse_args()
    destination = write_index(args.root, args.output)
    print(f"[charlotte-index] wrote {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
