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
