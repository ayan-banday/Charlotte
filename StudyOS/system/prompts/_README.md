# Prompts — the live entry points

These are the **conversational entry points** the coach uses. They drive the flow (ask the student,
research, present options, generate outputs); the **playbooks** hold the deterministic mechanics they
reference, and **`spec.md`** holds the definitions. You don't run these yourself — Claude follows
them.

| Prompt | When it fires | Pairs with |
|---|---|---|
| `00_default_behavior.md` | Always in force — standing behavior + formatting rules | every session |
| `01_course_guide_prompt.md` | Building a `course_guide.md` (once per course) | `playbooks/01_build_guides.md` |
| `02_topic_session_prompt.md` | Every topic study session (topic guide → clusters → questions → tracking) | `playbooks/01`–`04` |

**Also drop here, if you have it:** a **gold-standard example guide** from a course you've already
built well, as the quality bar — `playbooks/01_build_guides.md` reads it first and matches its depth,
structure, and tone when building any new course guide.

**Does NOT go here:** raw course materials (those go in `inputs/`) or anything Claude generates
(guides, clusters, gaps).
