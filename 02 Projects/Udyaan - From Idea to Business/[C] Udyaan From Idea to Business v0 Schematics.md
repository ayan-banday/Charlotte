---
date created: 2026-08-17
date updated: 2026-08-17
status: active
purpose: Make the Udyaan From Idea to Business course v0 playable prototype buildable by a new team without prior context.
---

# Udyaan From Idea to Business Course v0 Project Schematics

## 1. Context

The **Udyaan From Idea to Business course v0** is the playable learning layer for Udyaan's *From Idea to Business* course. It helps a student move from an untested business idea to a first real-world business attempt. The course teaches the decisions; the v0 product turns those decisions into missions, visible progress, submitted evidence, and feedback.

This document is the starting point for curriculum contributors, designers, engineers, interns, professors, and reviewers. It describes what v0 must do, what it deliberately does not do, and the questions that must be answered before the build expands.

## 2. v0 Objective

Build one usable, deployed learning loop that a student can complete independently:

1. Enter one mission.
2. Learn only what is needed for that decision.
3. Complete a real business action.
4. Submit a visible artifact as evidence.
5. Receive feedback.
6. See what changed and what unlocks next.

**v0 is not the full 39-hour course.** It is proof that the course can become a useful product. It must be small enough to ship, clear enough to test, and structured enough to expand.

## 3. v0 Scope

### The first mission

The first v0 mission should be **Map the Territory: find and define a customer problem.**

The student must leave with:

- A chosen customer group.
- A written problem statement.
- Evidence from at least one real customer conversation or other approved evidence.
- An estimate of urgency, cost, or current alternatives.
- A next decision: continue, revise, or choose another problem.

### Required student flow

1. **Start:** The student sees the mission, its outcome, time expectation, and proof required.
2. **Learn:** A short lesson and Loom/video explain the decision and common mistake.
3. **Practise:** GPT-supported prompts help the student draft questions, a problem statement, or an interview plan.
4. **Act:** The student carries out the real-world task.
5. **Submit evidence:** The student submits the artifact and a short reflection.
6. **Receive feedback:** AI gives structured first-pass feedback. A human can review or override when required.
7. **Progress:** The student sees mission status, feedback, and the next unlocked step.

### Required v0 screens

- Sign in / student profile.
- Home or map view showing the current mission and progress.
- Mission page containing the outcome, lesson, task, rubric, and submission action.
- Artifact submission page.
- Feedback and revision page.
- Simple staff/reviewer view for seeing submissions and leaving feedback.

## 4. Deliverables by August 31

| Deliverable | What it contains | Done means |
|---|---|---|
| **Product requirements brief** | Student, problem, promise, first mission, user flow, non-goals, success measures | A new contributor can explain what the Udyaan From Idea to Business course v0 is for and what the first student must achieve. |
| **Curriculum and content specification** | First mission lesson, video outline, GPT practice, real-world task, artifact rubric, feedback rules | The curriculum team can create the first mission without inventing its learning logic. |
| **Game-mechanics specification** | Map/world concept, mission state, progress rules, unlock condition, feedback state, rewards kept minimal | A designer and engineer can build the experience without guessing how progress works. |
| **UX and interaction specification** | Screen list, annotated wireframes, empty/error/success states, accessibility and mobile assumptions | A designer can turn it into high-fidelity screens and an engineer can estimate the work. |
| **Technical foundation decision pack** | Stack decision, system diagram, data model, API/action list, auth roles, deployment and test plan | Engineers can challenge the choices, then begin implementation from one shared source of truth. |
| **Intern-team operating pack** | Role briefs, selection criteria, decision rights, weekly outputs, meeting cadence, project board | Interns can join a clear operating system rather than becoming a collection of helpers. |
| **v0 resource and cost model** | People, hours, software, AI use, feedback capacity, infrastructure, alternatives, risk | Ash can explain what the prototype costs, what the university supplies, and what must be constrained. |

## 5. Curriculum Specification for the First Mission

| Element | v0 decision |
|---|---|
| Student promise | "By the end of this mission, I can name a customer problem worth investigating and show the evidence behind it." |
| Lesson | What a business problem is, why assumptions are not evidence, how to choose a reachable customer group. |
| Story beat | The explorer enters a territory with many possible paths and must choose one problem to investigate, rather than immediately forge a solution. |
| Real-world task | Speak with a potential customer or collect approved first-hand evidence; record the problem, urgency, current workaround, and exact language used. |
| Required artifact | Customer/problem brief: customer group, problem statement, evidence, urgency/cost/alternative, and open assumptions. |
| Feedback rubric | Specificity of customer, evidence quality, urgency/value, clarity of wording, and falsifiable next step. |
| Unlock condition | Artifact meets the minimum rubric or is revised after feedback. |

