# Course Registry

**Read this at the start of every session.** It declares every course's default gap-closure type,
guide status, and confidence ceiling. Full detail on what each course actually assesses lives in
that course's own `courses/<Course>/context.md` — this table is the index, not the source.

**Adding a course = adding one row here + one `context.md` file.** See `QUICKSTART.md`. There is no
fixed course list and no level/track split (`H2`/`H1` etc.) — if a course has levels or tracks,
record that as a free-text note inside its `context.md`, not as a separate registry entry, unless
you genuinely want to track them as fully independent courses (separate guide, topics, gaps).

This project enables a **per-topic type override**: the table below gives the *default* type for a
course; an individual topic may override it in its own `topic_guide.md` front matter. Read the
default first, then the topic override — the override wins **for that topic only**.

---

## Registry

| Course | What it assesses (see `context.md`) | Default gap-closure type | Guide status | Confidence ceiling |
|---|---|---|---|---|
<!-- Example row — illustration only, not a real entry:
| Accounting | Professional certification exam, 2 papers, case-study heavy | `applied` | NOT BUILT | — |
-->
| Accounting_for_Business_Decisions | Self-set goal — master the JAIN bridge-course workbook (no assessment exists; see `context.md`) | `quantitative` | BUILT | LOW <70% — no held-out validation possible |

---

## Current position

*Where the student is standing right now, and what to open. Rewritten at the end of every session
(`SYSTEM.md` §9). This block is a convenience pointer, not a source of truth: if it disagrees with
that topic's `master_status.md`, `master_status.md` wins and this block gets corrected.*

**Accounting_for_Business_Decisions** → active topic: `Accounting_Fundamentals`

- **Coverage:** 3 of 81 nodes touched, 78 UNTOUCHED
- **Gaps:** 2 ACTIVE, 1 FRAGILE, 0 CLOSED
- **Last session:** 2026-07-17 — discussion only, no question set issued, so no score exists yet
- **BLOCKING:** one captured session has never been processed. It contains a confident-and-wrong
  error (capital vs profit). Say *"process the 2026-07-17 session"* before opening new material.
- **Open these:**
  - `courses/Accounting_for_Business_Decisions/Accounting_Fundamentals/master_status.md`
  - `gaps/Accounting_for_Business_Decisions/Accounting_Fundamentals_gaps.md`
  - `courses/Accounting_for_Business_Decisions/Accounting_Fundamentals/topic_guide.md`
  - `courses/Accounting_for_Business_Decisions/Accounting_Fundamentals/UNPROCESSED_SESSION_2026-07-17.md` (blocking)

---

## Type → gap-closure method

The full definitions (what "mechanical", "new angle", and "worked example" mean, plus the close
conditions per type) live once in **`system/spec.md` §2**. Reading never closes a `quantitative` gap
— variants must be solved.

Quick chooser (also in `courses/_TEMPLATE_context.md`):
- **`quantitative`** — answers are computed/derived (maths, calculations, data-handling).
- **`qualitative`** — answers are explained/argued (essays, concepts, mechanisms, humanities).
- **`applied`** — answers apply a framework to a source/scenario (case studies, professional
  scenarios, source-based questions).

---

## Guide status & confidence ceiling

Update a course's row when its guide is built: **Guide status** → `NOT BUILT` / `BUILT` /
`NEEDS RECALIBRATION`. **Confidence ceiling** → the validated ceiling from the guide's build (e.g.
`~90%`, `LOW <70%`), based on whether it rests on `[SOURCED]` materials, `[INFERRED]` proxies, or a
mix. A course with no official materials at all is not a blocker — it's a stated lower ceiling.
