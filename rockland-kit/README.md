# ROCKLAND GAMES desktop and laptop kit

Everything here runs on Windows on either ROCKLAND GAMES machine:

| Machine | Workspace | Engine folder | CANTA KART target | How the scripts know |
|---------|-----------|---------------|-------------------|----------------------|
| Pink GeForce desktop (RTX 3080) | `N:\ROCKLAND-GAMES` | `N:\Epic` | 120 fps at 1440p | an N: drive exists |
| MSI laptop | `D:\ROCKLAND-GAMES` if the laptop has a data drive with 150 GB free, else `C:\ROCKLAND-GAMES` | `D:\Epic` or `C:\Epic` | 60 fps at 1080p | no N: drive, a battery |

Below, `<Root>` means the workspace for the machine you are on. `scripts\00-detect-machine.ps1` prints it.
Any other drive: run `scripts\03-create-rockland-games.ps1 -Root E:\ROCKLAND-GAMES`, or set the `ROCKLAND_ROOT` environment variable.

The kit was prepared in cloud sessions that cannot touch either machine, so nothing below has been executed yet. Run the numbered steps in order.

## Order of operations

| Step | What | How |
|------|------|-----|
| 0 | See which machine this is, where the workspace goes, and any warnings (disk, RAM, two GPUs) | `scripts\00-detect-machine.ps1` (right-click, Run with PowerShell) |
| 0 | Keep the PC and screen awake; laptop lid does nothing | `scripts\00-never-sleep.cmd` (double-click; re-run as administrator once if the lid lines say Access is denied) |
| 1 | Start Remote Control so you can drive the PC from your phone | open a terminal in the workspace drive and run `claude remote-control` (see below) |
| 2 | Git, Git LFS, Epic Games Launcher | `scripts\01-install-tools.cmd` (right-click, Run as administrator) |
| 3 | Visual Studio 2022 Community + "Game development with C++" | `scripts\02-install-visualstudio.cmd` (right-click, Run as administrator) |
| 4 | Unreal Engine newest 5.x and UEFN into the Epic folder | in the Epic Games Launcher, see below |
| 5 | Create `<Root>` with git + LFS and the BerbiceWorld project; on the laptop also pin the editor to the GeForce | `scripts\03-create-rockland-games.ps1` (right-click, Run with PowerShell) |
| 6 | Build the CANTA KART vertical slice | `CantaKart\VERTICAL-SLICE-PLAN.md` |

## Step 1: Remote Control

If `claude` is not installed yet, in PowerShell run `irm https://claude.ai/install.ps1 | iex`, reopen PowerShell, then `claude login`.
Then `cd` to the workspace drive (`N:\` on the desktop, `D:\` or `C:\` on the laptop) and run `claude remote-control`.
Leave that window open. The session appears in the Claude Code app on your phone.

## Step 4: Unreal Engine and UEFN into the Epic folder

The launcher picks the install folder in its UI, not from a script. Use `N:\Epic` on the desktop and the folder step 0 printed on the laptop (`D:\Epic` or `C:\Epic`).

1. Sign in to the Epic Games Launcher. Account country: United States.
2. Left sidebar → **Unreal Engine** → **Library** tab → **+** next to Engine Versions.
3. Pick the newest **5.x** release (not a preview). Click **Install**.
4. In the install dialog, click **Browse** and choose `<Epic>\UE_5.x`. On the desktop never accept the default on C:. On a one-drive laptop `C:\Epic\UE_5.x` is fine.
5. Left sidebar → **Unreal Engine** → **UEFN** → **Install**. Browse to `<Epic>\UEFN`.
6. Also set **Settings → Vault Cache Location** to `<Epic>\VaultCache` so Marketplace assets stay in one place.

Step 5 also finds an engine left at the launcher default, `C:\Program Files\Epic Games`, so an install that already happened there is not wasted.

## MSI laptop notes

- **Plugged in, always.** On battery Windows throttles the GeForce and Unreal stutters and thermal-throttles. Set the MSI Center or Windows power mode to Best performance while building.
- **Two GPUs.** The laptop has an integrated GPU plus the GeForce. Step 5 pins `UnrealEditor.exe` to the GeForce. After the first package, also pin the game: Settings → System → Display → Graphics → Add desktop app → `<Root>\Builds\Windows\CantaKart.exe` → Options → **High performance**.
- **Disk.** Unreal Engine 5.x is about 60 GB, Visual Studio about 10 GB, the DerivedDataCache grows past 20 GB. Step 0 warns below 150 GB free. An external SSD works: run step 5 with `-Root E:\ROCKLAND-GAMES` and install the engine to `E:\Epic`.
- **Heat.** Lift the back of the laptop or use a cooling pad for shader compiles and packaging; they run every core for 10 to 30 minutes.
- **Screen.** The slice targets 60 fps at 1080p on the laptop's own screen. On an external 1440p monitor expect to drop `r.ScreenPercentage` to 75.
- **The same repo, two machines.** Each machine has its own local git repo in its own `<Root>`. Nothing is pushed, by rule, so carry work between machines on a USB drive by copying `<Root>` whole, `.git` included.

## Rules (apply to every file and every session)

- Studio name is ROCKLAND GAMES.
- The three-letter abbreviation of the well-known crime game series never appears anywhere.
- Pink paint, never gore. Creatures are befriended, never captured.
- No real private people. Naomi's son's birth date never appears anywhere.
- Every account country is United States.
- Publish nothing. Stage builds in `<Root>\Builds` and tell Naomi.
- Commit after every session. Never push.
- After every session write `<Root>\Docs\REPORT.md` and tell Naomi in one short message.
