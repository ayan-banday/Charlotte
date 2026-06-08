---
date created: 2026-04-29
date updated: 2026-04-29
---

# Prompt Storage Rule

**Triggered by:** "store this prompt", "save this prompt", "record this prompt", or any equivalent phrasing

---

## What Claude Does When Triggered

1. **Identify the domain** the prompt belongs to. Ask if unclear: "Which domain does this prompt belong to? (e.g. Exam Backcasting, Webinars, Email Campaigns, or a new domain?)"

2. **Check if the domain folder exists** in `/Skills Library/`. If it does not exist, create it and create a `00 Introduction to [Domain Name].md` for it.

3. **Name the file.** Use the prompt's own name or heading as the filename. No `[C]` prefix. Just the name. Example: `Prompt 1 - Subject Setup.md`, `System Prompt.md`.

4. **Write the file** to `/Skills Library/[Domain]/[Prompt Name].md`. Include the full prompt content exactly as given. No summarising.

5. **Update `[C] Skills Index.md`** — add the new prompt to the correct domain section with: skill name, what problem it solves, and when to use it.

6. **Update `00 Introduction to Skills Library.md`** — add the new file to the domain's file list in the Structure section. If it is a new domain, add the domain entry under Domains.

7. **Update the relevant project intro file** if the prompt is being used in an active project. Add a Methodology section (or update the existing one) that links to the prompt and explains when to use it.

8. **Confirm to the user:** "Stored. [Prompt Name] is now in Skills Library/[Domain]/. [C] Skills Index and the Skills Library intro are updated. [If project updated: [Project Name] intro also updated.]"

---

## What Good Storage Looks Like

- The prompt file is self-contained. Anyone reading it can run it without needing other context.
- The Skills Index entry tells Claude exactly when to reach for this prompt.
- The project intro makes the connection explicit: "this project uses these prompts."

---

## What to Never Do

- Do not summarise the prompt. Store it in full.
- Do not invent a domain. Ask if the domain is unclear.
- Do not create files without updating the index and intro. All three happen together.
