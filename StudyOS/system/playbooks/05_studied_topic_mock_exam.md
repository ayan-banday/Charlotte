# Playbook 05 — Integrated Mock Exam (Multiple Studied Topics)

> **Purpose:** simulate assessment conditions across MULTIPLE studied clusters/topics to test
> whether the student can deploy consolidated knowledge under time pressure. Sits between
> individual-cluster session tests (playbook 03) and real-assessment attempts (playbook 04
> convergence gate).
>
> **When to invoke:** after the student has completed cluster-level tests for a topic AND any
> synthesis cluster built for it (if one exists). Trigger phrase: **"give me a mock exam covering
> [topics I've studied]"** or **"create an exam covering everything I've studied so far."**
>
> **Owner:** the coach executes the pipeline end-to-end; the student supplies the topic list.

---

## 1. Confirm-understanding SOP (this workflow)

Reading this playbook confirms the workflow. When the student says "confirm you understand" —
reference this file, don't re-derive the workflow from scratch.

**The 6-step pipeline:**

1. **Topic scoping** — the student lists topics. Read each topic's `topic_guide.md` + latest
   `master_status.md` + any synthesis cluster's study sheet (off-sequence clusters use the
   `synthesis_` / `gap_` prefix, e.g. `synthesis_Governance_Master/` — name varies per course).
   Identify covered clusters + covered nodes + Priority-1 gap history.

2. **Exam design** — build an N-question mock (default: **3 questions**) at a mark weight
   appropriate to the course's real assessment (match the course guide's archetype distribution and
   format — MCQ, structured, essay, practical, whatever this course actually uses). Ensure **one
   question per major cluster** covered + **one synthesis/comparative question** spanning clusters.
   **No hints in the stems.**

3. **Timing suggestion** — scale to the real assessment's pacing (e.g. 3 questions × [the course's
   per-question time] + reading time). Offer a shorter mini-mock (2 questions) as an alternative.

4. **Session execution** — the student attempts it. They submit answers via a voice/recorded
   transcript (optional — filter obvious transcription artifacts like homophones or mis-heard words,
   but never filter out numerical, date, or conceptual errors) or written answers with C/U
   self-ratings. One question at a time or batch submission — both accepted.

5. **Grading + flagging** — for EACH question, apply this course's grading-focus rules (from the
   course guide / any locked feedback conventions the student has set):
   - Score at the top, using whatever scale this course's real assessment uses (marks, a letter/tier
     band, percentage — take it from the course guide, don't invent a new one).
   - Knowledge gaps surfaced.
   - The student's points expanded with concepts/evidence/examples appropriate to the course.
   - Model-answer logic, section by section, grounded in real terminology/sources/data for this
     course — not generic "good answer" filler.
   - If a voice transcript was used: ignore transcription noise, but still flag every numerical,
     date, or conceptual error as if it were typed.
   - **Assessment realism:** mirror how this course is actually graded (from the course guide),
     never a generic rubric.

6. **File updates (mandatory after every mock exam)**:
   - `courses/<Course>/<Topic_Name>/master_status.md` — APPEND a mock-exam results block: date +
     per-question scores + patterns.
   - `clusters/[NN_relevant_cluster]/cluster_NN_flags.md` — APPEND per-question Priority-1 flags with
     state (ACTIVE / FRAGILE / CLOSED).
   - Any topic-level "recurring errors / memorization reference" file, if the student keeps one —
     update with new patterns.
   - The synthesis/gap cluster's flags file (if one exists) — APPEND cross-cluster pattern findings.

**Never overwrite. Always append.** Playbooks 03/04 remain in effect for file protocols.

---

## 2. Rules already in effect (applied automatically)

Apply whatever feedback conventions the student has locked in for this course (grading focus, voice-
transcript handling, assessment-realism standard, format rules, question-count limits). If the
student hasn't set any, default to: concept-first feedback (no nitpicking surface errors), score
visible at the top of each grade, no hints in question stems, and directing the student to the study
sheet rather than re-teaching the whole cluster in chat.

---

## 3. Mock exam file structure

