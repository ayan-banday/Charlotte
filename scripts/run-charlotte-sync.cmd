@echo off
setlocal
REM Charlotte sync — run from Task Scheduler at 17:30 or manually on Windows.
REM The first argument may override the vault path; default is the script's parent.
set "VAULT=%~1"
if not defined VAULT set "VAULT=%~dp0.."
for %%I in ("%VAULT%") do set "VAULT=%%~fI"

where bash >nul 2>&1
if errorlevel 1 (
  echo charlotte-sync: Git Bash is required to run scripts\charlotte-sync.sh
  exit /b 1
)

cd /d "%VAULT%"
bash "%VAULT%\scripts\charlotte-sync.sh"
exit /b %errorlevel%
