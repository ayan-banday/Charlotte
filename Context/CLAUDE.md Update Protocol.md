---
date created: 2026-05-02
date updated: 2026-05-02
---

# CLAUDE.md Update Protocol

Automatic system state sync triggered by: **"sync claude.md"**

---

## What This Does

When you say "sync claude.md", I:

1. **Scan current system state**
   - Count all folders, files, projects, skills, workflows
   - Check all introduction files for accuracy
   - Verify indices match actual content

2. **Update File Structure Registry.md**
   - Refresh folder inventory
   - Update file counts
   - Verify all links are correct

3. **Update CLAUDE.md references**
   - Update date in FILE STRUCTURE REGISTRY section
   - Verify trigger table is current
   - Check all rule files still exist

4. **Confirm to you**
   - Show what changed
   - Report any inconsistencies found
   - Ask for approval before making changes

---

## When to Use

Say "sync claude.md" at any of these moments:

- **After adding new projects/skills/workflows**: Keeps registry current
- **After moving or renaming files**: Updates file structure map
- **After session cleanup**: Ensures system is documented
- **End of work day**: Final sync before closing out
- **Weekly or monthly**: Periodic audit of system state

---

## Step-by-Step Protocol

**Step 1: Scan System**
```
- Count /02 Projects/ subfolders
- Count /Skills Library/ skills by domain
- Count /Workflows/ files
- Check all introduction files exist
- Verify all index files match content
```

**Step 2: Check Registry**
```
- Load File Structure Registry.md
- Compare against actual system
- Note any discrepancies
- Update dates and counts
```

**Step 3: Report Findings**
```
- Show what I found
- List any inconsistencies
- Ask: "Should I update the registry and CLAUDE.md?"
- Wait for confirmation
```

**Step 4: Update Files**
```
- Update File Structure Registry.md with current state
- Update CLAUDE.md date_updated field
- Confirm all changes completed
```

---

## Example Execution

**You say:** "sync claude.md"

**I respond:**
```
Scanning system state...

Found:
- 3 active projects
- 66 skills across 4 domains
- 3 active workflows
- All introductions current
- Registry matches actual system

File Structure Registry.md and CLAUDE.md are current. No changes needed.
```

**Or if changes are found:**
```
Scanning system state...

Found:
- 3 active projects (NEW: "How to Write a Newsletter")
- 66 skills (NEW: 3 additional infrastructure skills since last sync)
- Registry counts outdated

Should I update File Structure Registry.md and CLAUDE.md with these changes?
```

---

## Notes

- **Non-destructive**: Only updates dates and counts. Never deletes content.
- **Verification-first**: Always reports findings before making changes. Asks for approval.
- **Full transparency**: Shows you exactly what changed and why.

---

## Trigger Phrase

Add to your workflow:
- End of project work: "sync claude.md"
- After creating new files: "sync claude.md"
- Weekly check-in: "sync claude.md"

That's it. Everything else is automatic.
