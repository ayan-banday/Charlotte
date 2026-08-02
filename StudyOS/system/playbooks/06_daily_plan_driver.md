# Playbook 06 — Study Planner (optional)

**This entire playbook is optional.** The system is fully usable session-by-session with no plan at
all — the student just names a topic and runs playbooks 01–04 (see `SYSTEM.md` §8, which does **not**
list this as a mandatory start-of-session step). Use this playbook only when the student actually
wants a schedule: a deadline to work backward from, or just an ordered backlog so they're not
deciding what to study next every day.

**When to invoke:** the student asks for a study plan, a schedule, "what should I study next," or
says something with a deadline attached ("I have a test in 5 weeks"). Never invoked automatically.

---

## What it produces

A single per-course plan file: `courses/<Course>/study_plan.md`. It is built from three inputs:

1. **The course's topic/node list** — pulled from `courses/<Course>/course_guide.md`'s content node
   map (and any existing topic guides' node maps, for topics already broken down further).
2. **The student's goal** — ask directly: what are you working toward, and is there a deadline?
3. **An optional deadline.** If given, the plan is date-driven (a day-by-day or week-by-week
   schedule). **If no deadline is given, skip the calendar entirely** — the plan is just an **ordered
   topic backlog** (priority order + rough sizing), with no dates attached.

Do not invent a deadline or a pace the student didn't ask for. A backlog with no dates is a complete,
valid plan.

---

## The protocol (run in order, only when this playbook is invoked)

1. **LOCATE.** Read `courses/<Course>/study_plan.md` if it exists. If it's date-driven, take today's
   real date and find the scheduled target (topic/cluster). If it's a backlog with no dates, the
   "target" is simply the next un-built item at the top of the list. If no plan file exists yet, this
   step produces nothing to locate — go build one (see "Building a plan" below).
2. **COMPARE** (date-driven plans only). Count clusters/topics **built** vs **scheduled-to-date**.
   Decide: **ON TRACK / BEHIND by X / AHEAD.** If BEHIND, name the specific slipped items and, if the
   plan defines a drop/priority order, point to it. For a backlog-only plan, there's nothing to
   compare against a calendar — just report position in the list.
3. **REPORT + SUGGEST.** One tight line naming today's or next's target and current progress, e.g.:
   > *"Next up: [Course] → [Topic] — [Cluster]. You're on track ([N]/[total] built). Want me to build
   > it now?"*
   Also surface anything else useful right now: build the cluster, generate its test, process a
   pending submission, or clear a pending gap cluster first.
4. **BUILD on approval.** Generate the target cluster via `02_cluster_and_study.md` (study sheet,
   grounded in `inputs/` where available, `[SOURCED]`/`[INFERRED]` tagged) + its adversarial question
   set via `03_run_session.md`. **One cluster at a time — the one at the top of the plan (or the one
   the student names). Never auto-generate the whole plan.**
5. **UPDATE the tracker.** Mark the built item done in `study_plan.md` and refresh its **current
   position** block: today's target (if dated), progress (`built/total`), status vs plan (if dated),
   last built, next to build, pending gap clusters.

No git/version-control sync step — this playbook only writes local files.

---

## Building a plan (first run for a course)

1. Read the course guide's content node map (and any topic guides that exist) to get the full topic
   list.
2. Ask the student: goal, and is there a deadline? Wait for the answer.
3. **If a deadline exists:** work backward from it to a day/week schedule, prioritizing by whatever
   signal exists (high-yield flags in guides, the student's stated weak areas, or just guide order if
   nothing else distinguishes topics). Reserve buffer time and, if relevant, time for a real-assessment
   attempt near the end (playbook 04).
4. **If no deadline:** just produce a priority-ordered backlog — no dates, no day-by-day structure.
5. Write `courses/<Course>/study_plan.md` with the schedule/backlog plus a **current position**
   tracker block. Show it to the student before treating it as authoritative — they may want to
   reorder.

---

## Gap clusters override the plan

When a test exposes a gap (per `03_run_session.md` / `spec.md` §3), the **gap cluster is the next
thing built** — ahead of the next item in the plan. Slot it in wherever the plan has room (a buffer
slot if dated; the front of the backlog otherwise). Record it in the tracker as an inserted item so
the plan stays honest about what actually got built.

## Guardrails

- One cluster on its scheduled/next turn (or on request) — not the whole plan.
- If BEHIND on a dated plan, recommend what to reprioritize or drop; don't silently let unbuilt items
  pile up unacknowledged.
- Don't predict scores or promise grades. The plan shows what to study and in what order; readiness
  is decided by playbook 04, not by the plan.
- This playbook, and the plan file it produces, are **entirely optional** — if the student never asks
  for one, never build one.
