---
date created: 2026-08-26
date updated: 2026-08-26
---
# Google Drive Artifacts Connector

## Purpose

Describe the connector contract for promoting reviewed files from `Black Hole/<date>-<slug>/` to the team’s Google Drive and linking them from the relevant project introduction.

## Contract

- Input: reviewed artifact path, destination folder, project path, and a short description.
- Action: upload the artifact and return its Drive URL.
- Follow-up: add the approved Drive link to the project introduction or canonical document.
- Safety: keep unreviewed builds in Black Hole; never overwrite canonical files without explicit approval.

## Credential boundary

Ash configures the Google Drive connector in Cursor/Codex. Do not commit OAuth tokens, service-account keys, or private Drive URLs to this vault.
