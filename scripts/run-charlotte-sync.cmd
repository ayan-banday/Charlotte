@echo off
REM Charlotte sync — run from Task Scheduler at 17:30 or manually on Windows.
cd /d S:\Charlotte
bash scripts/charlotte-sync.sh
if errorlevel 1 (
  REM Fallback if Git Bash not in PATH — Manus: implement charlotte_index.py + python call here
  echo charlotte-sync: see scripts/charlotte-sync.sh
)
