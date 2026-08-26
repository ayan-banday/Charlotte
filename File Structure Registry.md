---
date created: 2026-05-02
date updated: 2026-08-17 — Added Graphify vault knowledge-graph operating plan.
---

# File Structure Registry

Master map of all folders and systems. Use this instead of searching to navigate quickly.

Last updated: 2026-08-17 — Graphify plan added to Context.

---

## /System/

**Purpose:** The assistant's brain — persistent memory + the rules that run it. Vault-native,
portable, token-bounded. (Hermes/OpenClaw-style, adapted to markdown.)

**Files:**
- SOUL.md (HOT, loaded every session — Charlotte persona: how the assistant talks to Ash)
- MEMORY.md (HOT, loaded every session — `## Facts` ≤2,200 chars + `## Profile` ≤1,375 chars)
- Recall.md (DEEP, retrieved on demand — durable learnings, self-compacts recursively)

**Bootstrap:** root `CLAUDE.md` (always-loaded, the full constitution) reads SOUL.md + MEMORY.md first, every session (~1.8–2.2k tokens).

---

## /00 Inbox/

**Purpose:** Unprocessed captures, working files, idea batches

**Files:**
- 00 Dispatch.md (working file for idea batches; process with "clear up the dispatch" workflow)

---

## /00 Self-Management/

**Purpose:** Find patterns. Build the durable personality profile (Patterns.md) Ash decides from.

**Structure:**
- 00 Introduction to Self-Management.md (the loop + week-file shape)
- [C] RGS.md (yearly anchor, quarterly milestones)
- Patterns.md — durable personality profile. Deep tier, grepped on demand (like Recall.md). The only self-file read day to day.
- /Weeks/ — Week [ISO].md, raw data points per week. Retained, NOT auto-read; pulled for playback only.
- /Goals/ — [C] [Month] Goals.md (monthly priorities, May–Dec 2026)
- /Archive/ — decayed patterns + old heavy weeks (Week 19–21, May), kept for reference, not auto-read.

**The loop:** dump → extract to week file → "how's my week been" playback → Ash reflects → Charlotte updates Patterns.md + the MEMORY ## Profile headline. Plugs into the memory engine (/CLAUDE.md).

---

## /01 Daily Logs/

**Purpose:** Daily notes (YYYY-MM-DD.md format)

**Files:**
- 2026-05-10.md (and earlier dates)
- Que Routing Log.md (append-only run log for the daily Process The Que routine — created on first run)

---

## /02 Projects/

**Purpose:** Active projects moving toward completion

**Core files:**
- 00 Introduction to Projects.md (project structure + guidelines)
- Projects Index.md (inventory of all active projects)

**Active Projects:**
1. **Udyaan** — Primary Q3/Q4. Smart biodegradable packaging for Oyedesi. G9 pilot.
   - `00 Introduction to Udyaan.md`
   - `01 Brain Dump for Udyaan.md`
   - `[C] Udyaan Problem Statement.md`
   - `[C] Udyaan Project Schematics.md`
   - `[C] Udyaan Developmental Plan.md` — Project Documentation Standard (7 sections)
   - `[C] G9 Banana Research.md`
   - `[C] Udyaan Packaging POA.md`
2. Webinar Funnel (Procrastination) — Parked (Q3 pivot to Udyaan)
3. Deep Generalist for Jani — Phase 1 encoding in progress
4. Newsletter Becoming the Person Your Goals Belong To — Ideation
5. Tanzeer call learning bottleneck — Brain dump space for learning process analysis (call May 19)

**Template:**
- [Template] Project Name/ (reference structure for new projects)

---

## /03 Projects Archive/

**Purpose:** Completed projects, historical reference

**Archived Projects:**
- How to Write a Newsletter
- Newsletter Do Hard Things

---

## /05 Notes and Ideas/

**Purpose:** Thinking space, raw ideas, sourcebooks

**Files:**
- Goal Drift.md
- /Sourcebooks/ (reference materials, book notes)

---

## /Context/

**Purpose:** Rules, protocols, and system documentation

**Files:**
- Claude Workflow Discovery Pattern.md
- Daily Reflection Rule.md
- Prompt Storage Rule.md
- Reflection Protocol.md
- Rule Recording Protocol.md
- Graphify Vault Knowledge Graph Plan.md (scope, operating rules, refresh path, and value model for the vault graph)
- /Goals/
  - RGS - Full details.md (expanded yearly/quarterly breakdown)

