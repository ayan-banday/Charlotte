---
date created: 2026-08-11
date updated: 2026-08-17 — Made graph-grounded retrieval the default for vault and project questions.
---

# Agent Instructions

## Primary instruction file

Read and follow [`CLAUDE.md`](./CLAUDE.md) first. It is the primary instruction file for this vault and governs navigation, naming, linking, memory, and change-management conventions.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

### Charlotte vault graph

This is a markdown knowledge vault, not a codebase. Its authoritative local graph is rebuilt with `graphify extract .`, which respects the durable-vault scope in `.graphifyignore`. The generated graph lives in `graphify-out/`; use `graphify-out/graph.html` for interactive inspection and `graphify-out/GRAPH_REPORT.md` for the current measurable coverage.

For a relationship between vault documents, use `graphify path "A" "B" --graph graphify-out/graph.json`; then open the returned source notes to verify the relationship. `references` and `mentions` are literal, extracted relationships, never semantic claims.

### Default vault-answer protocol

For any non-trivial question about a project, goal, plan, decision, person, or pattern in this vault:

1. Rebuild with `graphify extract .` if the graph predates relevant edits.
2. Run `graphify query "<topic>" --graph graphify-out/graph.json`, then use `path` for the claimed connection and `explain` for a focal note when useful.
3. Open the primary note, direct linked notes, and the newer strategic note. Prefer newer source-of-truth documents when they conflict.
4. Answer in four parts: what is real, what changed or conflicts, the current constraint, and the next decision.

Skip this only for simple requests that do not depend on vault context. Never treat graph edges themselves as strategy, intent, or truth.
