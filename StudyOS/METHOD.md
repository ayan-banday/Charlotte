# METHOD — how a human drives this system

> `README.md` is the map. `SYSTEM.md` is the rulebook Claude follows. `QUICKSTART.md` is setup.
> **This file is the part that isn't in any of them: how you actually drive it.**

**The repo is the cheap part.** Anyone can clone the files. What makes it work is a set of moves that
currently live in one person's head — captured here, from a live session on 2026-07-17 that went
from an empty repo to a built course in about 40 minutes.

Every quote below is verbatim from that session.

---

## The workflow

```
   ┌─────────────────────────────────────────────────────────────┐
   │  0. FIX THE OUTCOME                                         │
   │     "what exactly is it that I want it to do"               │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  1. DROP THE SOURCE IN          inputs/<Course>/<Topic>/    │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  2. BUILD THE GUIDES            course_guide · topic_guide  │
   │     the node map IS the coverage checklist                  │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  3. PRE-STUDY                   ◀── its job is NOT to teach │
   │     read it to find out WHERE YOU ARE CONFUSED              │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  4. TEACH IT BACK, UNEDITED                                 │
   │     ramble. include the confusion. do not tidy it.          │
   └───────────────────────────┬─────────────────────────────────┘
                               │
              ┌────────────────┴────────────────┐
              ▼                                 ▼
   ┌─────────────────────┐          ┌──────────────────────────┐
   │ 5. GAPS GET CAUGHT  │          │ 6. TAKE THE CONFUSION    │
   │    confident+wrong  │          │    TO A HUMAN            │
   │    → Priority 1     │          │    friends · professors  │
   └──────────┬──────────┘          └────────────┬─────────────┘
              │                                  │
              │        sharper questions ────────┘
              ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  7. STUDY THE CLUSTER — bare minimum to move the train      │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  8. PRE-ATTEMPT BEFORE YOU KNOW ANYTHING                    │
   │     "this is supposed to be painful"                        │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  9. LOOM IT. SUBMIT IT.        ◀── the step most often skipped│
   │     transcript > self-rating                                 │
   └───────────────────────────┬─────────────────────────────────┘
                               ▼
                  ┌────────────────────────┐
                  │  gaps → gap cluster    │──┐
                  │  → more questions      │  │
                  └────────────────────────┘  │
                               ▲              │
                               └──────────────┘
                                  loop until
                          ACTIVE=0 · FRAGILE≤5 · no UNTOUCHED
                               │
                               ▼
                  ┌────────────────────────┐
                  │  GROUND TRUTH          │
                  │  a real past paper     │
                  │  (or say you have none)│
                  └────────────────────────┘
```

---

## 0 — Fix the outcome before anything else

**What it is**

Say what you want to be able to *do*, in your own words, before any method is discussed.

> *"The way I prompt things is gonna be output first. I am outcome obsessed."*

The outcome is fixed. **Everything downstream is disposable** — format, structure, sequence, all of
it. If you fix the method first, you end up defending the method.

**In action**

The outcome that drove this whole build:

> *"What I want us to do is: after I study the clusters, I want to be able to just be on par with a
> person that has studied 11th and 12th and actually exceed their skill level. I want to finish it
> as soon as possible. And how do I want it — I want to have what the concept is, how is that
> useful, understanding from the first principles, a few example questions, after that I do the SIR."*

One sentence of outcome, one sentence of shape. That produced 81 nodes and 6,000 lines.

**Set a fresh objective at every step, not once at the top.**

> *"So every moment I'm just setting new and new objectives."*

The pre-study sheet got its own:

> *"Why is the reason why we do pre-study in the first place? We do that to understand why something
> is important in the real world, how is accountancy important for things, what are the main big
> concepts that make accountancy work in the first place. Why do they work? And that's it. That's
> the objective I want to achieve."*

**The loop underneath everything**

> *"Aim is what questions I'm trying to answer, what is the objective I'm trying to achieve. Shoot
> is just looking at what we have — does it answer that question or not. And then refining it
> further and further. That's all I'm doing."*

**Where it bites**

- **Wrong:** "Build me a study guide for accounting."
- **Right:** "After this I want to out-reason commerce students on anything non-standard. Concept ·
  why it's useful · first principles · examples I can solve."

