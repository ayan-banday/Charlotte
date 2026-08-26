---
date created: 2026-08-26
date updated: 2026-08-26
purpose: Single bootstrap doc for Manus AI — fresh environment, zero prior context
---

# Manus AI — Start Here

Ash's Charlotte vault rebuild. **Read this file first**, then the linked docs. Build phases in order. Do not skip the sync layer (Phase 2).

---

## What Ash is building

An agent-operated knowledge vault where:

- **Telegram** captures thoughts while walking
- **Obsidian** shows projects, Gantt, calendar (Smart Gantt plugin + Google Calendar)
- **IDE** (Cursor / Claude Code / Codex) runs workflows (newsletter, copy, webinar, builds)
- **Graphify** + **`vault-index.json`** let agents find files without reading the whole vault (low tokens)
- **Git commit** triggers index + graph refresh (sync point)
- **`Black Hole/`** receives Manus + agent build outputs until Ash promotes them
- **6pm batch** proposes capture routes + calendar events; Ash approves before anything commits

**Not building:** Notion as knowledge store or command center.

---

## Read order (full context)

| # | File | Why |
|---|---|---|
| 1 | This file | Bootstrap |
| 2 | `docs/charlotte-rebuild-spec.md` | Full technical spec, 7 phases |
| 3 | `docs/charlotte-user-journeys.md` | How Ash uses it day-to-day (mermaid) |
| 4 | `CONTEXT.md` | Glossary — use these terms |
| 5 | `docs/adr/0001`–`0006` | Locked decisions — do not re-litigate |
| 6 | `docs/vault-index.example.json` | Target schema for machine index |
| 7 | `CLAUDE.md` | Charlotte constitution (update pointers only in v1) |

---

## Fresh environment setup

### 1. Clone vault

```bash
git clone https://github.com/ayan-banday/Charlotte.git
cd Charlotte
git checkout cursor/charlotte-rebuild-spec-47db   # or main after merge
```

Ash's local path is `S:\Charlotte` on Windows.

### 2. Enable git sync hook (not a watcher app)

**There is no separate watcher application.** Sync runs when Ash **commits**.

```bash
git config core.hooksPath .githooks
chmod +x .githooks/post-commit scripts/charlotte-sync.sh
```

After every commit, `post-commit` → `scripts/charlotte-sync.sh` → rebuild index + Graphify update.

**Optional:** Windows Task Scheduler at 17:30 runs `scripts/charlotte-sync.sh` before 6pm batch (catches uncommitted edits).

### 3. Install Graphify (Ash may already have this)

Ash has Graphify installed locally. Builder should verify CLI works:

```bash
# One of these depending on Ash's install:
graphify --version
# or: pip install graphify-vault
```

Corpus v1 folders only: `02 Projects/`, `Skills Library/`, `Workflows/`, `System/`, `Context/`. Exclude `Black Hole/`, `tmp/`, `output/`, `node_modules/`.

### 4. Matt Pocock agent skills (already in repo)

```bash
npx skills@latest add mattpocock/skills -y
```

Repo already contains `.agents/skills/` (37 skills). Fresh clone may reinstall via above.

**Matt skills to use during this build:**

| Skill | When |
|---|---|
| `setup-matt-pocock-skills` | Once — issue tracker + `docs/agents/` layout |
| `wayfinder` | Optional — map multi-session build as decision tickets |
| `to-tickets` | Split spec phases into GitHub issues |
| `implement` | Build each phase ticket (fresh context per ticket) |
| `improve-codebase-architecture` | Before vault folder reorg |
| `writing-for-agents` | When editing CLAUDE.md / skills |
| `tdd` + `code-review` | Python sync script + router |

**Do not duplicate** Matt skill bodies into `Skills Library/`.

### 5. Obsidian (Ash's machine — document, don't automate)

Community plugins to install manually in Obsidian:

