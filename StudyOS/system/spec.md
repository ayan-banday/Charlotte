# Study Backcasting System — Specification

**The single source of truth for the system's logic.** Every concept is defined here exactly once.
`SYSTEM.md` is the always-loaded operational summary (laws + map + checklists); the prompts and
playbooks operationalize this spec; the templates shape its outputs. **If anything disagrees with
this file, this file wins** — flag the conflict.

This file merges and supersedes the former `architecture.md` and `rules_and_logic.md`.

> **Build decisions baked in:** Directories only — **no Obsidian tags** of any kind. Voice/recorded
> transcripts are **session-only inputs**, never saved to disk. A course's specific assessment
> context (institution, board, format, self-set goal — whatever applies) lives in that course's own
> `context.md`, filled in once; the engine itself never hardcodes an exam board or institution. A
> course lives directly at `courses/<Course>/` — there is no level/track folder split. Level or
> track may exist at most as an optional free-text front-matter field.

---

## 1. System architecture (the two-level flow)

The system has two levels. It runs in sequence — it does **not** become a loop until the topic
level starts.

**Level 1 — Course Setup (run once per course)**
- **Input:** raw course materials (past assessments/papers, syllabus, rubric/mark scheme, model
  answers) — **all optional.** A course can start from just a name and a `context.md`.
- **Process:** build a validated hypothesis of how the assessment *thinks* across all topics.
- **Output:** the `course_guide.md` (never deleted; updated only on recalibration).
- **Exit condition:** confidence ≥90% across the 5 dimensions (§5), **or** a LOW-confidence warning
  tag is applied explicitly.
- **Procedure:** `playbooks/01_build_guides.md`. Entry prompt: `prompts/01_course_guide_prompt.md`.

**Level 2 — Topic Sessions (run repeatedly until convergence)**
- **Input:** the student names a topic to study.
- **Process:** build the topic guide → propose clusters → generate questions → process the
  submission → track gaps → check convergence.
- **Output:** updated `master_status.md`, `flags.md`, concept docs, `[Topic]_gaps.md`, next questions.
- **Exit condition:** all three convergence conditions met (§9) **and** validated against a real
  past assessment where one exists.
- **Procedures:** `playbooks/01`–`04`. Entry prompt: `prompts/02_topic_session_prompt.md`.

---

## 2. Course types & gap closure

Every course has a **default type**, declared once in `courses/registry.md` and **read before every
session**. The type controls *how a gap is closed*. A topic may **override** the course default in
its own `topic_guide.md` front matter (read the default first, then the override — the override
wins for that topic only).

**`quantitative`** — Maths, Physics/Chemistry calculations, engineering, data-handling.
- **Gap closure:** concept doc **+ 3–5 variant questions solved until mechanical.**
- **"Mechanical" means:** the student solves 5 variants of the same type with zero hesitation,
  correct method every time, no miscalculation.
- **Non-negotiable:** reading never closes a quantitative gap. Variants must be *solved*.

**`qualitative`** — Biology essays, History, humanities, literature, organic mechanisms,
explanation-style topics.
- **Gap closure:** concept doc **+ re-test at a new angle.**
- **"New angle" means:** different question stem (same concept), or same stem with a different
  example/case.
- **Key hardness:** the concept doc must **name the misconception explicitly**, not just restate the
  correct knowledge.

**`applied`** — source-based questions, case studies, professional/practical scenarios.
- **Gap closure:** concept doc **+ a full worked example** under realistic/timed conditions.
- **"Full worked example" means:** the student sees the doc, then immediately practices the exact
  question type (same sources, same framework, same time constraint), and the example shows the
  **whole reasoning chain and how to spot the trap** — not just the final answer.

**Close conditions by type** (see the state machine in §3 for the full matrix):

| Type | New angle = | Closes when |
|---|---|---|
| `quantitative` | different numbers / application context, same method | confident + correct across variants, twice |
| `qualitative` | different stem or example, same concept | confident + correct, second session |
| `applied` | different source / scenario, same skill & framework | confident + correct on the next real question |

