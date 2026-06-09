# CLAUDE.md

This file is the Claude Code entry point. It is deliberately thin and the *only* tool-locked file — everything portable lives in the vault so Charlotte can move to any AI tool.

## Bootstrap (every session, before responding)
Read, in order:
1. **`AIOS/MI.md`** — the operating contract (who you are, how to work, the memory engine, the save rule).
2. **`System/MEMORY.md`** — `## Facts` + `## Profile`.
3. **`System/SOUL.md`** — the voice.

That is the whole always-on tier. The maps (`AIOS/Vault Map.md`, `AIOS/Skill Map.md`) and procedures (`ATLAS/Protocols.md`) load on demand. Follow MI.md from there.

## Harness specifics (Claude Code / Windows only)
- **Scheduled capture:** `run-que.cmd` runs daily at 21:00 via Windows Task Scheduler → executes `ATLAS/Workflows/Route Capture.md` against the Notion "The Que" DB. Also manual on "process the que".
- **MCP:** Notion (full), Gmail / Calendar / Fathom (read-only) are allowlisted in `.claude/settings.local.json`.
- **Git:** the vault is a git repo; every change is revertible. Commit when Ash asks.

Swap Claude Code for another tool later → only this file and the `.cmd` scripts change.
