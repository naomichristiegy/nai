@echo off
rem ROCKLAND GAMES: keep the PC and its screen awake. Desktop and MSI laptop.
rem No admin needed for the sleep timers. Applies to the active power plan, plugged in and on battery.
powercfg /change monitor-timeout-ac 0
powercfg /change monitor-timeout-dc 0
powercfg /change standby-timeout-ac 0
powercfg /change standby-timeout-dc 0
powercfg /change hibernate-timeout-ac 0
powercfg /change hibernate-timeout-dc 0
powercfg /change disk-timeout-ac 0
powercfg /change disk-timeout-dc 0
rem Laptop: closing the lid must not sleep the machine, or Remote Control drops mid-build.
rem These two lines may need "Run as administrator"; if they print Access is denied, re-run this file that way once.
powercfg /setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0
powercfg /setdcvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0
powercfg /setactive SCHEME_CURRENT
echo.
echo Screen and PC sleep are now OFF on the active power plan. Closing the lid does nothing.
echo Laptop: keep the charger plugged in. On battery the GeForce is throttled and Unreal stutters.
echo Also turn off "Lock screen after" in Settings ^> Accounts ^> Sign-in options if Remote Control gets interrupted.
pause
