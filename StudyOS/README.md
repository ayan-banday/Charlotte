# StudyOS

An anti-bullshit engine for studying anything with a real assessment at the end of it — an exam, a
certification, coursework, or a self-set learning goal. It works *backwards* from how the assessment
thinks: building assessor-grade guides, testing you adversarially, and tracking your real weak spots
across sessions until a topic is genuinely ready — not just until your score looks good.

> **New here? Read `QUICKSTART.md` next** — it's the 5-minute path from zero to your first study
> session. `SYSTEM.md` is the rulebook Claude follows; this README is the map for *you*.

---

## The idea

Most study tools test what you already reviewed. This one finds what you're actually weak at —
including the confident-but-wrong answers self-rating always misses — and won't let a topic be
called "done" until the gaps are closed and verified on a real assessment (or, if none exists, an
explicitly-flagged model test).

It works with **zero official materials**: give it a syllabus and past papers and it validates
itself against them; give it nothing and it still runs, just at a stated lower confidence ceiling.

---

## How it works (the loop)

1. **Add a course.** One row in `courses/registry.md` + one `courses/<Course>/context.md` describing
   what the assessment actually is. Takes a few minutes — see `QUICKSTART.md`.
2. **(Optional) drop materials** — syllabus, past papers, notes, model answers — into
   `inputs/<Course>/<Topic>/`.
3. Claude builds the **course guide** (once per course) and, per topic, a **topic guide**, validated
   against held-out materials where they exist (the "90% check").
4. Claude proposes a **cluster breakdown** (named subtopics). You approve, then ask for clusters
   **one at a time**. Each comes with a study sheet.
5. You study a cluster, then Claude gives you **adversarial questions** — every one has a trap.
6. You answer — paste a transcript or self-rate each answer. Claude grades, detects where you were
   actually confident vs guessing, and updates your **gaps**.
7. Repeat across clusters. Claude keeps generating questions targeting your **recurring gaps** plus
   **untested** parts of the topic.
8. When gaps are closed, take a **model test**, then — if one exists — a **real past assessment**
   under timed conditions. That's the honesty check that decides if you're actually ready.

---

## Folder map

| Folder / file | What it is | Who fills it |
|---|---|---|
| `SYSTEM.md` | The rulebook Claude follows every session (laws + map + checklists) | Already set up |
| `QUICKSTART.md` | The 5-minute path to your first course + session | Already set up |
| `system/spec.md` | The full spec — single source of truth for the engine's logic | Already set up |
| `courses/registry.md` | One row per course: what it assesses, gap-closure type, guide status | **You** |
| `courses/<Course>/context.md` | Per-course details — copy from `courses/_TEMPLATE_context.md` | **You** |
| `system/prompts/` | Conversational entry points Claude follows | Already set up (don't edit) |
| `system/playbooks/` | Step-by-step mechanics behind each prompt | Already set up (don't edit) |
| `system/templates/` | Blank skeletons Claude copies for generated files | Already set up (don't edit) |
| `inputs/<Course>/<Topic>/` | Raw materials (optional): past papers, syllabus, notes, model answers | **You** (optional) |
| `gaps/<Course>/<Topic>_gaps.md` | Rolled-up weak spots per topic | Claude (generated) |
| `courses/<Course>/<Topic>/` | Topic guide, clusters, study sheets, gap tracking, tests | Claude (generated) |

**Plain definitions:**
- **Prompt** = a conversational entry point Claude follows (e.g. "run a topic session"). **Playbook**
  = the how-to mechanics a prompt invokes. You never run these yourself; Claude reads them.
- **Template** = a blank fill-in-the-shape file so every generated `master_status.md` looks the
  same regardless of course. You never edit these; Claude copies them.
- **Inputs** = raw materials you optionally provide. **Gaps** = the output showing what you're
  actually weak at.

---

## How to start a session (what to say to Claude)

- *"Build the [Course] guide from the inputs."* → Claude runs the course-guide playbook.
- *"I want to study [Topic] for [Course]."* → Claude builds the topic guide, proposes clusters,
  waits for your approval.
- *"Generate the next cluster."* → one cluster + study sheet.
- *"Give me questions on this cluster."* → adversarial question set.
- *"Here's my transcript / here are my answers."* → Claude grades, updates gaps, builds the next set.
- *"Are we converged on this topic?"* → Claude checks the three convergence conditions.

---

## Next step

Nothing is set up yet — `courses/registry.md` is empty. Go to `QUICKSTART.md` and add your first
course.
