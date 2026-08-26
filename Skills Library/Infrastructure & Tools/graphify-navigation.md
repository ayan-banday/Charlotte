---
date created: 2026-08-26
date updated: 2026-08-26
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
graphify --version
```

If the command is unavailable, install Graphify using Ash’s existing machine-specific method, then rerun the check. The repository does not vendor the executable, Python package, cache, or generated graph because those are environment-specific and can be large. The handoff currently names `graphify-vault` as the Python package fallback; confirm the exact package/CLI name on the target machine before installing.

## Update

The Git post-commit hook runs:

```bash
scripts/charlotte-sync.sh
```

That script always rebuilds `vault-index.json`. When `graphify` is available on the local `PATH`, it also runs an incremental update over the canonical corpus. When it is unavailable, the index still refreshes and the hook reports the missing optional dependency.

## Query patterns

Use path-first queries such as:

```text
/graphify query "Udyaan newsletter skills"
/graphify query "project name key workflows"
/graphify query "current workflow for [trigger]"
```

Return paths and short relevance context first. Read only the project introduction, one workflow, and the smallest relevant skill chain. Do not bulk-read the Registry or the entire Skills Library when the index and graph can narrow the search.

## Ownership boundary

Git owns the sync hook, corpus rules, query conventions, and `vault-index.json`. Each local machine owns the Graphify installation and its generated `.graphify/graph.json`. Do not add Graphify credentials or machine-specific installation paths to the repository.
