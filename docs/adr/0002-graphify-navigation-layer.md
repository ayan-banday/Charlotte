# Graphify as agent navigation layer

Agents must not grep the full vault or load File Structure Registry + every intro file per session. Graphify indexes a curated corpus and exposes `graph.json` for query/path/explain.

v1 corpus: `02 Projects/`, `Skills Library/`, `Workflows/`, `System/`, `Context/`. Exclude `Black Hole/`, `tmp/`, `output/`, `_codex_tmp/`, `node_modules/`, build scratch.

Incremental `--update` on file changes. Vault markdown remains human-readable source of truth; the graph is the machine index.