---

## 3. Gap state machine

Every gap lives in exactly one state, stored per topic in `master_status.md`.

**ACTIVE** — the gap is open.
- **Triggered by:** a wrong answer, **or** a correct answer with hesitation.
- **Priority sub-classification:**
  - **Priority 1 — confident + wrong.** The most dangerous case. Always listed first in the next
    session and in the gap roll-up.
  - **Priority 2 — repeatedly ACTIVE** (appeared in 2+ sessions without improving).
  - **Priority 3 — standard ACTIVE** (wrong/unattempted, first occurrence).
- **Actions:** every ACTIVE gap gets a concept doc (+ variants if quantitative, + worked example if
  applied). The gap **must** appear in the next session.

**FRAGILE** — the student knows it, but not deeply or consistently.
- **Triggered by:** a correct answer with hesitation, **or** a correct guess (anything in the delta
  zone — see §4).
- **Actions:** one question at a **new angle** next session. No concept doc needed (already
  understood; just needs confirmation).

**CLOSED** — mastery demonstrated.
- **Triggered by:** FRAGILE → correct + confident (second occurrence).
- **Actions:** never appears in questions again. Stays in `master_status.md` for history.
- **Immutable** unless the student explicitly reopens it (extremely rare).

**Transition matrix (apply exactly):**
```
ACTIVE  + correct + confident       → FRAGILE
ACTIVE  + correct + hesitation      → stay ACTIVE   (regenerate the concept doc, don't just re-test)
ACTIVE  + wrong                     → stay ACTIVE
FRAGILE + correct + confident (2nd) → CLOSED
FRAGILE + correct + hesitation      → stay FRAGILE
FRAGILE + wrong                     → ACTIVE         (drops back down)
CLOSED  + anything                  → CLOSED         (immutable unless explicitly reopened)
```

---

## 4. Confidence detection & the delta zone

Confidence drives every state transition, so this must be right. **Transcript > self-rating.**

**Source 1 — Voice/recorded transcript (primary).**
The student pastes raw transcript text into the session. Scan each answer for **hesitation signals**:
- **Verbal:** "I think", "I guess", "not sure", "I'm flagging this", "maybe", "I don't know", "hmm",
  "probably", "could be".
- **Process:** answer restart, self-correction mid-answer, long pause before answering, talking
  themselves into/out of an option.

**Decision rule:** if *any* hesitation signal appears anywhere in that answer → **hesitant**. No
hesitation **and** correct → **confident**. **Confident + wrong → Priority 1.**

> **Bias conservative.** A false "hesitant" costs one extra re-test. A false "confident" lets a gap
> hide. **When in doubt, flag hesitant.** False negatives (missing hesitation) are worse than false
> positives.

Transcripts are **session-only** — process them, never save them to disk.

**Source 2 — Student self-rating (fallback, for written answers).**
The student tags each answer **`C`** (confident) or **`U`** (uncertain). Less depth than a
transcript, but enough to run.

| Result | State |
|---|---|
| Correct + C | FRAGILE (one confident confirmation still needed before CLOSED) |
| Correct + U | FRAGILE |
| Wrong + C | ACTIVE, **Priority 1** |
| Wrong + U | ACTIVE, Priority 2 |

**The delta zone.** After grading, compute two scores:
- **Raw score** = all correct answers (including lucky guesses).
- **Confident score** = correct answers that were confident (C / no hesitation).

The gap between them is the **delta zone**. Any answer in it (correct but not confident)
**defaults to FRAGILE even though it was technically right.** This is the core anti-bullshit rule:
**guessing right is not mastery.** Always report the delta to the student.

---

## 5. The 90% confidence check (guide validation)

Both the course guide and each topic guide must pass this check before being relied on.

**The test.** Hold out **5–10 past-assessment/past-paper questions** the guide was *not* calibrated
on. For each, predict all five dimensions **before** looking at the answer, then check against the
real rubric / mark scheme / model answer and count hits:
1. Assessment format and structure
2. Mark scheme / rubric (what is rewarded per band)
3. Topic content node (what knowledge is tested)
4. Question type and method
5. Trap model (which misconception the distractor targets)

