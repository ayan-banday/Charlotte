---
date created: 2026-06-07
date updated: 2026-06-07
---

# Write a Newsletter

**Problem:** The newsletter skills exist but were never wired into one flow pointed at Ash's
own voice — so "I have an idea" never reliably becomes "published newsletter."

**Outcome:** A finished, humanized newsletter draft in Ash's voice, with a branded banner,
saved into the active Newsletter project.

**Time investment:** 30–90 minutes depending on how much mining the idea needs.

---

## Prerequisites

Before running:
- An idea, a problem, or a rough thought to build on (the rawer the better).
- Hot memory loaded (`SOUL.md` + `MEMORY.md`) so the voice and audience are already known.

---

## Workflow Steps

### Step 1: Interview / Mine
Run `[[newsletter-writing-system]]` **Mining Prompt** (the 7-phase dig). Charlotte interviews Ash:
big idea, A→B transformation, the one takeaway, the lived story, named concepts, proof.
**Output:** a Newsletter Brief.

### Step 2: Hook research
Run `[[content-hook-research]]` on the topic — real viral hooks (YouTube/Reddit/IG), no
fabricated numbers. **Output:** 3 title options, adapted to Ash's voice. (Mandatory before titling.)

### Step 3: Draft
Run `[[newsletter-writing-system]]` **Newsletter Writing Prompt** (APAGA, section by section).
**Voice-check every section against `[[ash-newsletter-voice]]` — Ash, not Jani.** That's the default.

### Step 4: Humanize
Run `[[text-humanizer]]` on the full draft to strip AI tells.

### Step 5: Image
Run `[[newsletter-image-generator]]` for the banner — Ash's brand/logo (not a client's).

### Step 6: Save
Drop the draft + image into `EFFORTS/Active/Newsletter Becoming the Person Your Goals Belong To/`
(or the relevant newsletter project).

---

## Decision Points

**Skip mining (Step 1)** when a Brief already exists for the idea — go straight to Step 2.
**Chisel mode** when fixing an existing draft — run only the Newsletter Writing Prompt on the
named weak section.

---

## Parallelize

Steps that don't depend on each other can fan out: while the draft (Step 3) is forming,
hook research (Step 2) and image generation (Step 5) can run as subagents. Recombine at Step 6.

---

## When to Use This Workflow

Trigger: "write a newsletter" / "I want to write a newsletter" / "let's do this week's issue."

Frequency: weekly (the publishing cadence).
