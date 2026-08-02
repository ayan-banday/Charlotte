# Playbook 03 — Run a Session (Generate → Grade → Track → Next)

**Goal:** the full per-session loop — build an adversarial question set, grade the submission, detect
confidence, update gap state, and build the next set. This merges the old "generate questions",
"process session", and "confidence detection" steps into one continuous procedure.

> Definitions: `spec.md` §3 (state machine), §4 (confidence), §7 (question rules), §8 (the 7-step
> sequence). Templates: `concept_doc`, `flags`, `master_status`, `topic_gaps`. This playbook is the
> procedure; `spec.md` wins on any conflict.

---

## Part 1 — Generate the question set

**Mandatory context, every time:** the topic `topic_guide.md` (its archetype distribution + trap
model drive the set), the cluster `cluster_NN_study_sheet.md`, and the topic `master_status.md`
(which gaps must reappear).

**Build rules (apply in order):**
1. **Mirror the archetype distribution exactly** — do not invent a new mix.
2. **Gap-driven selection** (from `master_status.md`): ACTIVE always appear, **Priority 1
   (confident-wrong) gets the first question**; FRAGILE get one question at a **new angle** (by type
   — see the table below); CLOSED never appear unless the student asks; remaining slots → **untouched
   nodes** for coverage.
3. **Every question embeds a real trap** from the trap model. **No trap → too easy → regenerate.**
4. **Difficulty:** Bloom **Application or higher.** No recall.
5. **Format:** 4-option MCQ where the course uses MCQ (1 correct + 3 plausible distractors from the
   same cluster); otherwise the real essay/structured/practical format for this course.
6. **Freshness:** never reuse an angle from a previous session.
7. **Visual subjects:** give a blank image-search link to open **before** the options; describe the
   image only after the student answers (descriptors only — never the answer term).

**Count:** standard cluster **≥10**; high-yield node **15–20**; cross-cluster mock — size
**suggested** by ACTIVE + FRAGILE count (report the suggestion).

---

## Part 2 — Detect confidence (do this while grading)

**Transcript > self-rating.**

**Source 1 — voice/recorded transcript (primary, optional).** If the student pastes a raw
voice/recorded transcript, scan each answer for hesitation signals:
- **Verbal:** "I think", "I guess", "not sure", "I'm flagging this", "maybe", "I don't know", "hmm",
  "probably", "could be".
- **Process:** answer restart, self-correction mid-answer, long pause, talking themselves in/out.

**Rule:** *any* signal → **hesitant**. None + correct → **confident**. **Confident + wrong →
Priority 1.** **When in doubt, flag hesitant.** Transcripts are session-only — never saved to disk.

**Source 2 — self-rating (fallback, or default for written answers).** Student tags each answer
`C`/`U`:

| Result | State |
|---|---|
| Correct + C | FRAGILE |
| Correct + U | FRAGILE |
| Wrong + C | ACTIVE, **Priority 1** |
| Wrong + U | ACTIVE, Priority 2 |

**New angle by type** (for FRAGILE re-tests):

| Type | New angle = |
|---|---|
| `quantitative` | different numerical setup / context, same method |
| `qualitative` | different stem or example, same concept |
| `applied` | different source or scenario, same skill & framework |

---

## Part 3 — Process the submission (7 steps, in order)

1. **Grade & assign state.** Correct / partial / wrong × confidence → map through the state matrix
   (`spec.md` §3) to ACTIVE/FRAGILE/CLOSED + priority. (Priorities: P1 confident+wrong, P2
   repeatedly-ACTIVE, P3 standard.)
2. **Two scores + delta.** Raw (all correct) vs confident (correct + confident). Report the delta;
   every correct-but-unconfident answer **defaults to FRAGILE** — guessing right is not mastery.
3. **Concept docs (all ACTIVE + FRAGILE)** — copy `concept_doc.template.md`. Per gap: **Rule** ·
   **Why you get it wrong** (name the exact misconception) · **Method/fact** (bulleted, key terms
   bold) · **Worked example** (the actual question that created the gap) · **Assessment trap**. End
   with a **Quick Recall** section. Quantitative gaps add **3–5 variants** (gap can't reach FRAGILE
   until variants are solved with zero hesitation); applied gaps add a **full worked example + new
   same-type question** under realistic conditions.
4. **Append `cluster_NN_flags.md`** (per affected cluster). **Append, never overwrite.** Name the
   **misconception**, the exact scenario to test next, the rule, the state at flag time.
5. **Append `master_status.md`** (topic-level). **Append, never overwrite.** Add this session's
   per-gap lines; recompute the **Summary** (ACTIVE count, FRAGILE count, suggested next size).
   CLOSED gaps stay but stop appearing in mocks.
6. **Regenerate `[Topic]_gaps.md`** — roll up all current ACTIVE + FRAGILE across clusters, **P1
   first** → `gaps/<Course>/<Topic_Name>_gaps.md` (may be fully rewritten; history lives in
   `master_status.md`).
7. **Build the next set** — return to Part 1: ACTIVE present (P1 first), FRAGILE one new angle each,
   CLOSED excluded, remaining = untouched nodes.

**Feedback per question** (give after the student submits): correct answer + one-line reason · why
each distractor is wrong (naming the misconception) · the key differentiator · the assessment tip.

---

## Done when

The set matched the archetype distribution and every question had a real trap and fresh angle; all 7
processing steps ran; append-only files were **appended** (verify you didn't overwrite); and the
next set is ready. Then check **playbook 04** (convergence).