**Thresholds — all five must pass.**

| Dimension | Threshold | A failure means |
|---|---|---|
| Assessment format & structure | ≥95% | the guide misunderstands the question type or paper layout |
| Mark scheme / rubric (reward per band) | ≥90% | the guide's marking-logic prediction is wrong |
| Topic content nodes | ≥90% | held-out questions don't map to the guide's nodes |
| Question type & method | ≥85% | the guide misclassifies the question before seeing the answer |
| Trap model | ≥85% | the guide doesn't predict the misconception correctly |

**If a dimension fails:** find the weak section of the guide, fix it, and **re-test only that
dimension** — not the whole guide.

**Confidence ceilings (`[SOURCED]` vs `[INFERRED]`).** Tag every claim in a guide:
- `[SOURCED]` — grounded in the student's own loaded materials, **or** an authoritative external
  source found via research (official syllabus, standard textbook, certification body, real past
  assessments, instructor rubric/feedback).
- `[INFERRED]` — from general knowledge, reasoning, or a secondary source not directly traceable to
  the course's own materials or an authoritative source.

When no official rubric/mark scheme is available, use model answers + instructor-marked work as a
proxy, tag the claims `[INFERRED]`, and state a ceiling (e.g. 85–88% instead of 90%). This is
acceptable — **never fake confidence.**

**Very low confidence (<70% overall):** stamp the guide explicitly —
`WARNING: Built with LOW confidence. Ground truth will be your first real assessment or full-scope
model test. Recalibrate if performance mismatch occurs.`

---

## 6. Clustering logic

A topic is broken into **named clusters** — real content names (`Dimensional_Analysis`), **never**
`Cluster_1`.

**Count by breadth:** narrow topic → **3–4**, medium → **4–6**, wide → **5–7**. Clusters must be
**collectively exhaustive** — together they cover every node in the topic guide.

**Generation sequence:**
- **Propose the full breakdown** (all cluster names + one-line descriptions) and **get the student's
  approval before generating Cluster 1.**
- Then generate clusters **one at a time, on request** ("generate the next cluster"). **Never
  auto-generate all clusters.** Respect the student's pace.
- A cluster may be regenerated later (e.g. when flags show it's weak) but **never deleted**.

**Cluster study sheet** — an *exam-preparation artifact, not a textbook summary*. Must contain:
- **Core knowledge** — exactly what's needed to answer any assessment question on this cluster (no
  more).
- **Key facts / formulas / rules** — at the level the assessment expects.
- **Connections** — how this cluster links to the other clusters and the wider course.
- **Assessment angle** — how this cluster is *typically tested* (from the topic guide).
- **Common misconceptions** — the traps from the trap model that apply here.

**Pre-study sheet** — generated after clusters exist, or on request. **Big-picture only, light:**
what the topic is fundamentally about, how the clusters connect, the single most important concept.
**Skip it if the student has done their own pre-study.**

---

## 7. Question generation rules

Questions are adversarial — they exist to **find gaps**, not to make the student feel good.

**Mirror the archetype distribution exactly.** If the topic guide says "60% type A / 25% type B /
15% type C," the set matches that. **Do not invent a new distribution.**

**Gap-driven selection** (for re-test sets — read from `master_status.md`, apply in order):
1. **ACTIVE topics always appear; Priority 1 (confident-wrong) gets the first question.**
2. **FRAGILE topics get one question at a new angle** (by type — §2). Not the framing that caught it.
3. **CLOSED topics never appear** unless the student explicitly asks.
4. **Remaining slots → untouched nodes** from the guide's content node map (for coverage).

**Question properties:**
- **Trap:** every question embeds a **real trap** from the trap model — a distractor must encode an
  actual misconception, not a random wrong value. **No trap → too easy → regenerate.**
