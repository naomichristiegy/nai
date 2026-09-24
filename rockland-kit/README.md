# ROCKLAND GAMES desktop kit

Everything here runs on the pink GeForce desktop (Windows, RTX 3080, N: drive).
It was prepared in a cloud session that cannot touch the desktop, so nothing
below has been executed yet. Run the numbered steps in order.

## Order of operations

| Step | What | How |
|------|------|-----|
| 0 | Keep the PC and screen awake | `scripts\00-never-sleep.cmd` (double-click, no admin) |
| 1 | Start Remote Control so you can drive the PC from your phone | open a terminal in `N:\` and run `claude remote-control` |
| 2 | Git, Git LFS, Epic Games Launcher | `scripts\01-install-tools.cmd` (right-click, Run as administrator) |
| 3 | Visual Studio 2022 Community + "Game development with C++" | `scripts\02-install-visualstudio.cmd` (right-click, Run as administrator) |
| 4 | Unreal Engine newest 5.x and UEFN into `N:\Epic` | in the Epic Games Launcher, see below |
| 5 | Create `N:\ROCKLAND-GAMES` with git + LFS and the BerbiceWorld project | `scripts\03-create-rockland-games.ps1` (right-click, Run with PowerShell) |
| 6 | Build the CANTA KART vertical slice | `CantaKart\VERTICAL-SLICE-PLAN.md` |

## Step 4: Unreal Engine and UEFN into N:\Epic

The launcher picks the install folder in its UI, not from a script.

1. Sign in to the Epic Games Launcher. Account country: United States.
2. Left sidebar → **Unreal Engine** → **Library** tab → **+** next to Engine Versions.
3. Pick the newest **5.x** release (not a preview). Click **Install**.
4. In the install dialog, click **Browse** and choose `N:\Epic\UE_5.x`. Never accept the default on C:.
5. Left sidebar → **Unreal Engine** → **UEFN** → **Install**. Browse to `N:\Epic\UEFN`.
6. Also set **Settings → Vault Cache Location** to `N:\Epic\VaultCache` so Marketplace assets stay off C:.

## Rules (apply to every file and every session)

- Studio name is ROCKLAND GAMES.
- The three-letter abbreviation of the well-known crime game series never appears anywhere.
- Pink paint, never gore. Creatures are befriended, never captured.
- No real private people. Naomi's son's birth date never appears anywhere.
- Every account country is United States.
- Publish nothing. Stage builds in `N:\ROCKLAND-GAMES\Builds` and tell Naomi.
- Commit after every session. Never push.
- After every session write `N:\ROCKLAND-GAMES\Docs\REPORT.md` and tell Naomi in one short message.