**Location:** `courses/<Course>/<Topic_Name>/tests/model_test_[N].md` (or `.html` if the student has
asked for a styled, print-like exam paper — self-contained, embedded CSS, no external assets. Either
format is fine; markdown is the default).

**Content template:**

```markdown
# Mock Exam — [Topic] — Model Test [N]

**Date generated:** YYYY-MM-DD
**Topics covered:** [list of clusters + syllabus nodes]
**Format:** [this course's real assessment format/paper style]
**Total marks / scale:** [whatever this course's real assessment uses]
**Suggested time:** [N] (scaled to real pacing + reading time)
**Style:** Adversarial, exam-standard, no hints in stems

---

## Instructions

- Answer in [the language/format this course expects]
- Voice-dictated transcript accepted (optional) or written answers with C/U self-rating
- One question at a time OR all at once — your choice
- Timed practice recommended for realistic simulation

## Coverage map

| Q | Type | Cluster tested | Core concepts required |
|---|---|---|---|
| 1 | [type] | [cluster 1] | [...] |
| 2 | [type] | [cluster 2] | [...] |
| 3 | [type] | [cluster 3 or synthesis] | [...] |

---

## Q1 ([marks], [type])

[Stem only. NO hints. NO trap descriptions.]

---

## Q2 ([marks], [type])

[Stem only.]

---

## Q3 ([marks], [type])

[Stem only.]

---

## Post-exam self-audit checklist (before submitting)

[Adapt per course — e.g. for an essay-based course: stance stated upfront, N+ points each with
reasoning, evidence anchors, named examples/cases, balance, cross-topic linkage, conclusion. For a
quantitative course: units checked, method stated, working shown, answer sanity-checked. Build the
checklist from this course's mark-scheme logic, not a generic template.]

Mark **C** ONLY if every item is met. Otherwise **U**.
```

---

## 4. Grading output template (for post-mock feedback)

Per-question feedback follows this structure:

```markdown
# Q[N] Feedback — Score: [XX/scale]

## What you did well
[Brief praise — 3–5 bullets]

## Part 1 — Knowledge gaps surfaced
[Concepts the student was reaching for; missing evidence/terminology/data]

## Part 2 — Your points expanded
[Take their exact points, show how to deepen each]

## Part 3 — Model-answer logic, section by section
[Model reasoning for each part of the answer, grounded in real course-specific terminology/evidence]

## Quick summary
[Score → target, 3–5 items to fix next time]
```

**Cumulative session summary (after all questions graded):**

```markdown
# Mock Exam [Topic] [N] — Overall Report

- Total: [XX/scale]
- Per-question breakdown
- Cross-question patterns (repeating strengths/gaps)
- Priority-1 gaps CLOSED this mock
- Priority-1 gaps REOPENED / NEW this mock
- Next-session priority: [top 3 drills]
```

---

## 5. Trigger phrases

Any of these invoke this playbook:

- "give me a mock exam covering [X, Y, Z]"
- "create an exam for everything I've studied"
- "generate a mock test covering [multiple topics]"
- "I'm ready for a comprehensive test on [topic]"
- "let me practice a full paper on [topic]"

---

## 6. Interaction with playbook 04 (convergence)

The mock exam is **NOT** the final convergence gate. Convergence still requires (playbook 04):
- ACTIVE gap count = 0
- FRAGILE gap count ≤ ~5
- Coverage complete (no UNTOUCHED nodes)
- **PLUS**, when a real past assessment exists, a timed attempt on it. If none exists, readiness is
  provisional — say so explicitly (playbook 04).

This mock (playbook 05) surfaces deployment gaps under time pressure across multiple topics. A real
past-assessment attempt (playbook 04) tests against the actual assessor's real distribution. Prefer
running both before declaring full readiness.

---

## 7. When to re-run

- After building any new cluster on an already-tested topic.
- Periodically during a long study run (e.g. every couple of weeks), if the student wants a
  standing cadence — set this by agreement with the student, not a fixed rule.
- As a final push readiness check as a deadline approaches, if one exists.