- **Difficulty:** Bloom **Application or higher.** No pure recall.
- **Format:** for MCQ courses, 4 options (1 correct + 3 plausible distractors from the same
  cluster). For essay/structured courses, match the real question format from the guide —
  MCQ is not required.
- **Freshness:** never reuse an angle from a previous session — different scenario, numbers, framing.
- **Visual topics:** if recognition is tested (histology, diagrams, etc.), give a **blank
  image-search link to open *before* reading the options**; describe the image only after the
  student answers. The search query uses descriptors only — never the answer term.

**Count:** standard cluster **≥10 questions**; high-yield node (flagged in the guide) **15–20**;
cross-cluster mock — size **suggested** by the ACTIVE + FRAGILE count (not fixed), and reported.

**Feedback after submission** — per question, provide:
1. **Correct answer** + one-line reason.
2. **Why each distractor is wrong** — one line each, **naming the misconception** it targets.
3. **Key differentiator** — the single fact separating the correct answer from the best wrong one.
4. **Assessment tip** — how this type shows up in the real assessment and what the trap usually is.

---

## 8. Session processing & gap tracking

After the student submits (answers + transcript or C/U), run these **7 steps in order, every
session** (→ `playbooks/03_run_session.md`).

1. **Grade & assign state.** Mark each answer correct / partial / wrong. Determine confidence (§4).
   Map through the state matrix (§3) to assign ACTIVE/FRAGILE/CLOSED + priority.
2. **Two scores + delta.** Report raw score, confident score, and the delta (§4). Every
   correct-but-unconfident answer defaults to FRAGILE.
3. **Concept docs (all ACTIVE + FRAGILE).** Per gap: **Rule** (1–2 sentences) · **Why you get it
   wrong** (name the exact misconception) · **Method/fact** (bulleted, key terms bold) · **Worked
   example** (the actual question that created the gap) · **Assessment trap**. End the doc with a
   **Quick Recall** section (one line per gap). Quantitative gaps add **3–5 variants**; applied gaps
   add a **full worked example + a new same-type question** under realistic conditions.
4. **Append `flags.md`** (per affected cluster). **Append, never overwrite.** Name the
   **misconception** specifically, plus the exact scenario to test next.
5. **Append `master_status.md`** (topic-level). **Append, never overwrite.** Add this session's
   per-gap lines and recompute the **Summary** (ACTIVE count, FRAGILE count, suggested next size).
6. **Regenerate `[Topic]_gaps.md`.** Roll up all current ACTIVE + FRAGILE gaps across every cluster,
   **Priority 1 first** → `gaps/<Course>/[Topic]_gaps.md`. (History is preserved in
   `master_status.md`; this roll-up may be fully rewritten.)
7. **Build the next question set** (§7): ACTIVE present (P1 first), FRAGILE one new angle each,
   CLOSED excluded, remaining slots = untouched nodes.

---

## 9. Convergence & final validation

The loop ends only when **all three are true at once**:
1. **ACTIVE count = 0** in the `master_status.md` summary.
2. **FRAGILE count is small** — handleable in one revision pass (typically **≤5**), not another full
   mock.
3. **Coverage is complete** — every node in the topic guide's content node map is SOLID, FRAGILE, or
   has been tested. **No UNTOUCHED nodes remain.** (This is the check people skip — walk the node map
   explicitly.)

**The loop does NOT stop because scores are high.** Sessions are adversarially designed; high scores
on gap-finding sessions are not a readiness signal.

**Final validation sequence (only after the three conditions pass):**
1. **Model test** — a full set covering the **entire topic** under realistic/timed conditions →
   `[Topic]/tests/model_test_[N].md`. Always run this one.
2. **Real past assessment** — **IF one exists** for this course (a genuine past paper, past exam,
   prior certification test, or equivalent) → under **timed/realistic conditions** →
   `[Topic]/tests/official_[year].md`. If no real past assessment exists, skip this step and say so
   explicitly.
