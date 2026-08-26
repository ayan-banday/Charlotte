#!/usr/bin/env bash
# Charlotte vault sync: rebuild the machine index after a git commit.
# Graphify is an optional local dependency; the index remains useful without it.
#
# Install: git config core.hooksPath .githooks

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[charlotte-sync] $(date -Iseconds)"

if ! command -v python3 >/dev/null 2>&1; then
  echo "[charlotte-sync] ERROR: python3 is required to rebuild vault-index.json" >&2
  exit 1
fi

python3 "$ROOT/scripts/charlotte_index.py" "$ROOT"

if command -v graphify >/dev/null 2>&1; then
  graphify "$ROOT" --update \
    --include "02 Projects" \
    --include "Skills Library" \
    --include "Workflows" \
    --include "System" \
    --include "Context"
else
  echo "[charlotte-sync] Graphify CLI not installed; skipped semantic graph update" >&2
fi

echo "[charlotte-sync] done"
