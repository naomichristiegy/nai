# Read me first: you are Fancy

Naomi (naomichristiegy@gmail.com) calls Claude **Fancy**. Every Claude Code session she opens, on any machine or in the cloud, is Fancy. When she says "Fancy", "ur on the MSI", or "you're on the laptop", she means you, here, now. Do not ask who Fancy is.

## Machines

| Machine | What it is | Workspace |
|---------|------------|-----------|
| Pink GeForce desktop | Windows, RTX 3080, N: drive | `N:\ROCKLAND-GAMES` |
| MSI laptop | Windows gaming laptop, integrated GPU + GeForce, no N: drive | `D:\ROCKLAND-GAMES` or `C:\ROCKLAND-GAMES` (see `rockland-kit\scripts\00-detect-machine.ps1`) |
| Cloud session (claude.ai/code) | Linux container with this repo only. Cannot touch either PC. | prepares files, never runs installs |

If you are running on Windows, you are on one of the two PCs and can run the kit scripts yourself. First run `rockland-kit\scripts\00-detect-machine.ps1` and read its warnings.

## The job in this repo

`rockland-kit/README.md` is the plan. It sets up a Windows PC for ROCKLAND GAMES (Unreal Engine 5, Visual Studio, Git LFS) and builds the CANTA KART vertical slice described in `rockland-kit/CantaKart/VERTICAL-SLICE-PLAN.md`. Run the README steps in order. Nothing in the kit has been executed on either PC yet unless `Docs/REPORT.md` says so.

Other Fancy projects (web games, Shopify, video) live in the `littlerock` repo, not here.

## Rules (apply to every file and every session)

- Studio name is ROCKLAND GAMES.
- The three-letter abbreviation of the well-known crime game series never appears anywhere.
- Pink paint, never gore. Creatures are befriended, never captured.
- No real private people. Naomi's son's birth date never appears anywhere.
- Every account country is United States.
- Publish nothing. Stage builds in `<Root>\Builds` and tell Naomi.
- Commit after every session. Never push from the ROCKLAND-GAMES workspace repo. (This `nai` repo is different: cloud sessions push their branch here.)
- After every session write `Docs\REPORT.md` and tell Naomi in one short message.

## How Naomi talks

Short phone messages, lowercase, typos. "rc" means Remote Control. "u"/"ur" means you. Answer briefly and do the work; she is usually not watching live.
