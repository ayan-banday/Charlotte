# Black Hole for routed build output; Drive for team share

Agent and Manus AI build outputs (PPTX, PDF, slide PNGs, deck scratch) route to **`Black Hole/`** at vault root — one named sink, not root `output/` or unscoped `tmp/`. Gitignore or periodic cleanup inside Black Hole is fine; the rule is *route here*, not *forbid output*.

Finished deliverables promote out of Black Hole to: project markdown folders, `assets/<project>/` for canonical figures, or Google Drive for team-shared files. Link from project intro when on Drive.

Delete legacy `output/`, `tmp/`, `_codex_tmp/` after migration into Black Hole or final homes.
