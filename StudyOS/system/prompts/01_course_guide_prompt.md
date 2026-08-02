# Prompt 01 — Build the Course-Level Guide

**Layer 1. Run once per course.** This is the conversational entry point for building a
`course_guide.md`. It produces a complete model of how the assessment thinks across the whole
course. The deterministic mechanics (the 90% check, tagging, validation) live in
`playbooks/01_build_guides.md` — this prompt drives the flow and the research; the playbook governs
the rules.

> **Before you start:** research is **strongly recommended** — enable it if you can. If it's off, or
> the loaded materials are thin, **say so and state the confidence ceiling, then proceed anyway** —
> this is not a hard blocker. Check `courses/<Course>/context.md` for the course's context (its
> format, board/provider, and any rules the student has filled in) and confirm what inputs exist in
> `inputs/<Course>/`: past papers/assessments, official docs (syllabus + mark schemes/rubric), and
> model answers / marked work where a rubric is absent. The system must still work for a course with
> **no** official past papers at all — it just runs at a lower confidence ceiling, clearly flagged.

> **Project note (what's already decided — do NOT re-ask):** the course and its context come from
> `courses/<Course>/context.md` (the student fills this in once, and it holds whatever is specific to
> their course/assessment — no exam board is hardcoded here); the default gap-closure type comes from
> `courses/registry.md`. So skip generic exam/country collection and any "directional gate" domain
> classification — read the course's context and type from the registry, then proceed. Ask only which
> course to build.

---

## Step 1 — Confirm scope

Ask the student which **course** (e.g. "Organic Chemistry", "AWS Solutions Architect Associate",
"Conversational Spanish") to build, then confirm the context, inputs you can see, and the type from
the registry:

> "Building the **[Course]** guide. Type from the registry: **[type]**. Context I have:
> [summary from `courses/<Course>/context.md`, or 'none filled in yet']. Inputs I can see: [list].
> Missing: [list]. Is this correct before I research?"

If `context.md` is missing or empty, ask the student to state the essentials inline — what the
assessment is, its format, any board/provider or rules that govern it — or fill it in themselves.
The system can proceed on whatever is given, flagging the rest `[INFERRED]`.

If inputs are thin, **state the confidence ceiling you'll be able to reach** — do not proceed
silently. If a **gold-standard example guide** exists for another course, read it first and match its
depth, structure, and tone — it is the quality bar.

---

## Step 2 — Ingest inputs, then research (research recommended)

**Read the loaded inputs first.** Ingest everything in `inputs/<Course>/` (syllabus + official docs,
past papers/assessments, rubrics/mark schemes, model answers) — where these exist, this is the
primary ground truth and the content node map is built from it. **Then**, if research is enabled,
research to *supplement* what the inputs don't cover (grounding hierarchy: `spec.md` §13). Conduct an
exhaustive search, anchored to the **exact course and assessment**. Look for:
- Official past papers/assessments and question banks
- Official syllabus, learning objectives, instructor/examiner feedback
- Mark schemes/rubrics and model answers
- Assessor commentary on how questions are set
- Topic frequency data across multiple sittings/editions
- Recent syllabus or curriculum changes
- Common misconceptions and traps flagged in feedback or reports

**How to search well:** every query anchors three things — the exact course/assessment name, the
exact topic, and the specific resource you want. Never lead with generic terms ("study guide",
"revision notes").
- **Good:** `[Course] [Board/Provider] past paper mark scheme kinetics 2019 2022`
- **Bad:** `chemistry kinetics revision tips`

**Primary vs secondary:** weight **primary sources** (the official board/provider, official portals,
examiner/instructor reports) **10×** over secondary ones (revision sites, tutoring blogs, YouTube).
The test: *did a human who actually set or marked this assessment write it?* If only secondary
sources exist, **say so** in the confidence report. If **no** official sources exist at all
(self-directed or informal course, or research is off) — that's a valid mode, not a failure state:
build from general knowledge, tag it `[INFERRED]`, and state the ceiling plainly.

**Output a Research Confidence Report:**
> **What I found:** [exactly what, and from where]
> **What is missing:** [exactly what could not be found]
> **Confidence level:** HIGH / MEDIUM / LOW
> **Reason:** [one paragraph]

- **If LOW:** say so plainly — *"I don't have enough reliable material to build a fully grounded
  guide; a guide built on this could misdirect your study. If you have past papers, a syllabus, or
  marked work, share them — or I can build the guide from general knowledge with the ceiling clearly
  flagged. Proceed on that basis?"* Do not proceed until the student confirms.
- **If proceeding on LOW anyway:** stamp the guide with the LOW-confidence warning (`spec.md` §5).

Do not move to Step 3 until the student confirms the research report (or confirms proceeding without
research/with thin inputs).

---

## Step 3 — Build the guide

Build `courses/<Course>/course_guide.md` from `templates/course_guide.template.md`. This is **not** a
course summary — it's a model of how the assessment thinks, thorough enough that someone could set a
full paper from it. Cover:

1. **Assessment overview** — format, question types, timing, marking; higher- vs lower-order split;
   Bloom levels tested; what the assessment consistently rewards vs punishes.
2. **Topic frequency map** — every major topic with frequency, Bloom level, assessment weight.
3. **Dominant question archetypes** — for each: what it looks like, how often it appears, the
   specific trap construction this assessment uses, and what a correct vs incorrect approach looks
   like. Archetypes come from **what the research/inputs reveal**, not a pre-set list.
4. **How distractors are built** — the misconceptions wrong options target; the most common trap;
   what half-knowing students reliably get wrong and why.
5. **High-yield topics** (top 5–7) — why each is high-yield, what aspects are tested, the usual
   angle, and the most common wrong answer.
6. **Topics likely to matter next** — overdue by frequency, recently updated in the syllabus, or
   flagged in recent feedback/reports.
7. **Assessor priorities** — a direct, unhedged briefing of what this assessment values.

**Tag every claim** `[SOURCED]` / `[INFERRED]` (`spec.md` §5). Then **run the 90% confidence check**
per `playbooks/01_build_guides.md` (5 dimensions, hold-out questions, fix-and-re-test failing
dimensions only).

---

## Step 4 — Close out

Update the matching row in `courses/registry.md` (status → BUILT, validation source, confidence
ceiling). Then tell the student:

> "Your **[Course]** Guide is ready and saved. You don't need to run this again for this course. **If
> a real past assessment or official mock exists, take one within your first week of studying.** If
> your session performance is >70% but that assessment is <50%, come back and we'll recalibrate — the
> guide is a hypothesis; a real assessment is ground truth. If no official assessment exists for this
> course, your first serious self-test is the ground truth instead."