The first gets you a generic artifact you'll then spend an hour correcting. The second gets three
rounds of format rejection **before** anything is built, which is far cheaper.

---

## 1 — Confirm before you do anything

**What it is**

A standing instruction. The model proposes; you approve; only then does it build.

> *"Confirm before you do anything. This is a prompting technique I use to talk to AI. So it's like
> not really doing work for me, but it's doing work with me. It doesn't do anything until I ask it
> to do it."*

**In action**

Four formats were proposed and rejected before one shipped:

| Round | What was rejected |
|---|---|
| 1 | Clusters invented straight from the workbook's session list, skipping both guides |
| 2 | Three clusters, when one was wanted |
| 3 | A per-node format with a "why it exists" field — *"too much hedging"* |
| 4 | A story with character names — *"we don't need to put in names"* |

Each rejection cost one message. Any one of them, discovered after the build, would have cost the
whole build.

**Where it bites**

- **Wrong:** let it build, then correct 6,000 lines.
- **Right:** kill the format at the sample stage.

The one live example — a sample node was shown before 8 agents were told to replicate the format
81 times. That review cost two minutes.

---

## 2 — Pro-coding: move the train, don't build the heap

**What it is**

The model that explains every other decision here.

> *"Instead of having a heap of knowledge — where it's a big mound filled up of material that you
> don't know what to do with, and then you're like 'okay, how is this useful' — what I am doing is,
> let's put some material in a train, a cargo train, and just move it around. Procedural encoding,
> or more specifically **problem-based encoding**. So I'm only learning as much as required to solve
> the problem that I've set for myself."*

> *"I just will do the bare minimum. So instead of mind mapping and making a heap of knowledge that
> I understand deeply, I just go and solve problems and know the things as they become important and
> understand how can I apply them in different ways."*

> *"It's about putting the bare minimum to move the train and make it profitable."*

**Knowledge is cargo. Cargo that doesn't move is a heap.**

**In action**

This is why the study sheet is ordered by **when a business needs each tool**, not by terminology:

| Act | The moment | What it forces |
|---|---|---|
| 1 | Money goes in | Where did it come from? → **A = L + E** |
| 2 | Something happened — write it down | Two sides → the **journal** |
| 3 | To write it, name both accounts | A thing, a person, a reason → **three account types** |
| 4 | Not everything is cash | **Liabilities** get real. An order is not a transaction. |
| 5 | *"How much do we owe?"* | Time-order can't total → the **ledger** |
| 6 | Did we slip? | The **trial balance** — and what it can't catch |
| 7 | *"So did we make money?"* | The **statements** |
| 8 | The rules that stop you lying | **Concepts and conventions** — last |

Nothing is introduced until the train needs it to move.

**Where it bites**

- **Wrong:** learn the vocabulary, then the rules, then apply them.
- **Right:** hit the problem, learn only what unblocks it.

The failure mode of pro-coding is real and worth naming: **you can skip a foundation you actually
needed.** See §9.

---

## 3 — The pre-study sheet's job is to make you curious, not to teach you

**What it is**

This is the counterintuitive one, and it's the load-bearing insight of the whole method.

> *"So what I did till now is I understood the big picture — actually, the more important thing, **I
> failed at understanding the big picture** — but what I am now is **curious** about how does this
> all work. How can I use it for my own business? How can I make this useful for my own sake? Why do
> we need accounting? Why can't we just put everything in cloud?"*

**The pre-study sheet did not produce understanding. It produced a list of questions.** That was
logged as the win.

**In action**

Twenty minutes with the pre-study sheet produced this, and none of it is comprehension:

> *"I see the balance sheet, the income statement, the cash flow, though **I don't have an idea as
> to why they're called as such**… I have **no clue how does the format work**, why is the format,
> and how does it all look and act… what I'm still confused about is the types of accounts, real,
> personal, nominal — **why are they called such, why do they exist**… ledger — **I have no clue why
> do we need a ledger, and what even is a ledger**. Trial balance, **no freaking clue** what that
> is. Financial statements, **no idea** what that is."*

That list became the brief for 6,000 lines of study sheet. **The confusion was the deliverable.**

**Read to locate confusion, not to absorb.**

> *"Actually, no, I kind of tried to understand it — and where I don't understand, **that's the most
> important thing. Where am I confused at? This is very important.**"*

**Where it bites**

