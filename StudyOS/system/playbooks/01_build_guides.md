# Playbook 01 — Build the Guides (Course & Topic)

**Goal:** produce the two validated guides everything else depends on — the **course guide**
(`courses/<Course>/course_guide.md`, built once per course) and each **topic guide**
(`courses/<Course>/<Topic_Name>/topic_guide.md`, built once per topic). Both are validated by the
same **90% check**. The conversational flow is in `prompts/01_course_guide_prompt.md` (course) and
`prompts/02_topic_session_prompt.md` Step 4 (topic).

> Definitions live in `spec.md`: §1 (the two levels), §2 (types), §5 (90% check), §7 (archetype
> distribution). This playbook is the procedure; `spec.md` wins on any conflict.

---

## Preconditions

- **Inputs are optional.** If `inputs/<Course>/` has past assessments, official docs
  (syllabus/curriculum + rubric or mark scheme), and model answers / marked work, use them as the
  primary ground truth (`spec.md` §13). If it's thin or empty, **say so and state the confidence
  ceiling** — do not proceed silently, but do proceed. The course's **type** is known from
  `courses/registry.md`. If a **gold-standard example guide** exists for another course, read it
  first — it's a quality bar for depth and structure, not content to copy.
- **Topic guide:** the course guide already exists. The topic guide inherits the course's assessment
  structure, mark logic, and trap model, then specialises them — but it is **grounded first in the
  topic's own loaded inputs** (`inputs/<Course>/<Topic>/`: notes, model answers, topic-filtered past
  assessments, other resources) plus the syllabus/curriculum scope for the topic, when those exist.
  Only after ingesting what's available do you use targeted research to fill **genuine gaps**,
  anchored to what this assessment actually tests. (Grounding hierarchy: `spec.md` §13.)

If inputs are missing or thin, **say so and state the confidence ceiling** — never proceed silently,
and never treat "no inputs" as a reason to stop.

---

## A. Course guide

1. **Ingest everything** available in `inputs/<Course>/`. Read the syllabus/curriculum (if present)
   to enumerate the full **content node map** (every node the assessment can test). Read whatever
   past assessments exist to see how the assessment is actually structured. If none exist, build the
   node map from the course's stated learning objectives / research, and flag it `[INFERRED]`.
2. **Build the guide** (template: `templates/course_guide.template.md`) covering, across all topics:
   assessment structure & format · mark scheme logic (reward per band) · content node map · question
   archetypes + **numerical distribution** (mirrored later in generation) · **trap model** (the most
   valuable section — misconceptions the assessment exploits) · the assessor's mental model.
3. **Tag every claim** `[SOURCED]` / `[INFERRED]` (`spec.md` §5). Never blur the two.
4. **Run the 90% check** (below).
5. **Write the file** and update the matching row in `courses/registry.md` (status → BUILT,
   validation source, confidence ceiling).

## B. Topic guide

1. **Create the topic folder** `courses/<Course>/<Topic_Name>/` (underscores, real content name).
1a. **Ingest the topic's inputs first**, if any. Read everything in `inputs/<Course>/<Topic>/`
   (notes, model answers, topic past assessments, other resources) and the syllabus/curriculum
   section for this topic. The **content node map (step 3) is derived from these actual materials**
   when they exist, then cross-checked against the topic's past assessments — not reconstructed from
   memory or the course guide alone. Use research to fill gaps the inputs don't cover, or to build the
   node map from scratch if there are no inputs at all (`spec.md` §13). If the topic's inputs are
   thin or absent, say so and state the ceiling.
2. **Set the topic type.** Default = the course's type from `courses/registry.md`. If this topic
   genuinely closes gaps differently, declare the override in the guide's front matter, e.g.
   `type: qualitative  # override of course default 'quantitative' — reasoning-based, not calculation`.
3. **Write the guide** (template: `templates/topic_guide.template.md`), specific to this topic:
   **content node map** (becomes the coverage checklist for convergence) · **archetypes +
   distribution stated numerically** (mirrored exactly in generation) · mark-scheme logic for this
   topic · **trap model** for this topic (drive distractors from these) · **high-yield flags** (get
   15–20 questions per cluster instead of 10).
4. **Tag claims** `[SOURCED]` / `[INFERRED]`.
5. **Run the 90% check** (below) on held-out topic questions.

---

## The 90% confidence check (both guides)

Hold out **5–10 past-assessment questions** the guide was *not* calibrated on. For each, predict all
five dimensions **before** looking at the answer, then check the real mark scheme / model answer and
count hits. The **five dimensions and their thresholds** are defined in **`spec.md` §5** (format
≥95%; mark scheme ≥90%; content nodes ≥90%; question type ≥85%; trap model ≥85%).

- **All five must pass.** If one fails, find the weak section, fix it, and **re-test only that
  dimension.**
- **No official rubric or mark scheme available?** Use model answers / marked work as proxy, tag
  `[INFERRED]`, state a ceiling (e.g. 85–88%). Acceptable — never fake confidence.
- **No past-assessment questions exist at all to hold out?** The check can't run in its normal form.
  Skip it, stamp the guide `WARNING: No held-out validation possible — built on research/inputs
  alone. Ground truth will be your first real assessment attempt. Recalibrate on first mismatch.`
  Treat this the same as an overall <70% result below.
- **Overall <70%?** Stamp the guide: `WARNING: Built with LOW confidence. Ground truth will be your
  first full-scope model test or real assessment attempt. Recalibrate if performance mismatch
  occurs.`

---

## Recalibration (later, not at build time)

Recalibrate a guide **only** when reality contradicts it: session/model performance **>70%** but a
**real past-assessment attempt <50%** (`spec.md` §9, §12). This trigger only applies once a real
past assessment has actually been attempted — see playbook `04`. Find the dimension that mispredicted
and fix it.

## Done when

The guide exists, all five dimensions pass (or a ceiling/warning is explicitly stated), every claim
is `[SOURCED]`/`[INFERRED]` tagged, the archetype distribution is numeric, and (course)
`courses/registry.md` is updated / (topic) the content node map is complete enough to serve as the
coverage checklist. Then → **playbook 02** (clusters).
