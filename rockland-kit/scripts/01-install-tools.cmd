@echo off
rem ROCKLAND GAMES: Git, Git LFS, Epic Games Launcher. Run as administrator.
winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements
winget install --id GitHub.GitLFS -e --accept-package-agreements --accept-source-agreements
winget install --id EpicGames.EpicGamesLauncher -e --accept-package-agreements --accept-source-agreements
echo.
echo Done. Open the Epic Games Launcher, sign in (country: United States),
echo then install Unreal Engine 5.x and UEFN into N:\Epic as described in README.md.
pause