- **Wrong:** read the pre-study until you understand it, then move on.
- **Right:** read it once, note every place you stalled, move on **still confused**.

Re-reading until it clicks builds the heap. The confusion is what the next artifact is built from —
if you resolve it privately by re-reading, you have destroyed the input and learned less.

---

## 4 — Teach it back unedited

**What it is**

Say everything you think you understood, out loud, including the parts you don't. **Do not tidy it.**

**In action**

This produced the single most valuable catch of the session. Verbatim:

> *"Everything we own, assets, is gonna be equivalent to liabilities, **which is just the things
> we've spent the money on**, plus what we own in the business."*

That is a flat inversion of the accounting equation's right-hand side. It was stated **confidently,
unprompted, with no hedge** — which is the exact `spec.md` §4 danger case. It was logged as
**Priority 1**, and it is the most dangerous state in the system precisely because it does not feel
like a gap from the inside.

**It was caught because the teach-back was a ramble.** A polished paragraph would have hidden it.

**Honesty is a mechanism here, not a virtue.** Watch it happen mid-sentence:

> *"Equity is just — **I have no clue what equity is. You gotta be honest with yourself.** I know
> what equity is, it's like how much of the business you own, but I don't know how it means in
> here."*

That is someone catching themselves **in the act of performing understanding** and stopping. The
whole engine depends on that reflex.

**Track your own confidence while you answer.** This, said out loud during a question attempt:

> *"Yep, I got it right — but of course my confidence was low, so I didn't know that."*

That is a manual read of the **delta zone** (`spec.md` §4). Correct-but-unconfident defaults to
**FRAGILE**. Guessing right is not mastery, and the system only knows you guessed if you say so.

**Where it bites**

- **Wrong:** write a clean summary of what you learned.
- **Right:** ramble, contradict yourself, say "I have no clue" four times.

A clean summary is a performance. Performances have no gaps in them, which is why they're worthless
as input.

---

## 5 — Take the confusion to a human

**What it is**

**The system's real output is not knowledge. It is a sharper question to bring to a person.**

> *"I will be taking the stuff that I didn't understand and discussing it with my friends and
> professors, so it makes my questions sharper and me more useful."*

This is not a fallback for when the AI fails. It is a **designed stage**, and it runs on the exact
artifact §3 and §4 produce: a precise list of what you don't understand.

**In action**

> *"That's just like something that I'll get checked out with my professors, talk to them and
> actually make my ideas better. So yeah, I do a lot of intellectual work. It's going to be me
> talking to an accounting friend that I have. She seems smart. Professor, of course."*

And the second-order effect, which is the part most people miss:

> *"**It actually gives me social credit as well**, because now I can ask him for the PDFs. He's the
> guy that sent me this PDF. It was a lot of work if I had to transcribe it all on my own. So that
> also has political benefits."*

The loop compounds:

```
   confusion  ──▶  sharper question  ──▶  better conversation
        ▲                                        │
        │                                        ▼
        │                            you are more useful to them
        │                                        │
        └──────  they give you better source  ◀──┘
                 material next time
```

**Where it bites**

- **Wrong:** show up to a professor and ask "can you explain accounting?"
- **Right:** show up with *"why is a Bank A/C Personal when a Cash A/C is Real?"*

The first is a request for labour and gets you a shrug. The second is a good question, gets a real
answer, and makes the person want to send you the next PDF unprompted. **Vague questions cost people
time. Sharp questions make them feel useful.**

---

## 6 — Aim one band above the requirement, then cap it

**What it is**

Target a higher Bloom level than the assessment demands — because it is more effective, not for
prestige. **Then stop.**

> *"They're just focusing on the memorization stuff, but I don't like that. F\*\*\* that. So I'm
> going to actually get to an apply, analyze, honestly level. **I don't need evaluate level. It's
> like far too overkill.** I just need to be able to memorize, define, state. That's it. But of
> course I'm going to go higher because **it's much more effective for me to do that.**"*

Both halves are the move. Aim up **and** cap it. Most people do one.

**In action**

The workbook's five outcomes are *define · state · list · memorize · list*. Pure recall. Its
assessments are crosswords and word searches.

The study sheet built against it is **Application-or-higher only** — because rote-trained students
can journalise fluently and still not say what a debit *is*, and that gap is the whole edge.

**Where it bites**

