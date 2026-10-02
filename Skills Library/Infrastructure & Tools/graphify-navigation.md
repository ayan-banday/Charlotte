---
date created: 2026-08-26
date updated: 2026-10-02 — Corrected markdown rebuild command and documented agent extraction without API keys.
---
# Graphify Navigation

## Purpose

Use Graphify as Charlotte’s semantic navigation layer. It finds the smallest useful set of vault paths before an agent reads file bodies. Git stores the integration scripts and documentation; Graphify itself remains installed on each machine that runs Charlotte.

## Canonical corpus

Index only these paths:

- `02 Projects/`
- `Skills Library/`
- `Workflows/`
- `System/`
- `Context/`

Exclude `Black Hole/`, `output/`, `tmp/`, `_codex_tmp/`, `node_modules/`, and `.graphify/cache/`.

## Setup on a machine

From the repository root, verify the local executable:

```bash
graphify --help
```

If the command is unavailable, install Graphify using Ash’s existing machine-specific method, then rerun the check. The repository does not vendor the executable, Python package, cache, or generated graph because those are environment-specific and can be large. The handoff currently names `graphify-vault` as the Python package fallback; confirm the exact package/CLI name on the target machine before installing.

## Update

The Git post-commit hook runs:

```bash
scripts/charlotte-sync.sh
```

That script always rebuilds `vault-index.json`. When `graphify` is available on the local `PATH`, it runs `graphify extract "$ROOT"`. This incrementally re-extracts changed notes using `.graphifyignore`; `graphify update` only refreshes code through AST extraction and cannot refresh this markdown vault. When extraction fails or Graphify is unavailable, the index still refreshes and the hook marks `graphify-out/.needs_update`.

Headless semantic extraction needs a configured backend. Without an API key, use the installed Graphify skill's agent extraction workflow: extract changed notes, merge them with the saved extraction, then rebuild the graph, report, and HTML. Keep unchanged sources, replace changed-source fragments, and stamp only successfully extracted files in the manifest. A pending marker is cleared only after a verified refresh.

Verify that exported nodes retain `label` and `source_file`, check changed-note coverage, and smoke-test `query`, `path`, and `explain`. Extracted `references` and `mentions` must come from literal source evidence; inferred connections remain explicitly labelled and require verification in the notes.

## Query patterns

Use path-first queries such as:

```text
/graphify query "Udyaan newsletter skills"
/graphify query "project name key workflows"
/graphify query "current workflow for [trigger]"
```

Return paths and short relevance context first. Read only the project introduction, one workflow, and the smallest relevant skill chain. Do not bulk-read the Registry or the entire Skills Library when the index and graph can narrow the search.

## Ownership boundary

Git owns the sync hook, corpus rules, query conventions, and `vault-index.json`. Each local machine owns the Graphify installation and its generated `graphify-out/graph.json`. Do not add Graphify credentials or machine-specific installation paths to the repository.
