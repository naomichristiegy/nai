@echo off
rem ROCKLAND GAMES: Git, Git LFS, Epic Games Launcher. Run as administrator. Same on desktop and laptop.
winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements
winget install --id GitHub.GitLFS -e --accept-package-agreements --accept-source-agreements
winget install --id EpicGames.EpicGamesLauncher -e --accept-package-agreements --accept-source-agreements
echo.
echo Done. Open the Epic Games Launcher, sign in (country: United States),
echo then install Unreal Engine 5.x and UEFN into the Epic folder on the workspace drive
echo (N:\Epic on the desktop; the drive 00-detect-machine.ps1 printed on the laptop). See README.md step 4.
pause