---

## /Skills Library/

**Purpose:** Reusable action sequences for specific outcomes

**Core files:**
- 00 Introduction to Skills Library.md (library overview + navigation)
- Skills Index.md (complete inventory, 41 total skills)

**Domains (5 total):**

### Marketing (13 skills)
- 00 Introduction to Marketing.md
- /Sales & Conversion Copy/ (7 skills)
  - direct-response-copy.md
  - vsl-generator/
  - email-campaign-writer/
  - email-sequence/
  - newsletter-writing-system/
  - jani-insight-email.md
  - jani-voice/
- /Webinar Architecture/ (6 skills)
  - webinar-planning.md
  - webinar-hook.md
  - webinar-intro.md
  - webinar-value.md
  - webinar-transition.md
  - webinar-close.md

### Content (15 skills)
- 00 Introduction to Content.md
- /Content Writing/ (5 skills)
  - long-form-content.md
  - short-form-content.md
  - storytelling.md
  - text-humanizer/
  - voice-correct.md
- /Content Production/ (6 skills)
  - raw-cut/
  - instagram-carousel-generator.md
  - newsletter-image-generator.md
  - jani-reels-voice.md
  - video-use/
  - manim-video.md
- /Content Ideation & Strategy/ (4 skills)
  - content-mining.md
  - newsletter-ideas-generator.md
  - content-hook-research.md
  - thought-collector.md

### Learning & Education Systems (3 skills)
- 00 Introduction to Learning & Education Systems.md
- exam-backcasting-system.md
- learning-study-coach.md
- book-to-textbook-converter.md

### Ashes Voices (2 skills)
- 00 Introduction to Ashes Voices.md
- ash-newsletter-voice.md (Newsletter Voice — narrative-forward, framework-focused)
- ash-substack-voice.md (Substack Voice — direct opinion, shorter-form thought leadership)

### Infrastructure & Tools (8 skills)
- document-docx-editor.md
- document-pdf-editor.md
- document-pptx-editor.md
- document-xlsx-editor.md
- project-creator.md
- skill-creator.md
- system-help.md
- task-scheduler.md

**Archive:**
- /Skills-OLD-BACKUP/ (legacy skills, do not use)

---

## /Workflows/

**Purpose:** Multi-skill action sequences toward complete end goals

**Core files:**
- 00 Introduction to Workflows.md (workflow structure + creation process)
- [C] Workflows Index.md (complete inventory)

**Active Workflows (6 total):**
1. Launch a Webinar Funnel.md
2. Build an Email Campaign.md
3. Design a Welcome Sequence.md
4. Process Idea Batches.md (routes captured ideas to appropriate homes — Dispatch source)
5. Write a Newsletter.md (idea → mine → hook → draft in Ash's voice → humanize → image)
6. Process The Que.md (daily automated routing from Notion Que → vault, runs nightly at 21:00)

---

## Root Files

**System Documentation:**
- CLAUDE.md (constitution: how Claude behaves, rules, protocols, memory engine)
- File Structure Registry.md (this file)

**External (Notion):**
- "The Que" database — Ash's capture surface. DB URL stored in `/Workflows/Process The Que.md` frontmatter.

---

## Key Statistics

- **Total Markdown files:** 344+ (added Process The Que.md + Que Routing Log stub)
- **Active projects:** 4 (Webinar Funnel, Deep Generalist, Newsletter Becoming the Person Your Goals Belong To, Tanzeer call learning bottleneck)
- **Active workflows:** 6 (Webinar, Email Campaign, Welcome Sequence, Process Idea Batches, Write a Newsletter, Process The Que)
- **Total skills:** 41 (across 5 domains)
- **Skills domains:** 5 (Marketing, Content, Learning & Education, Ashes Voices, Infrastructure & Tools)
- **Monthly goals:** 11 files in /00 Self-Management/Goals/ (Feb-Dec 2026; month folders removed 2026-06-07)

---

## Navigation Quick Links

For quick navigation, Claude checks:

1. **Mentioning a specific file?** → Check File Structure Registry (you are here)
2. **Mentioning a domain (e.g., "marketing")?** → Read `/Skills Library/00 Introduction to [Domain].md`
3. **Mentioning a project?** → Read `/02 Projects/00 Introduction to [Project Name].md`
4. **Mentioning a workflow?** → Read `/Workflows/00 Introduction to Workflows.md`

**Rule:** Read introductions first. They explain everything.