- **Wrong:** match the assessment's level. You'll be exactly as brittle as everyone else.
- **Right:** one band above. It's less work than it sounds, because derived knowledge needs no
  maintenance.
- **Also wrong:** three bands above. That's how a bridge course eats a month.

---

## 7 — Orchestrate, then verify the orchestrator

**What it is**

Fan work out to agents. **Then check your own briefs, because you are the least reliable component.**

> *"It's just like loading up a few sub-agents. F\*\*\* it. It's complicated stuff, which I love to
> use."*

> *"What AI did to me is it made me a better manager. Because what I can now do is I can be a
> conductor of an orchestra — just wave my hands and tell people what to sing."*

**In action — the architecture that made 8 parallel agents safe**

Naive fan-out breaks. Acts 5, 6 and 7 all narrate the same ledger; eight agents each computing it
independently produces eight subtly different sets of numbers, and the continuity dies.

**Fix: freeze the spine first.**

```
   PHASE 0 (you, alone)          PHASE 1 (8 agents, parallel)      PHASE 2 (you)
   ┌──────────────────┐          ┌──────────────────────┐          ┌───────────────┐
   │ build the        │          │ each narrates the    │          │ integrate     │
   │ CANONICAL        │─frozen──▶│ frozen spine.        │─────────▶│ verify nodes  │
   │ worked example.  │          │ NEVER recomputes it. │          │ check figures │
   │ verify it.       │          │ no shared state.     │          │ kill drift    │
   └──────────────────┘          └──────────────────────┘          └───────────────┘
```

**Every error in the build was the orchestrator's. Not one was an agent's:**

| Error | Caught by |
|---|---|
| Spine claimed an omission demo lands at 26,10,000. It lands at **26,60,000 — identical.** | Verifying my own arithmetic before dispatch |
| Node map called artificial persons **Real**. They're **Personal**. | **An agent**, which refused the brief and flagged it |
| Node count written as 63, then 73. Actually **81**. | A mechanical diff against the map |
| Three nodes never assigned to any agent | The same diff |

The agents were the disciplined ones. One refused to invent a depreciation rate the spine didn't
contain. One deleted two of its own unsourced figures rather than let them stand.

**Where it bites**

- **Wrong:** fan out, collect, ship.
- **Right:** freeze the shared state, fan out, **then verify mechanically** — diff the coverage,
  recompute the arithmetic. Do not eyeball it.

If a workflow has no verification phase, its output is your first draft with more steps.

---

## 8 — Format is disposable. Kill it the moment it stops serving.

**What it is**

> *"I change format the moment it becomes necessary, trying to see what goal I'm trying to achieve.
> So that's something you'll see actively me doing — the shaping, every system, based off of the
> things that I've done till now and what I find the most useful."*

**In action — the format that shipped, after three rejections**

```markdown
## [Node] — [Name]              [SOURCED p.N] or [EXT — not in your workbook]

**Definition**
Plain words. What it is · why it exists · where the name comes from · the logic under it.

**Why the format looks like this**
The shape is forced by the job. Explained BEFORE the format appears.

**The format**
Table or ASCII box diagram, drawn in full.

**In action**
Worked example on real numbers.

**Where it bites**
Only where a real confusion exists. Solve an example containing it, name the exact point it bites.

**Your turn**
2 questions. Self-contained. Answer gated directly underneath.
```

**What got killed, and why:**

| Killed | Reason |
|---|---|
| A "why it exists" field per node | *"Too much hedging."* The **story order** already carries the why — you feel the need before the tool arrives. |
| Character names ("Mr. Ganesh") | *"We don't need to put in names. It's more like how the sequence of events would look in the real world."* |
| A one-line definition cap | *"It doesn't have to be one line, as long as it helps me understand in simple words at the seventh-grade level."* |
| Abstract trap explanations | *"Solve an example that might be a trap, then I try to solve it. Tell me where it could be a trap."* |
| An answer key at the end of the file | See below. This one shipped broken. |

**Where it bites — a real failure, kept here because it's instructive**

The first build put all ~160 answers in one block at the end of a 6,135-line file. Technically it
met the spec (*"the answer is given so I can compare"*). Practically it was useless:

> *"They didn't have an answer that I can compare my answer with the question, so I can solve it and
> be like 'yeah, I got it right or not?' They weren't self-contained, so I didn't know what they
> were referring to, so it was vague. **I want the questions to be self-contained regardless.**"*

