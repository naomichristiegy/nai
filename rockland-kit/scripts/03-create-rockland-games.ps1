# ROCKLAND GAMES: create the workspace, copy the BerbiceWorld project skeleton,
# set up git + LFS, and make the first commit. Never pushes.
# Run: right-click > Run with PowerShell (no admin needed).
# Desktop: N:\ROCKLAND-GAMES. Laptop: the data drive or C:, see Get-RocklandRoot. Override: -Root D:\ROCKLAND-GAMES
param([string]$Root)
$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "Rockland-Common.ps1")
$Root    = Get-RocklandRoot -Override $Root
$EpicDir = Get-RocklandEpicDir $Root
$Kit     = Split-Path -Parent $PSScriptRoot   # the rockland-kit folder this script lives in
$Drive   = Split-Path -Qualifier $Root

if (-not (Test-Path "$Drive\")) { throw "$Drive drive not found. Plug it in or run again with -Root <drive>:\ROCKLAND-GAMES." }
Write-Host "Workspace: $Root   Engine folder: $EpicDir   ($(if (Test-RocklandLaptop) { 'laptop' } else { 'desktop' }))"

foreach ($d in "BerbiceWorld","CantaKart","Docs","Source-Art","Builds") {
  New-Item -ItemType Directory -Force -Path (Join-Path $Root $d) | Out-Null
}

# Project skeleton, design docs, report template, machine sheet (if 00-detect-machine.ps1 ran)
Copy-Item -Recurse -Force (Join-Path $Kit "BerbiceWorld\*") (Join-Path $Root "BerbiceWorld")
Copy-Item -Recurse -Force (Join-Path $Kit "CantaKart\*")    (Join-Path $Root "CantaKart")
Copy-Item -Recurse -Force (Join-Path $Kit "Docs\*")         (Join-Path $Root "Docs")
Copy-Item -Force (Join-Path $Kit ".gitignore")     $Root
Copy-Item -Force (Join-Path $Kit ".gitattributes") $Root

# Packaged builds stage into <Root>\Builds on whichever drive this machine uses
$GameIni = Join-Path $Root "BerbiceWorld\Config\DefaultGame.ini"
$Staging = ($Root -replace '\\','/') + "/Builds"
(Get-Content $GameIni -Raw) -replace 'StagingDirectory=\(Path="[^"]*"\)', ('StagingDirectory=(Path="' + $Staging + '")') | Set-Content $GameIni -NoNewline

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

# Point the project at the newest UE 5.x installed and generate Visual Studio project files
$Engine = Find-RocklandEngine -EpicDir $EpicDir
if ($Engine) {
  $Ver = $Engine.Name -replace '^UE_',''
  $UProject = Join-Path $Root "BerbiceWorld\BerbiceWorld.uproject"
  (Get-Content $UProject -Raw) -replace '"EngineAssociation": "[^"]*"', ('"EngineAssociation": "' + $Ver + '"') | Set-Content $UProject -NoNewline
  git add $UProject; git commit -q -m "Point BerbiceWorld at UE $Ver" 2>$null

  # Laptop with integrated + GeForce: make Windows run the editor on the GeForce (per-user setting, no admin).
  $Editor = Join-Path $Engine.FullName "Engine\Binaries\Win64\UnrealEditor.exe"
  if ((Test-RocklandLaptop) -and (Test-Path $Editor)) {
    $Key = "HKCU:\Software\Microsoft\DirectX\UserGpuPreferences"
    New-Item -Path $Key -Force | Out-Null
    Set-ItemProperty -Path $Key -Name $Editor -Value "GpuPreference=2;"
    Write-Host "UnrealEditor.exe pinned to the high-performance GPU (Settings > System > Display > Graphics)."
  }

  $UBT = Join-Path $Engine.FullName "Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe"
  if (Test-Path $UBT) {
    Write-Host "Generating project files with $($Engine.Name)..."
    & $UBT -projectfiles -project="$UProject" -game -rocket -progress
    Write-Host "Open $UProject to build the editor module."
  }
} else {
  Write-Host "No engine found in $EpicDir (or C:\Program Files\Epic Games) yet. Install UE 5.x there, then run this script again."
}
Write-Host "$Root is ready."
