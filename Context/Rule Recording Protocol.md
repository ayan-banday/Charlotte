---
date created: 2026-04-29
date updated: 2026-04-29
---

# Rule Recording Protocol

**Triggered by:** "record this rule", "remember this rule", "save this rule", "add this rule", or any equivalent phrasing

---

## What Claude Does When Triggered

1. **Name the rule.** Use a short, specific descriptive name. Format: `[Rule Name].md`. Example: `Tone Rules.md`, `Backlog Update Rules.md`.

2. **Write the rule to `/Context/[Rule Name].md`**. Include the full rule as stated. Be precise. No padding.

3. **Add a trigger to CLAUDE.md.** In the Rules Triggers section of CLAUDE.md, add one line:
   `When [trigger condition]: read /Context/[Rule Name].md`

   Keep it tight. The trigger is the condition that fires the rule, nothing else.

4. **Do not put the rule content in CLAUDE.md.** CLAUDE.md holds the trigger only. The rule itself lives in `/Context/`.

5. **Confirm to the user:** "Rule recorded. Saved to /Context/[Rule Name].md. Trigger added to CLAUDE.md."

---

## The Meta-Rule (This Protocol Is Its Own Example)

This protocol is itself a rule recorded in `/Context/`. CLAUDE.md points here. The rule content never lives in CLAUDE.md.

This keeps CLAUDE.md lean. Rules accumulate in `/Context/` where they can be updated, versioned, and read on demand, without bloating the main context file.

---

## What a Good Rule File Looks Like

- Short filename that describes the rule domain exactly
- The rule stated directly — what Claude does, when, and how
- No invented content. Only what was given.

---

## What to Never Do

- Do not add rule content to CLAUDE.md. Triggers only.
- Do not merge two unrelated rules into one file. One rule domain per file.
- Do not invent trigger conditions. Use what was stated or ask for clarification.
