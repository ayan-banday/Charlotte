---
date created: 2026-07-18
date updated: 2026-07-18
status: built 2026-07-18
---

# StudyOS Integration Spec

How StudyOS moves into Charlotte as an isolated, on-demand study mode.

---

## Goal

Ash sits down working. Says "I want to study today." Charlotte pulls up StudyOS, reports what courses exist and where progress sits, asks what he wants to work on, and runs the study session. Nothing else from Charlotte loads. At session end, a short digest lands in the current week file so studying feeds the existing reflection loop.

## Non-goals

- No git repo for StudyOS. Charlotte's existing `.git` is untouched by this spec.
- No merging of the two rule systems. StudyOS is scoped, not absorbed.
- No new automation, scheduling, or headless process.
- No changes to `SOUL.md`, `MEMORY.md`, `Patterns.md`, or the reflection protocols.

---

## 1. The move

`D:\StudyOS` moves to `s:\Charlotte\StudyOS\`. Internal structure unchanged: `system/`, `courses/`, `gaps/`, `inputs/`, and the four root docs.

Two deletions during the move:

- `D:\StudyOS\.claude\settings.json` is not carried over. It holds only stale allow-entries pointing at a WhatsApp Desktop transfers path and scratchpad files (`act3.md`, `act4.md`) that no longer exist.
- `UNPROCESSED_SESSION_2026-07-17.md` — discovery reported it at the root; it actually lives at `courses/Accounting_for_Business_Decisions/Accounting_Fundamentals/`. **Not stale, not deleted.** It holds real unprocessed session findings and is live work. Process it before session 2.

Charlotte's `.claude/settings.json` currently contains only two StudyOS read-permission entries for the old `D:` path. Once StudyOS is in-tree those are dead and should be removed.

## 2. CLAUDE.md changes

Total hot-context cost: two lines. Everything else lives inside StudyOS and loads only on trigger.

**One row appended to the `## TRIGGERS` table:**

```
| "study" / "let's study" | `/StudyOS/SYSTEM.md` | Enter study mode. Load StudyOS chain only. Digest to week file at end. |
```

**One edit to `## MEMORY ENGINE`, deep tier line.** Current:

> *Deep (grep on demand, never auto-loaded, Ash never asked):* `Recall.md`, `00 Self-Management/Patterns.md`, `00 Self-Management/Weeks/**`.

Becomes:

> *Deep (grep on demand, never auto-loaded, Ash never asked):* `Recall.md`, `00 Self-Management/Patterns.md`, `00 Self-Management/Weeks/**`, `StudyOS/**`.

No other CLAUDE.md edits.

## 3. Precedence

StudyOS's `SYSTEM.md` currently declares itself loaded every session, with `system/spec.md` winning on conflict. Both claims are rewritten to be scoped.

New rule, stated in `SYSTEM.md` frontmatter and its opening section:

- Charlotte's `CLAUDE.md` is the operating system. It always wins.
- `SYSTEM.md` is authoritative **within a study session only**.
- Within a study session, `system/spec.md` remains the source of truth on StudyOS mechanics.
- StudyOS is a mode Charlotte enters, not a system that runs alongside her.

Frontmatter to add to `StudyOS/SYSTEM.md`:

```yaml
loaded: NOT auto-loaded — read only when study mode is triggered
load-when: Ash says "study" / "let's study", or an active study session is running
scope: study sessions only; subordinate to /CLAUDE.md
```

## 4. Study mode load chain

On trigger, in order:

1. `StudyOS/SYSTEM.md` — laws, map, checklists
2. `StudyOS/courses/registry.md` — what courses exist, where progress sits
3. Charlotte reports state and asks what to study
4. On answer: that course's `context.md`, the relevant `topic_guide.md`, and `gaps/<Course>/<Topic>_gaps.md`

Nothing further from Charlotte loads once study mode is entered. No Skills Index, no File Structure Registry, no Patterns.md, no project files.

`system/spec.md` opens only when a specific mechanic requires it. `system/playbooks/*` and `system/prompts/*` open only when their matching operation fires. `METHOD.md`, `README.md`, `QUICKSTART.md`, and `system/templates/*` never auto-load.

**Bootstrap caveat, accepted:** `SOUL.md` and `MEMORY.md` are already in context before the study trigger fires, since they load at session start. Combined they are roughly 4.6 KB. The rule is that nothing *further* from Charlotte loads after entering study mode.

## 5. Study sheet invariant

`courses/**/cluster_*_study_sheet.md` files are never read whole. The current `cluster_01_study_sheet.md` is 417 KB, roughly 63% of all markdown in StudyOS.

Access is by grep or offset-read of the section in play only. This goes into `SYSTEM.md` as a numbered invariant alongside the existing ones, not as a soft guideline.

## 6. Digest bridge

At end of every study session, 3 to 5 lines append to `00 Self-Management/Weeks/Week [ISO].md` under that day's heading, matching the existing bullet-block shape.

Contents: what was studied, where it broke, what's next.

Example:

```markdown
## Saturday, 2026-07-18

- Studied Accounting Fundamentals, cluster 01 (Recording Financial Transactions), ~50 min
- Debits/credits on contra accounts still not automatic, third session it has come up
- Journal entry sequencing is solid now, moving off it
- Next: cluster 02
```

**One direction only.** StudyOS writes to the week file and reads nothing from Charlotte. Charlotte never reads study sheets.

The week file is already raw tape. "How's my week been" already plays it back. Weekly reflection already graduates recurring lines into `Patterns.md`. Study friction therefore becomes visible next to energy and drift patterns with no new machinery. A gap that recurs across three sessions surfaces the same way any other repeated pattern does.

## 7. Registry

One entry added to `File Structure Registry.md` for the `StudyOS/` folder: purpose, the fact that it is deep-tier and never auto-loaded, and the trigger phrase.

Note: the Registry is already stale (last updated 2026-06-08, unaware of `ATLAS/`, `CALENDAR/`, and Week 29). Fixing that is out of scope here; run "sync claude.md" separately.

---

## Build order

1. Move the folder, delete the two stale files
2. Rewrite `SYSTEM.md` frontmatter, precedence section, and add the study-sheet invariant
3. Add the end-of-session digest step to `SYSTEM.md`'s end-of-session checklist
4. Add the trigger row and deep-tier line to `CLAUDE.md`
5. Clean the dead `D:` permissions from `.claude/settings.json`
6. Add the Registry entry

## Verification

Working means: a fresh session where Ash says "I want to study" results in Charlotte reading `SYSTEM.md` and `registry.md`, reporting course state, and asking what to study, without touching Skills Index, Registry, or Patterns. And a session that ends produces week-file lines in the shape above.

## Open

- Whether `CALENDAR/` (empty, unregistered) should later hold study scheduling. Deferred, not part of this build.
- `ATLAS/` is dead and reclaimable. Unrelated cleanup, deferred.