3. **Interpret:**
   - Real assessment available, both consistently high → **topic is mastery-ready.**
   - Real assessment available, model >70% **but** real assessment <50% → the **guide is
     misaligned with the real assessment.** Do not declare ready — recalibrate (§5, and
     `playbooks/01`).
   - **No real assessment exists:** a strong model test may support cautious readiness, but it must
     be **explicitly flagged as NOT yet verified against a real assessment.** Never silently declare
     "ready" or "verified" from a model test alone.

Where a real past assessment exists, it is the honesty check and the final gate — **a model test
alone never converges a topic** in that case. Where none exists, the model test is the best
available signal, but the "not yet verified" flag must stay attached to the topic's status until a
real assessment (or an equivalent external, graded evaluation) becomes available.

---

## 10. Course-type sub-loops & edge cases

**Quantitative gap closure** (the most complex):
1. Concept doc generated for the ACTIVE gap.
2. Student reads it (now oriented).
3. Generate **3–5 variants** (same type, different numbers/context).
4. Student solves all variants.
5. Gap → FRAGILE only if variants are solved with **zero hesitation**.
6. Gap → CLOSED only if confirmed confident again next session.

**Applied gap closure** (requires context):
1. Concept doc generated, including a **full worked example**.
2. Student reads the doc + works the example.
3. Generate a **new question of the same type** (different source, same skills).
4. Student solves it under realistic time constraints if applicable.
5. Gap → FRAGILE if solved with understanding of the reasoning chain; → CLOSED if reconfirmed next
   session.

The worked example must show the **full reasoning chain**, not just the final answer.

**Regenerate vs. generate new:** *regenerate* a cluster study sheet when flags show it needs
updating; *always generate new questions* — never reuse questions across sessions.

---

## 11. Scaling & multi-topic management

- **One course guide** per course (built once; rebuilt only on recalibration). Unlimited topics
  within it.
- **3–7 clusters** per topic by breadth. One `master_status.md` per topic (cumulative across
  clusters); one `flags.md` per cluster (surgical, session-level); one `[Topic]_gaps.md` per topic
  (aggregate, cross-cluster). `master_status.md` is **always topic-scoped, never course-scoped.**
- **Course-level summary** — on request only. Aggregate all topic `master_status.md` files into
  total ACTIVE / total FRAGILE / which topics are converged vs in-progress. **Not maintained
  automatically.**

---

## 12. Directory structure, file operations & I/O

**Directory map** (course-based layout — no level/track folder split):
```
courses/registry.md                      ← each course's default gap-closure type

inputs/<Course>/<Topic>/                 ← raw materials for this topic (optional)
    past_papers/  official_docs/  chapter_notes/  model_answers/  other_resources/

courses/<Course>/
    context.md                           ← this course's assessment context, filled in once
    course_guide.md                      ← built once; updated only on recalibration
    <Topic_Name>/
        topic_guide.md                   ← topic guide, built once per topic
        pre_study_sheet.md
        master_status.md                 ← APPEND-ONLY
        clusters/[NN_Cluster_Name]/            ← NN = zero-padded study-order number; off-sequence clusters use `gap_` or `synthesis_` prefix instead
            cluster_[NN]_study_sheet.md        ← may be regenerated, never deleted
            cluster_[NN]_flags.md              ← APPEND-ONLY
        tests/
            model_test_[N].md   official_[year].md

gaps/<Course>/<Topic_Name>_gaps.md       ← regenerated roll-up (history lives in master_status)
```

**Naming:** underscores, no spaces. Topic names are real content names (`Dimensional_Analysis`).
Cluster folders keep the content name but must be **prefixed by their study-order number** so a
"cluster 3" ask is directly resolvable: `03_Differential_Equations/`, not `Differential_Equations/`
and not `Cluster_3/`. Zero-pad to two digits. Parallel gap-closers at the same slot use a letter
suffix (`04b_...`). Off-sequence clusters (synthesis, gap, mastery, tactical, discipline layers
with no fixed study-order position) use a `gap_` or `synthesis_` prefix instead of a number
(`gap_TNT_Verbatim/`, `synthesis_Governance_Master/`). Inner files mirror the prefix:
`cluster_03_study_sheet.md`, `cluster_03_flags.md`, or `cluster_gap_...` / `cluster_synthesis_...`
for off-sequence. Tests named by type and year (`model_test_1.md`, `official_2023.md`).

