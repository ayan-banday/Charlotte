# Sync local Obsidian vault (S:\charlotte) from GitHub main.
# Run in PowerShell:  cd S:\charlotte; .\scripts\sync-vault.ps1

$ErrorActionPreference = "Stop"
$VaultPath = if ($args[0]) { $args[0] } else { "S:\charlotte" }

if (-not (Test-Path $VaultPath)) {
    Write-Host "Vault not found at $VaultPath"
    Write-Host "Clone first: git clone https://github.com/ayan-banday/Charlotte.git S:\charlotte"
    exit 1
}

Set-Location $VaultPath

if (-not (Test-Path ".git")) {
    Write-Host "Not a git repo. Clone: git clone https://github.com/ayan-banday/Charlotte.git S:\charlotte"
    exit 1
}

Write-Host "Pulling latest from origin/main..."
git fetch origin main
git checkout main
git pull origin main

$plan = "02 Projects\Udyaan\[C] Udyaan Developmental Plan.md"
if (Test-Path -LiteralPath $plan) {
    Write-Host "OK — Developmental Plan synced:"
    Write-Host "  $VaultPath\$plan"
} else {
    Write-Host "WARN — file still missing after pull. Check remote:"
    git log --oneline -3
    exit 1
}
