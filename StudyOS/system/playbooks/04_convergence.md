# Playbook 04 — Convergence & Final Validation

**Goal:** decide whether a topic is exam-ready. Convergence is **not** "scores are high" — the
questions are adversarial by design, so high scores prove nothing on their own.

> Definitions: `spec.md` §9 (convergence), §12 (recalibration trigger). This playbook is the
> procedure.

---

## Convergence test (all three must be true at once)

1. **ACTIVE count = 0** in the `master_status.md` summary.
2. **FRAGILE count is small** — handleable in one revision pass (typically **≤5**), not another full
   mock.
3. **Coverage complete** — every node in the topic `topic_guide.md` content node map is SOLID,
   FRAGILE, or has been tested. **No UNTOUCHED nodes remain.** (This is the check people skip — walk
   the node map explicitly and confirm each node was hit.)

If any one fails, the loop continues (→ **playbook 03**): generate the next set targeting what's
missing — ACTIVE gaps, or untouched nodes for coverage.

---

## Final validation sequence (only after the three conditions pass)

1. **Model test** — a full set covering the **entire topic** (all clusters) under exam conditions →
   `courses/<Course>/<Topic_Name>/tests/model_test_[N].md`.
2. **Real past assessment — IF one exists.** If a genuine past assessment for this course/topic is
   available, the student attempts it under **realistic/timed conditions** →
   `courses/<Course>/<Topic_Name>/tests/assessment_[identifier].md`. This is the honesty check.
   - **If no real past assessment exists** (common outside formal exam contexts): the model test is
     the only readiness signal available. **Explicitly flag this** — do not declare the topic
     "ready" the same way you would with a real assessment behind it. State it as: *"Model-test-ready.
     Not yet verified against a real assessment — none exists/was supplied. Treat this readiness
     claim as provisional."*
3. **Interpret (only when a real past assessment was attempted):**
   - Both consistently high → **topic is mastery-ready.**
   - Model >70% **but** real assessment <50% → the **guide is misaligned with the real assessment.**
     Do **not** declare ready. Trigger recalibration (**playbook 01**): find the dimension that
     mispredicted, fix it, re-validate.
   - This >70%/<50% recalibration trigger only applies when step 2 actually happened — it cannot
     fire off a model test alone.

**A model test alone never converges a topic to full confidence** — it converges it *provisionally*.
The real past assessment (when one exists) is what upgrades "provisional" to "mastery-ready."

---

## Course-level readiness (on request only)

When the student asks, aggregate all topic `master_status.md` files for a course into a summary:
total ACTIVE, total FRAGILE, which topics are converged (mastery-ready or provisionally so) vs
in-progress. **Do not maintain this automatically.**

## Done when

You can state, with evidence, either "converged + validated on a real assessment → ready",
"converged + model-test-only → provisionally ready, unverified", or exactly which condition is unmet
and what the next session targets.