**Append-only files** — never overwritten, to preserve history:
- `master_status.md` — session results appended at the bottom; summary recomputed each session.
- `flags.md` — new flags appended at the bottom.
- `[Topic]_gaps.md` is the exception — a regenerated roll-up (full gap history is preserved in the
  per-session `master_status.md` entries).

**Inputs to the system:** raw course materials (optional); the student's topic choice; the
student's answers (written or transcript); the C/U self-rating (if written); a voice/recorded
transcript (if available).

**Outputs:** course guide, topic guide, pre-study sheets, question sets, concept docs, updated gap
tracking (`master_status.md`, `flags.md`, `[Topic]_gaps.md`), and the next session's questions.

**What the system does NOT do:** predict scores (it shows readiness gaps only); store voice/recorded
transcripts; auto-start sessions; over-generate clusters.

**Recalibration trigger (the one critical checkpoint):** the guide is ground truth **until proven
wrong** — specifically when session/model performance is **>70%** but a **real past assessment
scores <50%** (where a real past assessment exists for this course). That gap means the guide is
misaligned. Find the dimension that mispredicted and fix it (§5).

---

## 13. Grounding — every artifact traces to a real source

Everything the system generates — course guide, topic guide, clusters, study sheets, questions,
concept docs — must be **grounded in real source material**. Nothing is invented from general
knowledge and presented as fact. This is the principle behind the input-ingestion steps in
`playbooks/01`–`02` and the "research supplements inputs" ordering in the prompts.

**Inputs are optional.** A course can run with thin or no materials — in that case the system
**says so explicitly**, states the confidence ceiling (§5), and still runs: it leans on research and
general knowledge tagged `[INFERRED]`. Thin inputs are a disclosed ceiling, never a blocker.

**Source-priority hierarchy (highest first):**
1. **Loaded inputs** — the materials in `inputs/<Course>/` and, for a topic,
   `inputs/<Course>/<Topic>/` (past papers/assessments, official syllabus/docs, rubric/mark scheme,
   chapter notes, model answers, other course resources). This is the **primary ground truth** when
   present — the student's own materials and the actual assessment they will sit. **Read it first.**
2. **Authoritative external sources** found via research — the supplement when inputs are thin or
   missing (official syllabus, a standard textbook, the certification body, real past assessments,
   an instructor's rubric/feedback). Tag derived claims `[SOURCED]`.
3. **General knowledge / secondary sources** — last resort, only to fill a genuine gap the two above
   don't cover. Tag `[INFERRED]` and state the confidence ceiling.

**Rules:**
- **Read the relevant inputs before researching.** Ingest the input folder first; use research to
  *fill gaps the inputs don't cover*, never to replace materials the student already provided.
- **The content node map is derived from the actual syllabus + notes in the inputs** when available,
  then cross-checked against past assessments — not reconstructed from memory. Where inputs are
  thin or absent, the node map may lean on `[SOURCED]`/`[INFERRED]` research instead — flagged as
  such.
- **Clusters and study sheets are built from the loaded notes / source material**, and the breakdown
  is validated for collective exhaustiveness against the course scope present in the inputs (§6) —
  not just against the topic guide's node map.
- **Questions are grounded in the trap model + real past assessments** where available in the
  inputs — real traps, not invented distractors (§7). Where no past assessments exist, traps are
  drawn from `[SOURCED]`/`[INFERRED]` knowledge of the assessment's known format, stated explicitly
  as such.
- **Traceability:** any non-trivial claim must be attributable to a source — a specific input file or
  a cited authoritative source. If it cannot be traced, tag it `[INFERRED]` and flag it. **Never
  present ungrounded content as established fact.**
- **If a topic's inputs are missing or thin, say so and state the confidence ceiling** (§5) — do not
  silently substitute general knowledge.
