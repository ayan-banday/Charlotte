# Playbooks — the mechanics

Step-by-step procedures the coach reads **before** running each operation. They hold the
deterministic mechanics; the **prompts** (`system/prompts/`) are the conversational entry points
that invoke them, and **`spec.md`** holds the definitions. Playbooks **reference** `spec.md` rather
than restating it.

**You don't edit or run these — the coach follows them.**

| Playbook | When it's read | Entry prompt |
|---|---|---|
| `00_ingest_inputs.md` | Filing an optional raw drop pile from `inputs/_inbox/` into the structured `inputs/<Course>/<Topic>/` tree — the one place the system touches `inputs/` (mechanical filing, not generation). Skipped entirely if no inputs are supplied. | student: *"ingest the inbox"* |
| `01_build_guides.md` | Building a course guide (once per course) or a topic guide — incl. the 90% / 5-dimension check and `[SOURCED]`/`[INFERRED]` tagging | `prompts/01`, `prompts/02` Step 4 |
| `02_cluster_and_study.md` | Proposing the cluster breakdown, generating clusters one at a time, writing study + pre-study sheets | `prompts/02` Steps 3–5 |
| `03_run_session.md` | The full session loop: generate adversarial questions → detect confidence → grade → the 7-step gap-tracking sequence → next set | `prompts/02` Step 6 |
| `04_convergence.md` | Checking the three convergence conditions; final model test + a real past assessment **if one exists** | `prompts/02` Step 7 |
| `05_studied_topic_mock_exam.md` | Optional integrated mock spanning multiple already-studied topics/clusters — tests deployment under time pressure, between per-cluster session tests (03) and the final convergence gate (04) | student: *"give me a mock covering [topics]"* |
| `06_daily_plan_driver.md` | **Fully optional.** A lightweight, generic per-course study planner — only used if the student wants a schedule; the system works fine session-by-session with no plan at all | student: *"what should I study next"* / *"build me a study plan"* |

Each playbook names the **template** it copies from `system/templates/`.
