@echo off
rem ROCKLAND GAMES: keep the pink GeForce desktop and its screens awake.
rem No admin needed. Applies to the active power plan, plugged in and on battery.
powercfg /change monitor-timeout-ac 0
powercfg /change monitor-timeout-dc 0
powercfg /change standby-timeout-ac 0
powercfg /change standby-timeout-dc 0
powercfg /change hibernate-timeout-ac 0
powercfg /change hibernate-timeout-dc 0
powercfg /change disk-timeout-ac 0
powercfg /change disk-timeout-dc 0
echo.
echo Screen and PC sleep are now OFF on the active power plan.
echo Also turn off "Lock screen after" in Settings ^> Accounts ^> Sign-in options if Remote Control gets interrupted.
pause
