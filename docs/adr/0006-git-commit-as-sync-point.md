# Git commit is the sync point for agents

When Ash commits (or pushes), a post-commit hook runs `scripts/charlotte-sync.sh`. That rebuilds `vault-index.json`, mirrors human indexes, and runs Graphify `--update` on the curated corpus.

Optional Windows Task Scheduler job at 17:30 local runs the same script for uncommitted work before the 18:00 routing batch.

No separate "watcher app." No filesystem daemon required. Commit = sync.
