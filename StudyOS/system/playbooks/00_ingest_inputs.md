# Playbook 00 — Ingest the Inbox (raw pile → structured inputs)

> **Status: v1 — refine after the first real ingest.** This is the newest playbook and has not yet
> been run end-to-end. Treat the **first batch as the calibration run**: tighten these rules from
> what actually happens, don't pre-write imagined edge cases.

**Goal:** turn a rough pile dropped in `inputs/_inbox/` into correctly-named, correctly-filed
materials under `inputs/<Course>/<Topic>/[category]/`, so guide-building (playbook `01`) can ground
on them. **This is the one place you touch `inputs/` — mechanical filing, not generation.**

> **Inputs are optional.** This playbook only runs if the student or their assistant actually has
> raw material to file. No inbox, no problem — guides can be built on research alone with a stated
> confidence ceiling (`spec.md` §5, §13). Don't ask for materials that don't exist; just note the
> ceiling.

> Definitions: the input contract (categories, naming) is in `inputs/README.md`. Grounding
> hierarchy: `spec.md` §13. Naming: `spec.md` §12.

---

## Preconditions
- Someone has dropped files into `inputs/_inbox/` — **hinted** (`_inbox/<Course>/<Topic>/...`) or as
  a **raw pile** (loose files). Both are valid.
- Triggered by the student saying e.g. *"ingest the inbox."* Never auto-run.

## Classify each file (three fields)
For every file, determine three fields and **mark each as `given`** (from a hint subfolder or the
filename) **or `inferred`** (read from the file's content):
1. **Course** — whatever the student is actually studying; no fixed list. A hint subfolder wins;
   otherwise derive from the file's own content (title page, header, syllabus code).
2. **Topic** — a real content name, underscores, no spaces (`Chinese_Politics`, never `Topic_1`). A
   hint subfolder wins; otherwise derive from the syllabus/curriculum + content.
3. **Category** — a rough bucket: `past_assessments` · `official_docs` (syllabus/curriculum, rubric,
   grading criteria) · `notes` · `model_answers` · `resources` (anything else useful — school
   handouts, textbook excerpts). Treat these as illustrative, not rigid — file into the closest fit.

## Naming (apply on the move)
- Underscores, no spaces, everywhere.
- Past assessments `[identifier]_p[N].pdf` (e.g. `2024_p1.pdf`); their mark schemes/rubrics
  `[identifier]_p[N]_ms.pdf`.
- **Never invent metadata you cannot see in the file.** If the date or paper number is not actually
  on the page, do **not** guess it into the filename — flag it for the student to supply.

## Confidence gate (the grounding guard)
- **All three fields confident** (given, or clearly read) → stage the move.
- **Any field low-confidence, or a conflict** (hint says X, content says Y) → **quarantine**: leave
  the file in `_inbox/`, list it under "needs confirmation" with your best guess. **Never silently
  misfile and never silently rename** — misfiled grounding is worse than an unfiled file.

## Procedure
1. **List** everything in `_inbox/` (recurse hint subfolders).
2. For each file, **read enough to classify** the three fields; build the
   `original_path → destination_path` mapping; tag every field `given`/`inferred`.
3. **Show the full mapping table to the student before moving anything** — each row: original name,
   destination, and which fields were inferred. *This table is the rename/refile audit* — it is how a
   misread date or a wrong topic gets caught.
4. On approval, **create missing destination folders and `move`** (not copy) the confident files.
   Leave quarantined files in place.
5. **Report:**
   - what moved where;
   - what's quarantined and why (the field in doubt + best guess);
   - **per topic touched, whether it now has enough to ground a guide** — i.e. what's ready for a
     guide, and what's still thin (note: thin/no inputs is a valid state, not a blocker — playbook
     `01` still runs, just with a lower stated confidence ceiling).
6. **Stop at filed-and-reported.** Do not build guides here — that's playbook `01`.

## Done when
`_inbox/` holds only quarantined files (or is empty), every moved file traces to a real
course/topic/category, the student has seen the mapping, and the report states which topics are
ready for playbook `01` and which are thin (and by how much).
