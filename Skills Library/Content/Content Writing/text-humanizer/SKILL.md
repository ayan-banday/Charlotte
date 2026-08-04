---
name: text-humanizer
description: Remove signs of AI-generated writing from text. Detects and fixes inflated symbolism, promotional language, superficial -ing analyses, vague attributions, em dash overuse, rule of three, AI vocabulary, negative parallelisms, and filler hedging. Use when editing or reviewing text to sound natural, before publishing newsletters or copy, or when the user asks to humanize text.
version: 2.2.0
---

# Text Humanizer

Remove signs of AI-generated writing. Based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## Workflow

When given text to humanize:

1. **Scan** for patterns in [reference.md](reference.md) (24 patterns across content, language, style, communication, and filler)
2. **Rewrite** problematic sections. Preserve meaning. Match intended tone.
3. **Add soul** — sterile "clean" text is still obviously AI. Vary rhythm, allow opinions, use "I" when appropriate, let some mess in.
4. **Draft** the humanized version
5. **Audit** — ask: "What makes the below so obviously AI generated?" Answer briefly with remaining tells.
6. **Final pass** — revise again to remove those tells
7. **Deliver** output per format below

## Adding Voice (Not Just Removing Patterns)

Signs of soulless writing even when technically clean:
- Every sentence same length/structure
- No opinions, uncertainty, or first-person when appropriate
- Reads like Wikipedia or a press release

Fix it:
- **Have opinions** — react to facts, don't just report
- **Vary rhythm** — short punches, then longer sentences
- **Acknowledge complexity** — mixed feelings beat neutral lists
- **Be specific about feelings** — not "concerning" but what exactly unsettles you

## Output Format

Provide:

1. **Draft rewrite**
2. **"What makes the below so obviously AI generated?"** — brief bullets on remaining tells
3. **Final rewrite** — revised after the audit
4. **Summary of changes** (optional, if helpful)

## Pattern Reference

All 24 patterns with before/after examples: [reference.md](reference.md)

Quick scan list:

| Category | Patterns |
|---|---|
| Content | Significance inflation, notability name-dropping, superficial -ing, promotional language, vague attributions, formulaic challenges sections |
| Language | AI vocabulary, copula avoidance, negative parallelisms, rule of three, synonym cycling, false ranges |
| Style | Em dash overuse, boldface overuse, inline-header lists, title case headings, emojis, curly quotes |
| Communication | Chatbot artifacts, knowledge-cutoff disclaimers, sycophantic tone |
| Filler | Filler phrases, excessive hedging, generic positive conclusions |

## Quality Checks

Revised text should:
- Sound natural read aloud
- Vary sentence structure naturally
- Use specific details over vague claims
- Use simple constructions (`is`/`are`/`has`) where appropriate
- Maintain appropriate tone for context

## Full Example

See [reference.md](reference.md#full-example) for a complete before → draft → audit → final walkthrough.
