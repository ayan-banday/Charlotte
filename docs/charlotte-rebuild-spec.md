---
date created: 2026-08-26
date updated: 2026-08-26
purpose: Build spec for Manas AI — Charlotte vault rebuild (grill-with-docs output)
status: ready-for-build
---

# Charlotte Rebuild — System Spec

**Audience:** Manas AI (builder). **Owner:** Ash. **Do not implement in planning session** — this document is the handoff.

**North star:** Open Obsidian → see active projects, timeline, this week's calendar → click into context → work in IDE with Charlotte using Graphify (low tokens). Capture on Telegram while walking. At 6pm: proposals on Telegram + IDE reflection trigger. Approve routes and calendar events. Never auto-commit.

---

## Problem Statement

Ash's Charlotte vault has grown entropic: build artifacts in `output/` (195MB), scratch in `tmp/` and `_codex_tmp/` (427MB+ with node_modules), orphan capture in `Void.md` (494 lines), broken workflow wikilinks, and agents that burn tokens reading the whole vault. Notion was considered for command center but rejected (clunky, lock-in, token-expensive). Ash wants Obsidian as the workspace, Graphify for agent navigation, Google Calendar for commitments-as-events, Google Drive for team file share, Telegram for capture, and IDE for execution.

---

## Solution

A four-layer system:

| Layer | Technology | Role |
|---|---|---|
| **Surfaces** | Telegram, Obsidian (+ plugins), Google Calendar, IDE | Capture, browse, schedule, execute |
| **Charlotte backend** | Thin Python or skill-orchestrated batch | Capture queue, routing batch, proposal log |
| **Vault** | Markdown in `Charlotte/` | Skills, workflows, brain dumps, week files, CONTEXT |
| **Graph** | Graphify → `.graphify/graph.json` | Agent navigation without full-vault grep |

**Not in scope:** Moving knowledge to Notion. Auto-adding commitments without approval. Community plugin zoo (max 2–3 surgical plugins).

---

## User Stories

