# ROCKLAND GAMES: shared helpers for the kit scripts. Dot-source this file; do not run it.
#   . (Join-Path $PSScriptRoot "Rockland-Common.ps1")
# Works on both machines: the pink GeForce desktop (N: drive) and the MSI laptop (no N: drive).

function Test-RocklandLaptop {
  # A battery means a laptop. The desktop has none.
  return [bool](Get-CimInstance Win32_Battery -ErrorAction SilentlyContinue)
}

function Get-RocklandRoot {
  # Where N:\ROCKLAND-GAMES lives on this machine, in this order of preference:
  #   1. -Root argument            2. ROCKLAND_ROOT environment variable
  #   3. N:\ROCKLAND-GAMES         (pink GeForce desktop)
  #   4. <data drive>:\ROCKLAND-GAMES  (laptop: the fixed non-C: drive with the most free space, if it has 150 GB free)
  #   5. C:\ROCKLAND-GAMES         (laptop with a single drive)
  param([string]$Override)
  if ($Override)          { return $Override.TrimEnd('\') }
  if ($env:ROCKLAND_ROOT) { return $env:ROCKLAND_ROOT.TrimEnd('\') }
  if (Test-Path "N:\")    { return "N:\ROCKLAND-GAMES" }
  $data = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
    Where-Object { $_.DeviceID -ne "C:" } | Sort-Object FreeSpace -Descending | Select-Object -First 1
  if ($data -and $data.FreeSpace -ge 150GB) { return "$($data.DeviceID)\ROCKLAND-GAMES" }
  return "C:\ROCKLAND-GAMES"
}

function Get-RocklandEpicDir {
  # Unreal Engine and UEFN go next to the workspace, on the same drive: N:\Epic, D:\Epic, or C:\Epic.
  param([Parameter(Mandatory)][string]$Root)
  return (Join-Path (Split-Path -Qualifier $Root) "Epic")
}

function Find-RocklandEngine {
  # Newest UE 5.x install. Looks in <drive>:\Epic first, then where the Epic Games Launcher installs by default.
  param([Parameter(Mandatory)][string]$EpicDir)
  $places = @($EpicDir, "C:\Program Files\Epic Games") | Where-Object { Test-Path $_ }
  return $places | ForEach-Object { Get-ChildItem $_ -Directory -Filter "UE_5.*" -ErrorAction SilentlyContinue } |
    Sort-Object { [version]($_.Name -replace '^UE_','') } -Descending | Select-Object -First 1
}

function Get-RocklandMachine {
  # One object describing this PC. Used by 00-detect-machine.ps1 and written to Docs\MACHINE.md.
  $cs   = Get-CimInstance Win32_ComputerSystem
  $cpu  = Get-CimInstance Win32_Processor | Select-Object -First 1
  $gpus = Get-CimInstance Win32_VideoController | ForEach-Object {
    [pscustomobject]@{ Name = $_.Name; Driver = $_.DriverVersion; Discrete = ($_.Name -match 'GeForce|RTX|Radeon RX') }
  }
  $disks = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" | ForEach-Object {
    [pscustomobject]@{ Drive = $_.DeviceID; FreeGB = [math]::Round($_.FreeSpace / 1GB); SizeGB = [math]::Round($_.Size / 1GB) }
  }
  $laptop = Test-RocklandLaptop
  $root   = Get-RocklandRoot
  [pscustomobject]@{
    Name        = $env:COMPUTERNAME
    Model       = "$($cs.Manufacturer) $($cs.Model)".Trim()
    Kind        = $(if ($laptop) { "laptop" } else { "desktop" })
    Cpu         = $cpu.Name.Trim()
    RamGB       = [math]::Round($cs.TotalPhysicalMemory / 1GB)
    Gpus        = $gpus
    Hybrid      = (($gpus | Measure-Object).Count -gt 1)   # integrated + GeForce: the game must be pinned to the GeForce
    Disks       = $disks
    Root        = $root
    EpicDir     = Get-RocklandEpicDir $root
    # Performance target for the CANTA KART slice. Desktop: 120 fps at 1440p. Laptop: 60 fps at 1080p on its own screen.
    TargetFps   = $(if ($laptop) { 60 } else { 120 })
    TargetRes   = $(if ($laptop) { "1920x1080" } else { "2560x1440" })
  }
}
