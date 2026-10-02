#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/scripts" "$TMP/.githooks" "$TMP/02 Projects/Dummy"
cp "$ROOT/scripts/charlotte_index.py" "$TMP/scripts/charlotte_index.py"
cp "$ROOT/scripts/charlotte-sync.sh" "$TMP/scripts/charlotte-sync.sh"
cp "$ROOT/.githooks/post-commit" "$TMP/.githooks/post-commit"
chmod +x "$TMP/scripts/charlotte-sync.sh" "$TMP/.githooks/post-commit"
mkdir -p "$TMP/bin"
cat > "$TMP/bin/graphify" <<'EOF'
#!/usr/bin/env bash
printf '%s\n' "$1" > graphify-command.txt
exit 17
EOF
chmod +x "$TMP/bin/graphify"
export PATH="$TMP/bin:$PATH"
cat > "$TMP/02 Projects/Dummy/00 Introduction to Dummy.md" <<'EOF'
# Dummy
**Status:** Active
## Key Workflows
- [[Write a Newsletter]]
EOF
cat > "$TMP/02 Projects/Dummy/01 Brain Dump for Dummy.md" <<'EOF'
# Brain Dump for Dummy
EOF
cat > "$TMP/Workflows-placeholder" <<'EOF'
EOF

cd "$TMP"
git init -q
git config user.email test@example.invalid
git config user.name "Charlotte Test"
git config core.hooksPath .githooks
git add .
git commit -qm "acceptance: add dummy project"
test "$(cat graphify-command.txt)" = extract
test -f graphify-out/.needs_update
python3 - "$TMP/vault-index.json" <<'PY'
import json
import sys
from pathlib import Path

index = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
assert any(project["name"] == "Dummy" for project in index["projects"])
PY
printf '%s\n' "sync hook acceptance passed"

# A successful rebuild clears the pending marker.
cat > "$TMP/bin/graphify" <<'EOF'
#!/usr/bin/env bash
printf '%s\n' "$1" > graphify-command.txt
exit 0
EOF
"$TMP/scripts/charlotte-sync.sh"
test "$(cat graphify-command.txt)" = extract
test ! -f graphify-out/.needs_update
printf '%s\n' "graph refresh success/failure checks passed"