## 6. Game-Mechanics Specification

The course v0 should make progress visible. It should not add points, streaks, or decorative game mechanics that distract from real work.

| Mechanic | Purpose | v0 rule |
|---|---|---|
| Territory map | Show where the student is in the business journey | One visible route with the current mission active and the next mission locked. |
| Mission state | Make progress unambiguous | `not_started` → `in_progress` → `submitted` → `needs_revision` or `completed`. |
| Evidence inventory | Show that business learning produces proof | Every completed mission stores one artifact and its feedback. |
| Unlock | Tie progress to demonstrated learning | The next mission unlocks only after the artifact passes the minimum rubric. |
| Field notes | Preserve learning from failure | Student records what happened, what changed, and the next hypothesis. |

## 7. Technical Foundation: Recommended v0 Architecture

### Architecture principle

Start with a **modular web-app monolith**. One codebase, one deployable application, one primary database. This is easier for interns to collaborate on, fast enough for v0, and simple to observe and improve. Do not build microservices, a custom AI platform, mobile apps, complex real-time features, or a separate analytics warehouse in v0.

### Recommended starting stack

| Layer | Starting choice | Why |
|---|---|---|
| Web application | TypeScript + Next.js | One typed codebase for the student app, staff views, and server-side actions. |
| Database, authentication, storage | Supabase: Postgres, Auth, Storage | Gives the project a relational data model, user access control, file storage, and a realistic production foundation. |
| Deployment | Vercel connected to GitHub | Every pull request can have a preview URL; production releases remain traceable to code. |
| Source control and collaboration | GitHub | Issues, branches, pull requests, reviews, release history, and a single place for technical decisions. |
| AI feedback | Server-side provider adapter, selected after an architecture review | Keeps model/provider logic away from the student interface and allows controlled prompts, logging, and later change. |
| Error and usage observability | Basic structured logs and an error-tracking tool chosen with engineers | Lets the team see failed submissions, broken flows, and critical usage events. |

This is a starting decision, not a command. Professors and engineers should review it against the university's policies, intern capability, budget, privacy expectations, and existing infrastructure.

### System boundaries

```text
Student / reviewer browser
        ↓
Next.js application
  ├─ Student and reviewer interfaces
  ├─ Mission, submission, feedback, and progress logic
  └─ Server-side AI feedback adapter
        ↓
Supabase
  ├─ Auth and roles
  ├─ Postgres course/progress data
  └─ Artifact storage
```

### Core data model

| Entity | Purpose | Minimum fields |
|---|---|---|
| User | Person who signs in | id, name, email, role |
| Role | Access level | student, reviewer, curriculum editor, admin |
| Course | The playable course | id, title, version, status |
| Mission | A learn-act-submit-feedback unit | id, course_id, title, brief, rubric, order, unlock rule |
| Enrollment | Student's relationship to course | user_id, course_id, status, started_at |
| Mission progress | Student state in a mission | enrollment_id, mission_id, state, started_at, completed_at |
| Artifact | Evidence submitted by the student | progress_id, type, content/file, submitted_at, version |
| Feedback | AI or human response to artifact | artifact_id, source, rubric scores, comments, decision |
| Decision log | Why a product or technical decision was made | decision, options, trade-off, owner, date |

### Access rules

- Students can read only their own enrollment, progress, artifacts, and feedback.
- Reviewers can read assigned or approved student submissions and leave feedback.
- Curriculum editors can change mission content, not user records or infrastructure settings.
- Admins manage roles, cohorts, releases, and data exports.
- Every database table exposed to the application needs an explicit access policy. Do not rely on the interface to protect data.

### Production-ready means for v0

Production-ready does not mean infinitely scalable. It means a real person can use the alpha safely and the team can change it without breaking it blindly.

- GitHub repository with a clear README, setup instructions, issue tracker, and ownership.
- `main` branch protected; changes happen through small pull requests with one reviewer where possible.
- Local, preview, and production environments are distinct.
- Automated checks run before merge: formatting, type checks, tests, and build.
- Authentication and role-based access are working before student data is stored.
- Database changes are written as reviewed migrations, never ad-hoc production edits.
- Secrets live in environment variables, never in code or chat.
- The team can see deployment failures and application errors.
- A rollback/recovery owner is named before public alpha access.

