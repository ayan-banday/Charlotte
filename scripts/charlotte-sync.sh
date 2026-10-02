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
  # extract handles markdown changes; update is AST-only. .graphifyignore
  # defines the durable-vault scope for CLI and agent-driven extraction.
  if graphify extract "$ROOT"; then
    rm -f "$ROOT/graphify-out/.needs_update"
  else
    mkdir -p "$ROOT/graphify-out"
    touch "$ROOT/graphify-out/.needs_update"
    echo "[charlotte-sync] Graph rebuild pending; run the Graphify skill to refresh changed notes" >&2
  fi
else
  mkdir -p "$ROOT/graphify-out"
  touch "$ROOT/graphify-out/.needs_update"
  echo "[charlotte-sync] Graphify CLI not installed; graph rebuild pending" >&2
fi

echo "[charlotte-sync] done"