1. **Smart Gantt** — Ash's plugin. Gantt from dated tasks in notes; drag to reschedule.
2. Google Calendar remains the commitment store (events, not a task DB).

Create `00 Command Center.md` at vault root (dashboard: Gantt embed, project links).

Ash wires Google Calendar himself. Builder documents connector skill stubs only.

### 6. Credentials (Ash provides — not in repo)

Ash self-serves via Cursor/Codex connectors:

- Telegram bot token
- Google Calendar API
- Google Drive API

Thin skill stubs to create: `telegram-capture.md`, `google-calendar-events.md`, `google-drive-artifacts.md` in `Skills Library/Infrastructure & Tools/`.

---

## What Manus must build (priority order)

### Phase 1 — Sync layer (**critical — solves tokens + auto-update**)

1. **`scripts/charlotte_index.py`** — scan vault → write `vault-index.json` at repo root
   - Schema: `docs/vault-index.example.json`
   - Parse each `02 Projects/*/00 Introduction*.md` for `## Key Workflows` wikilinks → populate `workflows` array per project
   - Scan `Workflows/*.md` for trigger phrases → `triggers` map
   - Scan `Skills Library/**/*.md` → name + path only (no bodies)
2. **`scripts/charlotte-sync.sh`** — already stubbed; wire to Python indexer + `graphify --update`
3. **`.githooks/post-commit`** — already stubbed; verify on Windows (Git Bash or `charlotte-sync.cmd` wrapper)
4. **`vault-index.json`** — generated file; commit allowed or gitignore (Ash preference: commit so pull syncs index)

**Acceptance test:** Add a dummy project folder → commit → `vault-index.json` lists it → Graphify graph includes it → next Cursor session reads index only (~3KB) not Registry.

### Phase 2 — Vault hygiene

- Migrate `output/`, `tmp/`, `_codex_tmp/` → `Black Hole/_legacy/` then delete originals
- Route `Void.md` content (manual Ash review once)
- Fix broken workflow wikilinks
- Archive Webinar Funnel, merge duplicate Udyaan project
- Update `File Structure Registry.md`, `Projects Index.md`

### Phase 3 — Project template + skill

- Update `[Template] Project Name/` — intro + `01 Brain Dump for [Project].md` only (no Overview)
- Rewrite `Skills Library/Infrastructure & Tools/project-creator.md` (see updated file)
- New projects: Charlotte interview → template copy → user commits → hook syncs

### Phase 4 — Capture + 6pm routing batch

- Telegram → `capture_queue.jsonl`
- Routing batch skill/script at 18:00
- Dual approval: Telegram + IDE "reflect for today"
- Proposal log: `01 Daily Logs/Routing Proposals YYYY-MM-DD.md`

### Phase 5 — Obsidian Command Center doc + plugin config

### Phase 6 — Connector skill stubs (no credential wizard)

---

## How Ash will use it (after build)

1. **New project:** Cursor → "new project" → Charlotte interviews → creates folder from template → Ash works → **git commit** → index + Graphify update automatically
2. **Work session:** Obsidian sees GCal event → IDE → "write a newsletter" → Charlotte reads `vault-index.json` slice + Graphify query + one workflow + skills only
3. **Manus build:** outputs go to `Black Hole/<date>-<slug>/` → Ash promotes to Drive or project on commit review
4. **Every commit:** sync hook runs — next agent session is current

---

## Repo branches / PRs

| Branch | Contents |
|---|---|
| `cursor/mattpocock-skills-47db` | `.agents/skills/` Matt pack |
| `cursor/charlotte-rebuild-spec-47db` | Spec, ADRs, CONTEXT, Black Hole, this handoff |

Merge spec branch before Manus starts, or build from branch.

---

## Questions → Ash only if blocked

- Exact Graphify CLI name on Ash's Windows install
- Whether `vault-index.json` should be committed to git or local-only
- Google Calendar: which calendar ID for commitments

Otherwise: follow ADRs and spec.
