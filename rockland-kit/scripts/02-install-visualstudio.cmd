@echo off
rem ROCKLAND GAMES: Visual Studio 2022 Community with the "Game development with C++" workload.
rem One line, one admin click. Unreal's own recommended components are included.
winget install --id Microsoft.VisualStudio.2022.Community -e --accept-package-agreements --accept-source-agreements --override "--passive --wait --add Microsoft.VisualStudio.Workload.NativeGame --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 --add Microsoft.VisualStudio.Component.Windows11SDK.22621 --add Microsoft.VisualStudio.Component.Unreal --includeRecommended"
echo.
echo Visual Studio 2022 Community install finished (or was already present).
pause