Two defects, one root cause — **the question was not solvable where it sat**:

- **Not self-contained.** Questions referenced "Day 4" and "Stage 3" and "the first week". You had to
  hold the whole worked example in memory to parse the question.
- **The answer was 6,000 lines away.** Present, and unreachable.

- **Wrong:** questions that reference context + one answer key at the end.
- **Right:** every question restates every figure it needs, and the answer sits gated directly
  underneath it.

**Restating a figure inside a question is not redundancy. It is what makes it a question.**

---

## 9 — The open question: when can you drop the map?

**What it is**

Pro-coding says skip the mind map. This session did:

> *"This is where the mind mapping will kick in. I'll start hip-shotting… but I won't use my tablet
> because it's too much of a bother. I don't need to do proper mind mapping for this."*

And then, forty seconds later, in the same session:

> *"I'm either at high conscious competence, slash unconscious competence — or just, you know, that
> place, **Mount Fuji of stupidity**. So Dunning-Kruger effect, that might be the case."*

**Both are true, and they're about different skills.**

- **Unconscious competence at driving the system.** Earned. Ten-plus builds behind it.
- **Novice at accounting.** Day one.

**In action — the cost, visible in real time**

At 24:00, hip-shotting a balance sheet, forty minutes after the P1 correction landed:

> *"Capital 20 lakh — it's money that we made."*

**Capital is what the owner put in. Profit is what was made.** That is a new gap, adjacent to the one
just corrected, and it went into no file.

**Where it bites**

- **The claim:** *the map is optional; problems teach you what you need.*
- **The risk:** the shortcut was earned in domains where you already had the map. Spending it in a
  domain where you're a novice is borrowing against competence you don't have yet.

**This is falsifiable in one session.** Run the next cluster with a map and compare the gap count.
It's the most useful open question in the method, and it's cheap to answer.

---

## 10 — The step that gets skipped

**Loom the attempt. Submit it.** This is the one the session dropped, and it's worth being blunt
about because it's the system's whole point.

> *"At this point I'd be recording on a Loom to give it the transcript."*

Then, seven minutes later:

> *"I won't be recording this onto a Loom, because this is just me trying to understand through
> examples."*

**A real graded session ran between 24:00 and 31:00 and the transcript was thrown away.** What was
recoverable is written up in
`courses/Accounting_for_Business_Decisions/Accounting_Fundamentals/UNPROCESSED_SESSION_2026-07-17.md`.
It includes a **candidate Priority 1** — and it survived only because a recording happened to be
running for an unrelated reason.

The irony is exact: **an engine built to catch confident-and-wrong, and the session was hand-graded
in someone's head** — which is the self-rating `spec.md` §4 says to distrust.

The P1 that *did* get caught was caught by accident of format. It happened to be rambled into a chat
message instead of scribbled on paper.

- **Wrong:** "this one's just me messing about, I won't record it."
- **Right:** record it. The session where you're *"just trying to understand"* is exactly the session
  where the gaps are.

**A gap you noticed and didn't log is a gap you will meet again, at full strength, later.**

---

## Run it yourself

1. **Say the outcome.** Not the topic — what you want to be able to *do*, and roughly what shape.
2. **Say "confirm before you do anything."** Keep saying it.
3. **Drop the source in** `inputs/<Course>/<Topic>/`. Say *"ingest the inbox."*
4. **Reject formats early.** Demand a sample node before anything is built at scale.
5. **Read the pre-study once.** Do not re-read it. **Write down every place you stalled.**
6. **Teach it back as a ramble.** Include every "I have no clue". Do not tidy it.
7. **Read the gaps it flags.** The confident-and-wrong ones are the point.
8. **Take the confusion to a human.** Sharper questions, better source material, compounding.
9. **Pre-attempt questions before studying them.** It's supposed to hurt.
10. **Record it. Submit it.** Every time. Especially the casual ones.
11. **Loop** until ACTIVE = 0, FRAGILE ≤ 5, no UNTOUCHED nodes.
12. **Find ground truth** — a real past paper. If none exists, say so out loud and keep the
    "unverified" flag attached.

**Setup is one-time.**

> *"This is like 9 a.m. … it's been like 40 minutes or so. Built a system from scratch. **I won't
> have to do this again.**"*
