# Templates

Blank skeletons Claude **copies** when generating a real file, so every artifact has the same shape
regardless of course. Placeholders look like `[Course]`, `[Topic_Name]`, `[Date]`, `[N]`.

**You don't edit these — the system fills copies of them.** Append-only files (`master_status`, `flags`)
are templates for the *first* write; later sessions **append** new blocks beneath, never overwrite.

| Template | Used for | Playbook |
|---|---|---|
| `course_guide.template.md` | `<Course>/course_guide.md` | 01 |
| `topic_guide.template.md` | `<Course>/<Topic>/guide.md` | 02 |
| `pre_study_sheet.template.md` | `<Course>/<Topic>/pre_study_sheet.md` | 03 |
| `cluster_study_sheet.template.md` | `<Course>/<Topic>/clusters/[NN_Cluster]/cluster_NN_study_sheet.md` | 03 |
| `concept_doc.template.md` | concept docs for ACTIVE/FRAGILE gaps | 05 |
| `flags.template.md` | `<Course>/<Topic>/clusters/[NN_Cluster]/cluster_NN_flags.md` (append-only) | 05 |
| `master_status.template.md` | `<Course>/<Topic>/master_status.md` (append-only) | 05 |
| `topic_gaps.template.md` | `gaps/<Course>/<Topic>_gaps.md` (regenerated roll-up) | 05 |
| `model_test.template.md` | `<Course>/<Topic>/tests/model_test_[N].md` | 06 |

Dates are absolute (e.g. `2026-06-05`). Names use underscores, no spaces, real content names.
Cluster folders are prefixed by their zero-padded study-order number (`01_...`, `02_...`), and
their inner study-sheet + flags files mirror the prefix (`cluster_01_study_sheet.md`,
`cluster_01_flags.md`). Off-sequence clusters (synthesis, gap, mastery) use `cluster_gap_` or `cluster_synthesis_`
in place of the number.