### Questions for professors and engineers this week

1. Is this monolith the simplest safe architecture for a 5–10 student alpha with interns?
2. Which existing university systems, privacy rules, or hosting rules constrain auth, student data, or AI feedback?
3. Which data must be relational from day one, and which can remain plain text or files?
4. What is the smallest vertical slice that proves the system end-to-end?
5. Which tests are essential before an alpha, and which are premature?
6. How should the team structure branches, pull requests, reviews, and deployment authority?
7. What security and consent requirements apply before storing student artifacts or sending them to an AI provider?
8. What should be instrumented so we can see activation, submission, feedback, completion, and failure?

## 8. First Operating Team and Intern Hiring

### Initial roles

| Role | Owns | First weekly output |
|---|---|---|
| Product / project lead | Scope, priorities, decisions, acceptance criteria | Updated project board and decision log |
| Curriculum designer | First mission's learning and artifact logic | Mission brief and rubric |
| Interaction / visual designer | Student flow, wireframes, game layer | Annotated screens and interaction states |
| Prototype engineer | Technical foundation and vertical slice | Running preview deployment and implementation notes |
| Research / operations coordinator | Intern process, professor input, resource model | Meeting notes, risks, resource/cost inputs |

One person may cover more than one role in v0. Do not recruit a large team before the first mission, stack, and weekly outputs are clear.

### Hiring sequence

1. Finalise these role briefs and selection criteria.
2. Ask the university for candidates with enough time and a visible sample of work.
3. Give shortlisted candidates a small, relevant paid or time-boxed task where possible.
4. Select for reliability, learning speed, clear communication, and role fit, not enthusiasm alone.
5. Onboard each intern with the project context, role charter, first weekly output, and decision rights.

### Weekly operating cadence

- **Monday, 30 minutes:** priorities, owner, definition of done, dependency.
- **Midweek, 15 minutes:** evidence, blocker, decision needed.
- **Friday, 30 minutes:** demo what changed, record metrics, retrospective, select next constraint.

## 9. v0 Resource and Cost Model

The university paying does not remove the resource-allocation problem. The model teaches Ash to decide what the project is worth doing and what not to fund.

| Cost category | Questions to answer |
|---|---|
| People | What hours does each role need? What does an intern, faculty reviewer, engineer, and coordinator cost? |
| Product build | What is the cost of design, engineering, testing, fixes, and maintenance? |
| Infrastructure | What are the hosting, database, storage, email, domain, analytics, and error-tracking costs at alpha and cohort scale? |
| AI feedback | What prompts/models are used, how many student attempts are expected, and what is the cost per completed mission? |
| Human feedback | Which artifacts require expert review, how long does it take, and what student-to-reviewer ratio is sustainable? |
| Acquisition | How are students recruited, what does each channel cost, and what is the activation rate? |
| Risk reserve | What is the cost if an intern leaves, a service limit is hit, or a student-data issue requires rework? |

The first model should show three cases: **alpha (5–10 students), first cohort, and a larger cohort.** It should state the assumptions clearly rather than pretending the numbers are precise.

## 10. Success Measures

For v0, measure learning and product behaviour, not vanity activity.

- Activation: enrolled students who start the first mission.
- Submission: activated students who submit the required artifact.
- Completion: submitting students who complete or revise the mission successfully.
- Time to completion: how long the mission actually takes.
- Feedback usefulness: student rating plus revision quality.
- Failure points: where students abandon, become confused, or need human help.
- Team reliability: weekly outputs delivered on time with visible evidence.

## 11. Explicit Non-Goals for v0

- A complete multi-phase course.
- Complex animation, points, leaderboards, or a custom 3D world.
- Native mobile apps.
- Multiple separate services or a custom backend platform.
- Full automation of human teaching judgment.
- Large-scale student recruitment before the first learning loop works.

## 12. Decision Gate

Before implementation expands beyond the first mission, Ash, the technical reviewer, and the Udyaan lead must agree that:

- The first mission is understandable and useful to a student.
- The data and access model protects students.
- The architecture is simple enough for the team to maintain.
- The resource model fits the university's actual support.
- The next build has a named owner, definition of done, and review date.
