# Charlotte Vault

Ash's agent-operated knowledge vault. Markdown source of truth. Graphify for agent navigation. Obsidian for human workspace. IDE for execution.

## Language

**Vault**:
The git-backed markdown repository (`Charlotte`). Canonical storage for skills, workflows, brain dumps, week files, and system memory. Not a dump folder for build artifacts.

_Avoid_: database, second brain (as product name)

**Capture Queue**:
Raw inbound thoughts before routing. Telegram is primary. Items land here first; nothing is filed until the evening batch proposes destinations.

_Avoid_: inbox, dispatch (as permanent home)

**Routing Batch**:
The ~6pm job that classifies Capture Queue items, proposes routes and calendar events, and waits for human approval. Nothing auto-commits.

_Avoid_: sync, auto-route

**Proposal**:
A suggested action from the Routing Batch: route this capture to X, add this calendar event, skip this item. Preserved in vault log until approved or rejected.

_Avoid_: suggestion, recommendation (in automation context)

**Commitment**:
A human-approved deliverable with a time window. Stored as a Google Calendar event (not a task list). One event = one deliverable + deadline.

_Avoid_: task, todo (as system primitives)

**Week File**:
The sole reflection surface: `00 Self-Management/Weeks/Week [ISO].md`. Updated after reflection in IDE, not via daily notes.

_Avoid_: daily log, journal

**Graph Corpus**:
The curated subset of vault folders indexed by Graphify for agent navigation. Agents query `graph.json` instead of grepping markdown.

_Avoid_: manifest, registry (for machine index)

**Vault Index**:
Machine-readable `vault-index.json` at repo root. Lists projects (paths, workflows, brain dumps), workflow triggers, skill paths. Rebuilt on every git commit. Agents read this instead of File Structure Registry.

_Avoid_: scanning all markdown folders each session

**Black Hole**:
The single routed sink for agent build output (decks, PDFs, exports, scratch). Manus AI and IDE agents write here; the evening batch or manual tidy moves finished pieces to project folders, Drive, or delete. One entropy bucket, not scattered `output/` / `tmp/`.

_Avoid_: output, tmp, dump folder

**Work Artifact**:
A finished deliverable tied to a project. Lives in `02 Projects/<Project>/`, Google Drive (team), or `assets/` (canonical figures). Raw builds land in Black Hole first; promotion out is explicit.

_Avoid_: build folder (unscoped)

**Skill**:
A reusable agent instruction file. Vault skills live in `Skills Library/`. Agent slash-command skills live in `.agents/skills/`. Do not duplicate bodies across both.

_Avoid_: prompt, rule (when referring to skill files)
