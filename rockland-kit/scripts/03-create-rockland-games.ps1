# ROCKLAND GAMES: create N:\ROCKLAND-GAMES, copy the BerbiceWorld project skeleton,
# set up git + LFS, and make the first commit. Never pushes.
# Run: right-click > Run with PowerShell (no admin needed).
$ErrorActionPreference = "Stop"
$Root = "N:\ROCKLAND-GAMES"
$Kit  = Split-Path -Parent $PSScriptRoot   # the rockland-kit folder this script lives in

if (-not (Test-Path "N:\")) { throw "N: drive not found. Plug in or map the N: drive first." }

foreach ($d in "BerbiceWorld","CantaKart","Docs","Source-Art","Builds") {
  New-Item -ItemType Directory -Force -Path (Join-Path $Root $d) | Out-Null
}

# Project skeleton, design docs, report template
Copy-Item -Recurse -Force (Join-Path $Kit "BerbiceWorld\*") (Join-Path $Root "BerbiceWorld")
Copy-Item -Recurse -Force (Join-Path $Kit "CantaKart\*")    (Join-Path $Root "CantaKart")
Copy-Item -Recurse -Force (Join-Path $Kit "Docs\*")         (Join-Path $Root "Docs")
Copy-Item -Force (Join-Path $Kit ".gitignore")     $Root
Copy-Item -Force (Join-Path $Kit ".gitattributes") $Root

# Git + LFS
Set-Location $Root
if (-not (Test-Path ".git")) { git init -b main | Out-Null }
git lfs install --local
git config user.name  "ROCKLAND GAMES"
git config user.email "rockland-games@localhost"
git add -A
if (git status --porcelain) {
  git commit -m "Session 1: ROCKLAND GAMES workspace, BerbiceWorld skeleton, CANTA KART plan" | Out-Null
  Write-Host "Committed. (No push, by rule.)"
} else {
  Write-Host "Nothing new to commit."
}

# Point the project at the newest UE 5.x installed in N:\Epic and generate Visual Studio project files
$Engine = Get-ChildItem "N:\Epic" -Directory -Filter "UE_5.*" -ErrorAction SilentlyContinue |
  Sort-Object { [version]($_.Name -replace '^UE_','') } -Descending | Select-Object -First 1
if ($Engine) {
  $Ver = $Engine.Name -replace '^UE_',''
  $UProject = Join-Path $Root "BerbiceWorld\BerbiceWorld.uproject"
  (Get-Content $UProject -Raw) -replace '"EngineAssociation": "[^"]*"', ('"EngineAssociation": "' + $Ver + '"') | Set-Content $UProject -NoNewline
  git add $UProject; git commit -q -m "Point BerbiceWorld at UE $Ver" 2>$null
  $UBT = Join-Path $Engine.FullName "Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe"
  if (Test-Path $UBT) {
    Write-Host "Generating project files with $($Engine.Name)..."
    & $UBT -projectfiles -project="$UProject" -game -rocket -progress
    Write-Host "Open $UProject to build the editor module."
  }
} else {
  Write-Host "No engine found in N:\Epic yet. Install UE 5.x there, then run this script again."
}
Write-Host "N:\ROCKLAND-GAMES is ready."
