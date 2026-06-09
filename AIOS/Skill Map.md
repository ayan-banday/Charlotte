---
date created: 2026-06-09
date updated: 2026-06-09
loaded: on demand (when a task might need a skill)
purpose: What skills exist, what each solves, when to use it. The single interface to ATLAS/Skills/.
---

# Skill Map

Skills live in `ATLAS/Skills/[Domain]/`. This is the interface — reach for a skill by what it does, not by walking the folder tree. **Workflows** (in `ATLAS/Workflows/`) are named *systems* that chain several skills toward a complete outcome.

## Systems (workflows — multi-skill sequences)
- **Launch a Webinar Funnel** → webinar-planning → hook → intro → value → transition → close.
- **Build an Email Campaign** → campaign-strategy → content-mining → email-brief → email-writer.
- **Design a Welcome Sequence** → campaign-strategy → welcome-sequence.
- **Write a Newsletter** → newsletter-writing-system → content-hook-research → draft in `ash-newsletter-voice` → text-humanizer → newsletter-image-generator.
- **Route Capture** → sort captured input (Notion Que or Dispatch) to its home. See Protocols.

## Marketing
**Sales & Conversion Copy**
- `direct-response-copy` — persuasive direct-response copy. When: conversion-focused offers/promos.
- `vsl-generator` — structured VSL scripts *(bundle)*. When: planning/drafting a video sales letter.
- `email-campaign-writer` — full campaigns, strategy→brief→writing *(bundle)*. When: campaign-level email assets.
- `email-sequence` — multi-email sequences *(bundle)*. When: welcome/nurture/conversion sequences.
- `newsletter-writing-system` — repeatable newsletter drafts *(bundle)*. When: newsletters tied to a sales narrative.
- `jani-insight-email` — insight → personalized email. When: insight-driven emails in Jani (client) context.
- `jani-voice` — Jani's voice/cadence *(bundle)*. When: output must sound like Jani.

**Webinar Architecture**
- `webinar-planning` / `-hook` / `-intro` / `-value` / `-transition` / `-close` — the webinar build, in order. When: building a webinar (use via the Launch a Webinar Funnel system).

## Content
**Content Writing**
- `long-form-content` — deep educational long-form. When: essays, long scripts, deep posts.
- `short-form-content` — concise social copy. When: reels captions, short posts, snippets.
- `storytelling` — narrative-driven communication. When: content needs emotional resonance.
- `text-humanizer` — strip AI tells *(bundle)*. When: before publishing, when copy sounds robotic.
- `voice-correct` — turn voice mismatches into better rules. When: edits made to fix tone/style.

**Content Production**
- `raw-cut` — rapid first-pass video edits *(bundle, scripts)*. When: an initial edit from raw footage.
- `instagram-carousel-generator` — carousel slides in your style. When: turning ideas into carousels.
- `newsletter-image-generator` — newsletter visuals. When: a newsletter needs custom imagery.
- `jani-reels-voice` — reels scripts in Jani voice. When: scripting Jani reels/talking-head.
- `video-use` — practical video deployment *(bundle, helpers)*. When: planning video usage/distribution.
- `manim-video` — animated technical explainers. When: teaching concepts with animated visuals.

**Content Ideation & Strategy**
- `content-mining` — extract stories/proof/mechanisms. When: before writing campaigns or long-form.
- `newsletter-ideas-generator` — angles from audience context. When: planning next newsletter topics.
- `content-hook-research` — research real high-performing hooks. When: before drafting emails/posts/reels/webinars.
- `thought-collector` — capture on-the-go ideas. When: collecting random ideas as they come.

## Learning & Education Systems
- `exam-backcasting-system` — reverse-engineer exam outcomes into plans. When: serious exam prep.
- `learning-study-coach` — adaptive day-to-day study coaching. When: focused study blocks.
- `book-to-textbook-converter` — books → structured resources. When: dense/unstructured source material.

## Ashes Voices (Ash's writing voice — not Charlotte's)
- `ash-newsletter-voice` — peer voice, crisis-as-proof, named frameworks. When: writing newsletter content.
- `ash-substack-voice` — direct, opinion-driven, shorter-form. When: Substack / shorter thought-leadership.

## Infrastructure & Tools
- `chronicler` — save a conversation/transcript verbatim with a summary on top. When: Ash says "save this verbatim" (never auto).
- `rock-tumbler` — sharpen Ash's draft/idea by open questions only, never drafts it. When: "tumble this" (runs in the Tumbler voice).
- `skill-creator` — author a new skill (correct structure/metadata). When: adding a reusable skill.
- `project-creator` — initialize a project workspace. When: starting a new project.
- `task-scheduler` — schedule recurring/timeline tasks. When: planning repeatable execution.
- `document-docx-editor` / `-pdf-editor` / `-pptx-editor` / `-xlsx-editor` — edit Office/PDF files. When: working with that file type.
- `system-help` — operational troubleshooting. When: system/tool usage is unclear.

## Adding a skill
Author with `skill-creator` into `ATLAS/Skills/[Domain]/`, then add one line here. That's the whole registration.
