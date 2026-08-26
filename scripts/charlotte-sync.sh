#!/usr/bin/env bash
# Charlotte vault sync — run on git commit (and optional 5:30pm scheduled task).
# Regenerates vault-index.json, mirrors Projects Index, incremental Graphify update.
#
# Install: git config core.hooksPath .githooks
# Manus: implement Python indexer; this shell stub documents the contract.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "[charlotte-sync] $(date -Iseconds)"

# TODO (Manus): replace with scripts/charlotte_index.py
if command -v python3 >/dev/null 2>&1 && [[ -f "$ROOT/scripts/charlotte_index.py" ]]; then
  python3 "$ROOT/scripts/charlotte_index.py"
else
  echo "[charlotte-sync] charlotte_index.py not installed — skip index rebuild"
fi

# Incremental Graphify update (curated corpus v1)
if command -v graphify >/dev/null 2>&1; then
  graphify "$ROOT" --update \
    --include "02 Projects" \
    --include "Skills Library" \
    --include "Workflows" \
    --include "System" \
    --include "Context" \
    || echo "[charlotte-sync] graphify --update failed (non-fatal)"
elif command -v python3 >/dev/null 2>&1 && python3 -c "import graphify_vault" 2>/dev/null; then
  echo "[charlotte-sync] run graphify --update manually if graphify CLI name differs"
fi

echo "[charlotte-sync] done"
