# ROCKLAND GAMES: find out which machine this is and where the workspace will go.
# Run: right-click > Run with PowerShell (no admin needed). Safe to run as often as you like.
# Writes Docs\MACHINE.md next to this kit (03-create-rockland-games.ps1 copies it into the workspace).
$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "Rockland-Common.ps1")
$m = Get-RocklandMachine

$gpuLines  = $m.Gpus  | ForEach-Object { "| $($_.Name) | $($_.Driver) | $(if ($_.Discrete) { 'yes, run the game on this one' } else { 'no (integrated)' }) |" }
$diskLines = $m.Disks | ForEach-Object { "| $($_.Drive) | $($_.FreeGB) GB free of $($_.SizeGB) GB |" }
$rootDisk  = $m.Disks | Where-Object { $_.Drive -eq (Split-Path -Qualifier $m.Root) }
$warnings  = @()
if ($rootDisk -and $rootDisk.FreeGB -lt 150) { $warnings += "Only $($rootDisk.FreeGB) GB free on $($rootDisk.Drive). Unreal Engine 5.x alone needs about 60 GB plus DerivedDataCache. Free space or plug in an external SSD and run with -Root." }
if ($m.RamGB -lt 16)  { $warnings += "$($m.RamGB) GB RAM. The editor wants 16 GB or more; close everything else while it is open." }
if ($m.Kind -eq "laptop") {
  $warnings += "Laptop: stay plugged in. The GeForce is throttled hard on battery and Unreal will stutter."
  if ($m.Hybrid) { $warnings += "Two GPUs. Step 5 pins UnrealEditor.exe to the GeForce; the packaged CantaKart.exe is pinned in Settings > System > Display > Graphics (see README)." }
}

$md = @"
# This machine

Written by ``scripts\00-detect-machine.ps1`` on $(Get-Date -Format 'yyyy-MM-dd HH:mm').

| | |
|---|---|
| Computer | $($m.Name) ($($m.Model)) |
| Kind | $($m.Kind) |
| CPU | $($m.Cpu) |
| RAM | $($m.RamGB) GB |
| Workspace | ``$($m.Root)`` |
| Unreal Engine and UEFN | ``$($m.EpicDir)`` |
| CANTA KART target | $($m.TargetFps) fps at $($m.TargetRes), Lumen off |

## GPUs

| Name | Driver | Run the game on it |
|------|--------|--------------------|
$($gpuLines -join "`n")

## Fixed drives

| Drive | Space |
|-------|-------|
$($diskLines -join "`n")

## Warnings

$(if ($warnings) { ($warnings | ForEach-Object { "- $_" }) -join "`n" } else { "- none" })
"@

$Kit = Split-Path -Parent $PSScriptRoot
$out = Join-Path $Kit "Docs\MACHINE.md"
Set-Content -Path $out -Value $md -Encoding UTF8
Write-Host $md
Write-Host "Saved to $out"
if ($m.Root -ne "N:\ROCKLAND-GAMES") {
  Write-Host ""
  Write-Host "No N: drive, so this is not the pink GeForce desktop. Workspace will be $($m.Root)."
  Write-Host "Install Unreal Engine and UEFN into $($m.EpicDir) in step 4. To use another drive, run 03 with -Root <drive>:\ROCKLAND-GAMES."
}
Read-Host "Press Enter to close"
