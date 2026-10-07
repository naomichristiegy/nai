# ROCKLAND GAMES session report

## Session 1 (prepared 2026-09-24 in a cloud session, not on the desktop)

**Where this ran:** a claude.ai cloud Linux container. It cannot see the pink GeForce desktop, the N: drive, or the Epic Games Launcher. Nothing below was executed on the desktop.

**Done (files, ready to run):**
- `scripts/00-never-sleep.cmd`: screen and PC never sleep.
- `scripts/01-install-tools.cmd`: Git, Git LFS, Epic Games Launcher (admin click).
- `scripts/02-install-visualstudio.cmd`: Visual Studio 2022 Community with Game development with C++ (admin click, one winget line).
- `scripts/03-create-rockland-games.ps1`: creates `N:\ROCKLAND-GAMES` with BerbiceWorld, CantaKart, Docs, Source-Art, Builds; git + LFS; first commit; generates Visual Studio project files if UE 5.x is in `N:\Epic`.
- `BerbiceWorld/`: Unreal 5.x Blueprint + C++ project skeleton, no starter content. Chaos Vehicles, Media Framework, Enhanced Input enabled. Lumen off, 120 fps cap, DX12, Shipping package to `N:\ROCKLAND-GAMES\Builds`.
- `BerbiceWorld/Source`: `TimeTrialGameMode` (3 laps, ordered checkpoints, lap and total timers, events for the widget) and `CantaCheckpoint` (road gate actor). Written without a compiler here; first editor open will build it.
- `CantaKart/VERTICAL-SLICE-PLAN.md`: step-by-step editor work for the seawall road, kart, time trial, pink timer, 99 Pulstar radio, perf pass, packaging, recording.
- `CantaKart/ROADMAP.md`: ROCKLAND, STARYARD GO, PINKLAND PAINT WARS, and the yard versions of the web games.

**Blocked (needs the desktop):**
- Remote Control, never-sleep, all installs, Unreal Engine and UEFN into `N:\Epic`, the landscape and kart work, packaging, the lap recording.

**Next session (on the desktop):** run README steps 0 to 5, then follow `CantaKart/VERTICAL-SLICE-PLAN.md`.

## Session 2 (prepared 2026-10-07 in a cloud session, not on either machine)

**Where this ran:** a claude.ai cloud Linux container again. Naomi is at the MSI laptop, which has no N: drive, so the kit now serves both machines. Nothing was executed on the laptop or the desktop.

**Done (files, ready to run):**
- `scripts/Rockland-Common.ps1`: shared helpers. Picks the workspace: `N:\ROCKLAND-GAMES` when an N: drive exists (desktop), else the fixed non-C: drive with 150 GB free, else `C:\ROCKLAND-GAMES`. `-Root` and `ROCKLAND_ROOT` override. Finds the newest UE 5.x in `<drive>:\Epic` or the launcher default `C:\Program Files\Epic Games`.
- `scripts/00-detect-machine.ps1`: prints and saves `Docs\MACHINE.md`: model, CPU, RAM, GPUs (flags the integrated one), drives and free space, chosen workspace and Epic folder, frame-rate target, and warnings for low disk, low RAM, battery and hybrid graphics.
- `scripts/00-never-sleep.cmd`: also sets lid close to do nothing (plugged in and on battery) so Remote Control survives a closed lid.
- `scripts/03-create-rockland-games.ps1`: machine-neutral. Rewrites `StagingDirectory` in `DefaultGame.ini` to `<Root>/Builds`. On the laptop pins `UnrealEditor.exe` to the high-performance GPU through the per-user DirectX preference, no admin.
- `README.md`: machine table, `<Root>` convention, Remote Control install line, MSI laptop notes (power, two GPUs, disk, heat, 60 fps target, carrying the repo between machines on USB).
- `CantaKart/VERTICAL-SLICE-PLAN.md`: paths use `<Root>`; perf pass has a laptop branch (60 fps at 1080p, `r.ScreenPercentage 75`, check the GeForce is the one rendering); packaging and recording steps have laptop lines.
- `BerbiceWorld/Config`: comments only. Engine settings unchanged: Lumen off, DX12, `t.MaxFPS=120` is a cap, not a requirement, so it is fine on the laptop.

**Not known yet (the laptop fills it in):** the laptop's exact GPU, RAM and drives. `00-detect-machine.ps1` records them in `Docs\MACHINE.md` on first run.

**Blocked (needs a machine):** everything in README steps 0 to 6.

**Next session (on the MSI laptop):** run `scripts\00-detect-machine.ps1`, read its warnings, then README steps 0 to 5, then `CantaKart/VERTICAL-SLICE-PLAN.md`.
