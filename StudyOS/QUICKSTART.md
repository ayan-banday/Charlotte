# QUICKSTART

The 5-minute path from an empty `courses/registry.md` to your first study session. Works even with
**zero official materials** — the system just states a lower confidence ceiling and runs anyway.

---

## a) Add a course row

Open `courses/registry.md` and add one row to the table with the course name, a one-line note on
what it assesses, and a default gap-closure type (`quantitative` | `qualitative` | `applied` — see
the chooser in that file, or `system/spec.md` §2). Leave **Guide status** as `NOT BUILT` and
**Confidence ceiling** as `—` for now.

## b) Fill the course's context.md

Copy `courses/_TEMPLATE_context.md` to `courses/<Course>/context.md` and answer its ~4 questions:

1. What is the assessment, actually (exam / certification / coursework / self-set goal)?
2. What's its format & structure (papers, question types, timing, weighting — "unknown" is fine)?
3. Do official materials exist (syllabus / past papers / rubric)? Yes, partial, or no — and where,
   if yes.
4. Default gap-closure type, and why.

Plus an optional deadline if there's a real assessment date. This takes about 3 minutes and it's the
one file everything else is built from.

## c) (Optional) Drop materials in inputs/

If you have a syllabus, past papers/assessments, notes, or model answers, put them in
`inputs/<Course>/<Topic>/`. **Not required.** If you skip this, say so when you start the guide build
— the system will build on `[INFERRED]` content and state the confidence ceiling out loud instead of
faking authority it doesn't have.

## d) Build the course guide

Tell Claude: *"Build the [Course] guide."* This runs prompt `system/prompts/01_course_guide_prompt.md`
(mechanics in `system/playbooks/01_build_guides.md`). It reads your `context.md` and any `inputs/`,
researches to fill gaps, and produces `courses/<Course>/course_guide.md` — a validated model of how
the assessment thinks, with every claim tagged `[SOURCED]` or `[INFERRED]`. Update the course's row
in `courses/registry.md` (status → `BUILT`, ceiling → the validated %) when it's done.

## e) Name a topic

Tell Claude: *"I want to study [Topic] for [Course]."* This runs prompt
`system/prompts/02_topic_session_prompt.md`. Claude builds a `topic_guide.md`, proposes a cluster
breakdown, and — once you approve — generates clusters **one at a time**, each with a study sheet
and a set of adversarial questions (every question has a real trap; no recall-level questions).

## f) Submit answers → gaps tracked

Paste your answers (written, or a raw transcript) or self-rate them. Claude grades, detects
confident-but-wrong answers and confident-sounding guesses, and updates the gap tracker
(`master_status.md`, `flags.md`, `gaps/<Course>/<Topic>_gaps.md`). Ask for the next cluster or the
next question set, and repeat until convergence — ACTIVE gaps at zero, FRAGILE gaps few, full
coverage — verified on a real past assessment if one exists, or an explicitly-flagged model test if
it doesn't.

---

That's the whole loop. Full rules live in `SYSTEM.md`; full logic in `system/spec.md`.
