---
date created: 2026-04-30
date updated: 2026-08-17 — Repaired workflow-skill reference.
---

# Claude Workflow Discovery Pattern

**Purpose:** How Claude should help when starting any project or workflow.

**Problem it solves:** When starting work on a workflow/project, the user often forgets what tools, resources, and workflows they have available. We need a discovery phase first that surfaces everything relevant before diving into execution.

---

## The Problem

Current state when starting a workflow:
- User says "I need to build X" (e.g., "I need to build a webinar")
- Claude jumps into asking clarifying questions or diving into the workflow
- User forgets what resources exist
- Outcome: Inefficient. Missing context.

Desired state:
- User says "I need to build X"
- Claude runs a discovery sweep first
- Claude shows: "Here are the workflows, skills, context, and resources relevant to X"
- User and Claude decide together which tools to use
- Then they dive into execution

---

## The Discovery Pattern

### Project Setup Phase (Once, Upfront)

When creating an active project file, structure it with:

**1. Phases defined by OUTCOME, not process**
- Not: "Write pre-launch emails" (this is how)
- But: "Excite the people and identify their core objections" (this is what happens)
- Each phase answers: What does success LOOK LIKE in this phase?

**2. Resources mapped to each phase**
- List relevant workflows for each phase
- List relevant skills for each phase
- List relevant context files (brain dumps, prior work, etc.)
- Example for webinar Phase 1: [[Build an Email Campaign]] workflow, [[Skills Library/Marketing/Sales & Conversion Copy/email-campaign-writer/campaign-strategy|Campaign Strategy]] skill, brain dump on procrastination objections

**3. Timeline and success metrics**
- When does each phase happen?
- What does done look like? (# registrations, # responses, # refinements, etc.)

**4. North star**
- This project file becomes THE reference. When you sit down to work, you start here.

---

### Session Work Phase (Daily/Weekly)

When you sit down to work on an active project:

**1. Claude surfaces the structure**
- "Here's the project. Here are your phases. Which phase are you in today?"
- Concise, bulletized, outcome-focused

**2. User picks a phase**
- "Phase 1: Excite people and identify objections"

**3. Claude shows resources for that phase**
- Workflows available
- Skills available
- Context/existing files
- Layered: big picture first, detail on demand

**4. User picks a starting point**
- "Let's start with [[Skills Library/Marketing/Sales & Conversion Copy/email-campaign-writer/campaign-strategy|Campaign Strategy]]"

**5. Dive into execution**
- Claude walks through that specific workflow/skill step-by-step

---

## Key Principle

**Thinking happens at project setup. Execution happens in sessions.**

Project file = decision-making and structure
Session work = following the structure and diving deep

This prevents forgetting what you have. It's all in one place. When you sit down, you reference the project file and ask: "Which phase are we in? What resources do we have for this phase?"

---

## Index + Introduction Sync Pattern

**When entering ANY folder to work:**

1. Read the index (e.g., `[C] Skills Index.md`, `[C] Workflows Index.md`)
2. Read the introduction (e.g., `00 Introduction to Skills Library.md`)
3. Identify the specific prompt/skill/workflow you need
4. Use that resource

**When making changes to ANY folder:**

1. Update the specific file (skill, workflow, prompt, etc.)
2. Update the index to reflect the change (description, status, location)
3. Update the introduction file to reflect the change (new skill listed, updated date, etc.)
4. Everything stays in sync — no searching needed

**Example:** Upgraded email-campaign-writer skill
- Changed: 6 skill files (German → English)
- Updated: `[C] Skills Index.md` (new description)
- Updated: `00 Introduction to Marketing.md` (reviewed date)
- Updated: `00 Introduction to Skills Library.md` (reviewed date)
- Result: All references point to current, correct resources

**Rule:** Index and Introduction files are the source of truth. Keep them current.

---

## How to Use This File

When upgrading the Claude co-work system, reference this file to:
- Implement the project file structure for active projects
- Define phases by outcome (what it looks like) not process (how you do it)
- Map workflows/skills to phases at project creation time
- Create the session-level prompt that references the project structure
- Build the "which phase today?" conversation pattern
