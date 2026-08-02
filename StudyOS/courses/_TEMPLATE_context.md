<!--
Copy this file to courses/<Course>/context.md and fill it in. Takes about 3 minutes.
Unknown / not-yet-decided is a fine answer for almost every field — just say so instead of
guessing. This file is what Claude reads before building the course guide (spec.md §1, §5).
-->
---
course: [Course name]
default_type: [quantitative | qualitative | applied]
guide_status: NOT BUILT
confidence_ceiling: [unknown until the guide is built]
deadline: [optional — YYYY-MM-DD, or "none"]
last_updated: [YYYY-MM-DD]
---

# Course Context — [Course name]

## 1. What is the assessment, actually?
> Exam? Certification? Coursework? A self-set goal with no formal assessor? Say what it is in one
> or two sentences — this decides how much of the system's "official materials" logic even applies.

[...]

## 2. Format & structure
> Papers/sections, question types, timing, weighting. **"Unknown" is fine** — the course guide will
> try to establish this from inputs/research and will flag low confidence if it can't.

- Structure: [...]
- Question types: [...]
- Timing: [...]
- Weighting: [...]

## 3. Do official materials exist?
> Syllabus, past papers/assessments, mark scheme/rubric, examiner or grader reports. Pick one and
> say where they live (or that they don't exist).

- [ ] Yes — official syllabus / spec exists → where: [...]
- [ ] Yes — past papers or past assessments exist → where: [...]
- [ ] Yes — a mark scheme / rubric exists → where: [...]
- [ ] Partial — only some of the above → which: [...]
- [ ] No official materials exist at all → the guide will run on `[INFERRED]` content only and
      state a lower confidence ceiling. This is fine; say so rather than inventing sources.

## 4. Default gap-closure type
> One line to choose (full definitions in `system/spec.md` §2):
> - `quantitative` — answers are computed/derived (maths, calculations, data-handling)
> - `qualitative` — answers are explained/argued (essays, concepts, mechanisms, humanities)
> - `applied` — answers apply a framework to a source/scenario (case studies, professional
>   scenarios, source-based questions)

Default type: **[quantitative | qualitative | applied]**
Reasoning: [...]
(Individual topics can override this later in their own `topic_guide.md` front matter.)

## 5. Deadline (optional)
> A real assessment date, a certification exam window, or "none" for an open-ended goal. Only used
> if you want the optional per-course planner (`SYSTEM.md` §2, `system/playbooks/06_daily_plan_driver.md`)
> — most courses don't need one.

[...]

## 6. Confidence ceiling note
> Leave as "unknown until built." After the course guide is built (`system/prompts/01_course_guide_prompt.md`),
> this gets updated with the actual validated ceiling and copied into `courses/registry.md`.

Unknown until the course guide is built.
