import json
from pathlib import Path

from scripts.charlotte_index import build_index


def make_vault(tmp_path: Path) -> Path:
    (tmp_path / "02 Projects" / "Acme").mkdir(parents=True)
    (tmp_path / "Workflows").mkdir()
    (tmp_path / "Skills Library" / "Content").mkdir(parents=True)

    (tmp_path / "02 Projects" / "Acme" / "00 Introduction to Acme.md").write_text(
        "---\ndate created: 2026-08-26\n---\n"
        "# Acme\n**Status:** Active\n\n"
        "## Key Workflows\n- [[Write a Newsletter]] — publish updates\n"
        "- [[Launch a Webinar Funnel]]\n",
        encoding="utf-8",
    )
    (tmp_path / "02 Projects" / "Acme" / "01 Brain Dump for Acme.md").write_text(
        "# Brain Dump\n", encoding="utf-8"
    )
    (tmp_path / "Workflows" / "Write a Newsletter.md").write_text(
        "# Write a Newsletter\n## When to use\n"
        'Trigger: "write a newsletter" or "this week\'s issue".\n',
        encoding="utf-8",
    )
    (tmp_path / "Workflows" / "Launch a Webinar Funnel.md").write_text(
        "# Launch a Webinar Funnel\n## When to use\n"
        '**Manual trigger:** "webinar funnel" or "help with the webinar".\n',
        encoding="utf-8",
    )
    (tmp_path / "Skills Library" / "Content" / "storytelling.md").write_text(
        "# Storytelling\n", encoding="utf-8"
    )
    (tmp_path / "Skills Library" / "Content" / "00 Introduction to Content.md").write_text(
        "# Content\n", encoding="utf-8"
    )
    return tmp_path


def test_build_index_discovers_project_and_key_workflows(tmp_path):
    index = build_index(make_vault(tmp_path), updated_at="2026-08-26T00:00:00Z")

    assert index["version"] == 1
    assert index["sync_source"] == "git-commit"
    assert index["projects"] == [
        {
            "name": "Acme",
            "status": "active",
            "folder": "02 Projects/Acme",
            "intro": "02 Projects/Acme/00 Introduction to Acme.md",
            "brain_dump": "02 Projects/Acme/01 Brain Dump for Acme.md",
            "workflows": ["Write a Newsletter", "Launch a Webinar Funnel"],
            "gcal_keywords": ["acme"],
        }
    ]


def test_build_index_extracts_workflow_triggers_and_skill_paths(tmp_path):
    index = build_index(make_vault(tmp_path), updated_at="2026-08-26T00:00:00Z")

    assert index["triggers"] == {
        "help with the webinar": "Workflows/Launch a Webinar Funnel.md",
        "this week's issue": "Workflows/Write a Newsletter.md",
        "webinar funnel": "Workflows/Launch a Webinar Funnel.md",
        "write a newsletter": "Workflows/Write a Newsletter.md",
    }
    assert index["workflows"] == [
        {
            "name": "Launch a Webinar Funnel",
            "path": "Workflows/Launch a Webinar Funnel.md",
            "triggers": ["webinar funnel", "help with the webinar"],
        },
        {
            "name": "Write a Newsletter",
            "path": "Workflows/Write a Newsletter.md",
            "triggers": ["write a newsletter", "this week's issue"],
        },
    ]
    assert index["skills"] == [
        {"name": "storytelling", "path": "Skills Library/Content/storytelling.md"}
    ]


def test_build_index_is_json_serializable_and_excludes_non_corpus_files(tmp_path):
    vault = make_vault(tmp_path)
    (vault / "Black Hole").mkdir()
    (vault / "Black Hole" / "secret.md").write_text("do not index", encoding="utf-8")
    (vault / "node_modules").mkdir()
    (vault / "node_modules" / "package.md").write_text("do not index", encoding="utf-8")

    index = build_index(vault, updated_at="2026-08-26T00:00:00Z")
    json.dumps(index)

    assert all("secret" not in skill["path"] for skill in index["skills"])
    assert all("node_modules" not in skill["path"] for skill in index["skills"])
