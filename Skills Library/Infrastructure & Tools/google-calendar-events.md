---
date created: 2026-08-26
date updated: 2026-08-26
---
# Google Calendar Commitments Connector

## Purpose

Describe the connector contract for turning an approved deliverable into a Google Calendar event. Calendar remains the commitment store; Obsidian mirrors context and dated work only.

## Contract

- Input: approved proposal, event title, start and end times, project path, and deliverable description.
- Action: create or update one event in Ash’s chosen commitments calendar.
- Description: include the deliverable, expected output, project link, and proposal reference.
- Safety: do not create events from unapproved or ambiguous proposals.

## Credential boundary

Ash configures the Google Calendar API connector and calendar ID in Cursor/Codex. Do not commit tokens, service-account keys, or calendar IDs that Ash has not explicitly made public.
