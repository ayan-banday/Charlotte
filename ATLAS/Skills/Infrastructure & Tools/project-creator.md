---
name: new-project
description: Creates a new project in the workspace with a pre-filled project overview. Trigger this skill whenever the user says "new project", "start a project", "create a project", "I want to work on something new", "add a project", or anything that signals they want to kick off a new project. Always interview the user before creating any files.
---

# New Project

This skill interviews the user about a new project, creates a folder and project overview, and registers the project in CLAUDE.md so Claude knows about it in future sessions.

## Step 1 — Interview the user

Before creating anything, ask these questions in a single conversational message. Don't make it feel like a form — keep it natural:

1. **Name** — What's the project called?
2. **Goal** — What is this project trying to accomplish? (one sentence is fine)
3. **Why** — Why does this project matter to you? What's the real reason you're doing it?
4. **Tangible Outcomes** — What does "done" look like? What will exist when this project is successful?
5. **Open Problems** — Do you already know the main problems you'll need to solve? (totally fine if they don't know yet)

Wait for their answers before doing anything else.

## Step 2 — Create the project folder and overview

Once you have their answers, create:

```
EFFORTS/Active/<Project Name>/
└── <Project Name> Overview.md
```

The overview file is the most important file in any project — it's what Claude reads first every time the project comes up.

Use this exact template:

```markdown
---
type: problems
date: YYYY-MM-DD
project: <Project Name>
---

## Goal
<their goal answer>

## Why
<their why answer>

## Tangible Outcomes
- <outcome 1>
- <outcome 2>
- <outcome 3>

## Open Problems
<if they gave problems, list them numbered: 1. Problem one>
<if they didn't, write: 1. (to be defined — we'll figure these out as we go)>
```

## Step 3 — Register the project

So future sessions know it exists, add one line under the **EFFORTS/** section of `AIOS/Vault Map.md` naming the new project. That is the whole registration — no index, no CLAUDE.md edit.

## Step 4 — Confirm and offer to dive in

Tell the user:
- The project folder and overview are created
- CLAUDE.md has been updated so Claude will remember this project
- Ask: "Want to dive into one of the open problems right now, or save it for later?"

Keep it short — they're ready to work.