1. As Ash, I want to brain-dump on Telegram while walking, so that I never open Notion on my phone.
2. As Ash, I want captures collected in one queue, so that I have one mental "inbox" not three.
3. As Ash, I want a 6pm batch to propose where each capture goes, so that I don't manually route notes.
4. As Ash, I want to approve or reject each proposal, so that nothing enters my commitments without consent.
5. As Ash, I want 6pm proposals on Telegram and via IDE ("reflect for today, I took a walk"), so that I can close the day from phone or laptop.
6. As Ash, I want proposals preserved in a log, so that I can review what was suggested vs what I approved.
7. As Ash, I want to open Obsidian and see project timeline (Gantt) and week calendar, so that I know what I'm working on without Notion.
8. As Ash, I want commitments as Google Calendar events (deliverable + time block), so that I think in events not task lists.
9. As Ash, I want to click a project in Obsidian and land in brain dump / intro / skills, so that context is one click away.
10. As Ash, I want to work in Cursor/Claude Code/Codex with Charlotte, so that copy, decks, and newsletters run end-to-end in IDE.
11. As Ash, I want Charlotte to query Graphify before reading files, so that token use stays low.
12. As Ash, I want team deliverables on Google Drive, so that teammates aren't in my git vault.
13. As Ash, I want agent build output routed to **Black Hole/** (Manus AI + IDE builds), so that entropy has one sink instead of scattered folders.
14. As Ash, I want weekly reflection only in week files via IDE, so that daily notes plugin is not part of the capture loop.
15. As Ash, I want Graphify corpus v1 curated (Projects, Skills, Workflows, System, Context), so that graph builds fast and stays clean.
16. As Ash, I want file adds to update indexes automatically, so that I don't manually sync registry/index.
17. As Ash, I want naming conventions enforced on new files, so that wikilinks don't break.
18. As Ash, I want a vault cleanup removing ~600MB scratch and orphan capture, so that entropy stops compounding.
19. As Ash, I want API connectors (Telegram, GCal, Drive) as thin skill stubs, so that agents know how to invoke them (Ash wires credentials).
20. As Ash, I want Matt Pocock skills in `.agents/skills/` only, vault skills in `Skills Library/`, so that nothing is duplicated.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│ SURFACES                                                     │
│  Telegram (capture) │ Obsidian (browse + Gantt) │ GCal       │
│  IDE (execute + reflect + approve)                           │
└────────────┬─────────────────┬───────────────────────────────┘
             │                 │
             ▼                 ▼
┌──────────────────────────────────────────────────────────────┐
│ CHARLOTTE BACKEND (thin)                                     │
│  capture_queue.jsonl │ routing_batch (6pm) │ proposals.log    │
│  router (reads graph + rules, does NOT read whole vault)     │
└────────────┬───────────────────────────────────────────────────┘
             │
     ┌───────┴────────┐
     ▼                ▼
┌─────────────┐  ┌──────────────────────┐
│ VAULT (.md) │  │ GRAPHIFY graph.json  │
│ source of   │  │ agent navigation     │
│ truth       │  │ curated corpus v1    │
└─────────────┘  └──────────────────────┘
     │
     ▼
┌─────────────┐
│ Black Hole/ │  ← routed agent + Manus build output (gitignored contents)
└─────────────┘
             │
             ▼
┌──────────────────────────────────────────────────────────────┐
│ EXTERNAL (not in vault git)                                  │
│  Google Drive — team artifacts                               │
│  Google Calendar — approved commitments as events            │
└──────────────────────────────────────────────────────────────┘
```

### Day flow

| Time | Action |
|---|---|
| Walk | Telegram → Capture Queue |
| Work | IDE + Graphify query → 3–5 files → workflow |
| 6pm | Routing Batch → Proposals → Telegram + IDE |
| 6pm+ | Ash approves → routes execute, GCal events created |
| Reflect | IDE "reflect for today…" → week file after confirm |
| Weekly | `weekly reflection` → Patterns.md |

---

## Workflow execution (newsletter, copy, webinar, builds)

**Principle:** Obsidian = *what to work on*. IDE + Charlotte = *how to do the work*. Graphify = *which files to read* (not the whole vault).

### Three layers for any work session

| Layer | Where | What happens |
|---|---|---|
| **Orient** | Obsidian Command Center + Google Calendar | See active projects, Gantt, this week's events (each event = deliverable + time block) |
| **Discover** | IDE — one sentence | Charlotte queries Graphify → workflow + skills + project intro (3–8 files max) |
| **Execute** | IDE — workflow steps | Run skills in order; saves to project markdown; raw builds → `Black Hole/` |

### How Charlotte picks a workflow

1. **Trigger phrase** — `CLAUDE.md` triggers: `write a newsletter`, `clear up the dispatch`, etc.
2. **Graphify query** — "newsletter workflow Ash voice" → `Write a Newsletter.md` + skill chain
3. **Project intro** — `02 Projects/<Project>/00 Introduction…` lists phases → workflows per phase ([[Claude Workflow Discovery Pattern]])
4. **Calendar event title** — event "Newsletter draft" → Charlotte loads newsletter workflow (title → intent map in router config)

### Workflow map (existing vault)

| You want to… | Say / GCal event | Workflow file | Skill chain (examples) |
|---|---|---|---|
| Write newsletter | `write a newsletter` | `Workflows/Write a Newsletter.md` | `newsletter-writing-system` → `content-hook-research` → `ash-newsletter-voice` → `text-humanizer` → `newsletter-image-generator` |
| Email campaign | `build an email campaign` | `Workflows/Build an Email Campaign.md` | `email-campaign-writer`, `email-sequence`, `direct-response-copy` |
| Webinar | `help with the webinar` | `Workflows/Launch a Webinar Funnel.md` | `webinar-planning` → hook → intro → value → transition → close |
| Welcome sequence | design welcome sequence | `Workflows/Design a Welcome Sequence.md` | `email-sequence`, `jani-voice` (if client) |
| Poster / ad copy | "write copy for [X]" | Skill direct (no full workflow) | `direct-response-copy`, `short-form-content`, or client `jani-voice` |
| Deck / presentation | Manus AI or "build deck" | Manus handoff | Output → `Black Hole/` → you promote to Drive or project |
| Capture routing | evening / `process captures` | `Workflows/Process Idea Batches.md` (session) + evening batch (automated) | router + approval |
| Weekly reflection | `weekly reflection` | `Context/Reflection Protocol.md` | week file → Patterns.md |

### Token budget per session (target)

| Always load | ~tokens |
|---|---|
| `SOUL.md` + `MEMORY.md` | ~2k |
| One workflow file | ~1–3k |
| 2–5 skill files (workflow declares them) | ~5–15k |
| Project intro + brain dump (if needed) | ~2–8k |
| Graphify query result (paths only) | ~500 |
| **Do not load** | File Structure Registry, all intros, Skills Index, Void |

### Black Hole routing

| Output type | First landing | After you're happy |
|---|---|---|
| Manus AI deck/PDF/exports | `Black Hole/<date>-<slug>/` | Drive (team) or `02 Projects/<Project>/` + link in intro |
| IDE-generated PPTX/PDF scratch | `Black Hole/` | Same, or delete |
| Newsletter draft (final) | `02 Projects/Newsletter…/Draft…md` | not Black Hole |
| Newsletter banner image | `assets/` or project folder | not Black Hole |
| Canonical doc figures | `assets/<project>/` | never Black Hole |

Evening batch may **propose** promoting a Black Hole folder to Drive/project; you approve like any other proposal.

### User journey diagrams

See `docs/charlotte-user-journeys.md`.

---

## Implementation Decisions

### Phase 1 — Vault hygiene (no new features)

1. Create `Black Hole/` at vault root with `00 Introduction to Black Hole.md` (routing rules for Manus + agents).
2. Migrate `output/` + `tmp/` + `_codex_tmp/` into `Black Hole/_legacy-migrate/` or Drive; then delete originals.
3. Gitignore: `Black Hole/**` (keep intro committed), `output/`, `tmp/`, `_codex_tmp/`, `**/node_modules/`, `.graphify/cache/`.
4. Route `Void.md` (494 lines) through one manual review session → brain dumps / archive; retire Void as capture surface.
5. Activate `00 Inbox/capture-queue.md` or `capture_queue.jsonl` as single staging (not Dispatch + Void).
6. Fix 20 broken workflow wikilinks (alias → lowercase-hyphenated skill names).
7. Run `sync claude.md` / update File Structure Registry + Projects Index + Workflows intro counts.
8. Merge or archive `Udyaan - From Idea to Business` into `Udyaan` (duplicate).
9. Park `Webinar Funnel` → `03 Projects Archive/` (Q3 pivot documented in MEMORY).
10. Standardize brain dump naming: `01 Brain Dump for [Project].md` everywhere.

### Phase 2 — Graphify integration

1. Ash has Graphify installed locally — builder runs against Charlotte vault.
2. Corpus v1 paths: `02 Projects/`, `Skills Library/`, `Workflows/`, `System/`, `Context/`.
3. Output: `.graphify/graph.json` + optional Obsidian export (do not duplicate vault).
4. Document `/graphify query` patterns in `Skills Library/Infrastructure & Tools/graphify-navigation.md`.
5. Charlotte bootstrap: query graph before bulk file reads (update CLAUDE.md pointer, not full constitution rewrite).

### Phase 3 — Capture + routing backend

1. Telegram bot → append to `capture_queue.jsonl` (or single markdown queue file).
2. Routing batch script/skill at 18:00 local:
   - Read queue + graph (project names, newsletter names from graph/registry)
   - Classify: self-mgmt → week file proposal; named newsletter → brain dump proposal; ambiguous → needs Ash
   - Write `01 Daily Logs/Routing Proposals YYYY-MM-DD.md` (preserved proposals)
   - Send Telegram summary (Ash configures bot)
3. IDE trigger: `reflect for today` / evening reflection → same proposal set in chat.
4. Approval handler: on approve → append to targets; on reject → log; never auto-add GCal.
5. Deprecate `run-que.cmd` + Notion Que workflow (or keep Notion as fallback ingest only if Telegram down).

### Phase 4 — Obsidian workspace

1. Install community plugins (max 2–3):
   - **Smart Gantt** (Ash's choice) — Gantt from dated tasks in notes; drag bars to reschedule; embed `gantt` blocks. Primary Obsidian timeline view.
   - Optional: Google Calendar remains the commitment store; dated events/tasks in vault notes feed Smart Gantt.
2. Create dashboard note: `00 Command Center.md` with embedded Gantt, links to active projects, week calendar embed.
3. Commit `.obsidian/community-plugins.json` + plugin configs to git (unlike workspace.json).
4. Obsidian URI scheme documented on project intro notes for quick open.
5. Disable or ignore daily-notes plugin for capture loop (week files only).

### Phase 5 — Commitments as calendar events

1. Approved proposals that are deliverables → create Google Calendar event (title, start/end, description = deliverables).
2. Optional: markdown mirror of dated tasks in project notes so Smart Gantt can render them. Calendar events stay in Google Calendar.
3. No Notion tasks DB. No Obsidian Tasks plugin required for v1.

### Phase 6 — Connector skill stubs

Create thin skills in `Skills Library/Infrastructure & Tools/`:

| Skill file | Invokes |
|---|---|
| `telegram-capture.md` | Bot send/receive patterns |
| `google-calendar-events.md` | Create/update events as commitments |
| `google-drive-artifacts.md` | Upload team files, link from project intro |

Ash wires API keys via Codex/Cursor connectors. Skills document invocation only.

### Phase 7 — Auto-index on git commit (sync layer)

**There is no watcher app.** Sync runs when Ash commits (and optionally 17:30 before 6pm batch).

1. `git config core.hooksPath .githooks` → `post-commit` runs `scripts/charlotte-sync.sh`
2. `scripts/charlotte_index.py` (Manus builds):
   - Scan `02 Projects/*/` → intro path, brain dump path, parse `## Key Workflows` wikilinks
   - Scan `Workflows/*.md` → trigger phrases
   - Scan `Skills Library/**/*.md` → name + path only
   - Write `vault-index.json` (schema: `docs/vault-index.example.json`)
3. Mirror one row into `02 Projects/Projects Index.md` if project added (script or skill)
4. `graphify --update` on corpus v1 (incremental)
5. **Acceptance:** new project + commit → next agent reads index entry without Registry

Optional: Windows Task Scheduler 17:30 → `scripts/run-charlotte-sync.cmd`

### Phase 3b — project-creator rewrite (done in spec branch)

- Template: intro + `01 Brain Dump for [Project].md` only
- Skill: `Skills Library/Infrastructure & Tools/project-creator.md`
- Ash: "new project" in IDE → interview → folder → **commit** → synced

---

## Vault Cleanup Tally

### DELETE (safe)

| Path | Size | Reason |
|---|---|---|
| `tmp/` | 237MB | Deck build scratch + node_modules |
| `_codex_tmp/` | 190MB | Duplicate rebuild scratch |
| `output/` (after migrate) | 195MB | Entropy sink; 3 duplicate Udyaan deck variants |

### MIGRATE then remove

| Path | Destination |
|---|---|
| `output/udyaan-playable-layer*` | `Black Hole/_legacy/` then Drive or project |
| `output/pdf/*.pdf` | `Black Hole/_legacy/` then Drive |
| `05 Notes and Ideas/Random Ideas/Void.md` | Route bullets → brain dumps; archive file |

### KEEP (core vault)

| Path | Files | Role |
|---|---|---|
| `System/` | 3 | SOUL, MEMORY, Recall |
| `Context/` | 7 | Rules, protocols |
| `Skills Library/` | 79 md | Ash skills |
| `Workflows/` | 8 | Multi-step workflows |
| `02 Projects/Udyaan/` | active | Primary project |
| `02 Projects/Newsletter…/` | active | Newsletter project |
| `02 Projects/Deep Generalist…/` | active | Jani encoding |
| `00 Self-Management/` | 22 | Weeks, goals, patterns |
| `assets/` | 9 imgs, 16MB | Canonical doc figures (G9, Udyaan course) |
| `.agents/skills/` | 37 | Matt Pocock agent skills |
| `Black Hole/` | routed sink | Manus + agent builds (contents gitignored) |

### PARK / ARCHIVE

| Path | Action |
|---|---|
| `02 Projects/Webinar Funnel (Procrastination)/` | → `03 Projects Archive/` |
| `02 Projects/Udyaan - From Idea to Business/` | Merge into Udyaan or archive |
| `02 Projects/Tanzeer call learning bottleneck/` | Archive if inactive |

### GITIGNORE additions

```
Black Hole/**
!Black Hole/00 Introduction to Black Hole.md
output/
tmp/
_codex_tmp/
**/node_modules/
.graphify/cache/
capture_queue.jsonl
```

---

## Skills to Invoke (Matt Pocock + vault)

| When | Skill | Notes |
|---|---|---|
| Planning (done) | `grill-with-docs`, `domain-modeling` | Produced this spec |
| Large build map | `wayfinder` | If implementation spans many sessions |
| Repo setup | `setup-matt-pocock-skills` | Issue tracker for build tickets |
| Spec → tickets | `to-spec`, `to-tickets` | Optional if using GitHub issues |
| Per ticket | `implement`, `tdd`, `code-review` | Backend + hooks |
| Vault reorg | `improve-codebase-architecture` | Before folder moves |
| Agent docs | `writing-for-agents` | Slim CLAUDE.md pointers |
| API setup | Ash's connectors | Not `wizard` — Ash self-serve |

**Storage rule:** Matt skills stay in `.agents/skills/`. New Charlotte operational skills in `Skills Library/Infrastructure & Tools/`. Cross-index in `Skills Index.md` only.

---

## Testing Decisions

- Routing batch: fixture `capture_queue.jsonl` with 10 sample captures → expected proposals JSON (no vault writes until approve).
- Graphify: query "Udyaan newsletter skills" returns paths without reading 79 skill files.
- Approval gate: reject path never writes to week file or GCal.
- Cleanup: vault markdown count unchanged except migrations; no broken wikilinks after link fix pass.

---

## Out of Scope

- Notion as command center or knowledge store
- Moving all knowledge to Notion
- Auto-adding tasks/projects without approval
- Building Graphify (Ash has it; builder integrates only)
- Charlotte backup (Ash maintains separate copy)
- Full custom web app dashboard (Obsidian + GCal sufficient for v1)
- Daily notes capture loop
- Research ticket for Graphify corpus (decided: curated subset v1)

---

## Further Notes

- **Attachments:** User dislikes images scattered in `03 Projects Archive/Images`. Prefer `assets/<project>/` for canonical figures; `_work/` for exports; Drive for team share. Update `app.json` `attachmentFolderPath` after reorg.
- **Google Calendar:** Events not Tasks API. Dummy timed blocks with deliverable in description is valid v1.
- **Graphify:** Ash installed locally; builder should not vendor Graphify into repo.
- **Registry:** `File Structure Registry.md` drifts from reality — refresh in Phase 1.
- **Triggers to update in CLAUDE.md:** Replace Notion Que emphasis with Telegram capture + evening batch; add `reflect for today` evening trigger.

---

## References

- `docs/manus-handoff.md` — **give this to Manus first**
- `CONTEXT.md` — glossary
- `docs/adr/0001`–`0006` — locked decisions
- `docs/vault-index.example.json` — index schema
- `CLAUDE.md` — Charlotte constitution (update pointers only in v1)
- `.agents/skills/` — Matt Pocock pack
