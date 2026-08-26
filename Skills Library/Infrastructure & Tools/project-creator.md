---
name: project-creator
description: Create a new vault project from the standard template (intro + brain dump). Trigger on "new project", "start a project", "create a project", "build me a project", or "I want to work on something new". Always interview before creating files. After creation, tell Ash to commit — git commit runs the sync hook (vault-index + Graphify).
---

# Project Creator

Creates `02 Projects/<Name>/` with **Option A** structure only:

```
02 Projects/<Project Name>/
├── 00 Introduction to <Project Name>.md
└── 01 Brain Dump for <Project Name>.md
```

No Overview file. No CLAUDE.md edits (token bloat). Registration happens on **git commit** via `scripts/charlotte-sync.sh` → `vault-index.json`.

Template source: `02 Projects/[Template] Project Name/`

---

## Step 1 — Interview

Ask in one message (conversational, not a form):

1. **Name** — project name?
2. **Goal** — one sentence outcome
3. **Why** — why it matters now
4. **Done looks like** — tangible outcomes (2–3 bullets)
5. **Workflows** — which workflows will power this? (newsletter, webinar, copy, custom build, etc.)
6. **Open problems** — known blockers, or "we'll discover"

Wait for answers.

---

## Step 2 — Create folder from template

1. Copy structure from `[Template] Project Name/`:
   - Rename `00 Introduction to [Template] Project Name.md` → `00 Introduction to <Project Name>.md`
   - Rename `01 Brain Dump for [Project Name].md` → `01 Brain Dump for <Project Name>.md`
2. Fill intro from interview: goal, why, success, phase = Discovery, **Key Workflows** section with exact wikilinks to `Workflows/*.md` files
3. Fill brain dump header only; leave sections sparse
4. Add more `[C]` files later as needed — not at creation

**Do not** create Overview.md.

---

## Step 3 — Register (human index only)

Add one row to `02 Projects/Projects Index.md` table (status, purpose, date).

**Do not** edit `CLAUDE.md` or `File Structure Registry.md` manually — commit hook + `sync claude.md` trigger refresh those.

---

## Step 4 — Commit reminder (critical)

Tell Ash:

> Project folder is ready. **Commit and push** when you're happy — that's what updates `vault-index.json` and Graphify so the next agent session knows this project exists.

Offer: dive into an open problem now, or add a Google Calendar event for first work block.

---

## Token rule for future sessions

When this project comes up, Charlotte reads:

1. `vault-index.json` entry (path + workflows) — ~200 bytes
2. Project intro — ~2k
3. Brain dump if mining ideas — optional
4. Workflow file + declared skills only

Never load full Projects Index or File Structure Registry for one project.
