#!/usr/bin/env bash
# Verify the machine-local Graphify installation used by Charlotte.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v graphify >/dev/null 2>&1; then
  echo "[charlotte-graphify] executable: $(command -v graphify)"
  graphify --version
  exit 0
fi

if command -v python3 >/dev/null 2>&1 && python3 -c 'import graphify_vault' >/dev/null 2>&1; then
  echo "[charlotte-graphify] graphify_vault Python module is installed, but no graphify executable is on PATH."
  echo "[charlotte-graphify] Use the machine’s documented Graphify entry point, then rerun this check."
  exit 0
fi

echo "[charlotte-graphify] Graphify is not available on this machine."
echo "[charlotte-graphify] Install it using Ash’s local setup, then rerun: scripts/check-graphify.sh"
echo "[charlotte-graphify] The sync hook will still rebuild vault-index.json without Graphify."
exit 1
