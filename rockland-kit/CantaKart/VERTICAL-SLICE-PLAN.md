# CANTA KART vertical slice: build plan

Studio: ROCKLAND GAMES. Project: `N:\ROCKLAND-GAMES\BerbiceWorld`. Target: 120 fps on the RTX 3080, Lumen off.
The C++ time-trial logic, config, and packaging settings are already in the project. The steps below are
editor work on the desktop, in order. Each step ends with a commit (never a push).

## 1. Open and compile
1. Double-click `BerbiceWorld.uproject`. Accept the prompt to build the editor module.
2. If the build fails, open `BerbiceWorld.sln` in Visual Studio 2022, set config **Development Editor**, build.
3. Confirm Project Settings → Plugins shows Chaos Vehicles, Media Framework, WMF Media enabled.

## 2. New Amsterdam seawall road (about 2 km)
1. Landscape mode → New. Section size 63x63, sections per component 1x1, components 32x16. Scale 100 = about 2 km on the long axis.
2. Sculpt: flat coastal plain, a raised seawall ridge along one long edge (about 2 m up), water plane just past it.
3. Add a **Landscape Spline** along the seawall top. Segments about 40 m apart. Width 800 (two lanes).
4. Spline mesh: a simple asphalt road segment from `Source-Art` (or a scaled engine cube with a dark material for first pass). Enable "Raise/Lower terrain" on the spline so the road sits on the landscape.
5. Make the road a loop: return leg on the landward side so 3 laps is one closed circuit of about 2 km.
6. Paint layers: asphalt on the road, grass and sand off it. Kick up dust later, not now.
7. Sky: Directional Light + Sky Atmosphere + Sky Light (real-time capture off), late-afternoon sun from the sea side.
8. Save as `Content/CantaKart/Maps/SeawallRoad`. Commit.

## 3. One drivable kart (Chaos Vehicles, arcade handling)
1. Content → CantaKart → Vehicles. Import a kart FBX from `Source-Art` with 4 wheel bones, or use the engine's Sports Car skeletal mesh to start and swap later.
2. Physics Asset: chassis box, no wheel bodies (wheels are simulated by the vehicle component).
3. Blueprint `BP_Kart` with parent **WheeledVehiclePawn**.
   - Vehicle Movement Component: 4 wheels using `BP_KartWheelFront` and `BP_KartWheelRear` (parent ChaosVehicleWheel).
   - Arcade feel: mass 350, engine max torque 500, max RPM 6000, single gear, differential rear-wheel, wheel friction force multiplier 3.0, steering angle 35, suspension max raise/drop 5, damping ratio 0.8, center of mass lowered 20 cm.
   - Enhanced Input: `IA_Throttle` (W/S, right trigger), `IA_Steer` (A/D, left stick), `IA_Brake` (Space), `IA_Reset` (R), mapping context `IMC_Kart`.
   - Spring arm 450 cm behind, 120 cm up, camera lag 3.0, FOV 95.
4. `BP_KartGameMode` is not needed: the C++ `TimeTrialGameMode` is already the project default. Set its Default Pawn Class to `BP_Kart` in Project Settings → Maps & Modes.
5. Place a Player Start on the road just before the start line. Test-drive. Commit.

## 4. 3-lap time trial with checkpoints and the pink lap timer
1. Drag `CantaCheckpoint` (C++ class) onto the road every 250 to 300 m around the loop. Set `CheckpointIndex` 0 at the start line, then 1, 2, 3... in driving order. Rotate each so the box spans the road.
2. Widget `WBP_LapTimer` (UMG):
   - Big text bound to `FormatLapTime(GameMode.GetCurrentLapTime())`, font 64, color pink **#FF4FA3**, outline 2 px white.
   - Below it: `Lap 1/3`, best lap, total time. Same pink, smaller.
   - Bind `OnLapCompleted` to flash the lap text white for 0.3 s; `OnTrialFinished` to show "FINISHED" with total time.
3. In `BP_Kart` BeginPlay: create `WBP_LapTimer`, add to viewport.
4. Wrong-way and skipped gates are ignored by the game mode; no need for extra logic in the slice.
5. Play 3 laps end to end. Commit.

## 5. In-kart radio: 99 Pulstar stream
1. Content → CantaKart → Audio. Create **Stream Media Source** `SMS_99Pulstar`. Stream URL:
   `https://lrtvs.gy:8443/99.mp3`
2. Create **Media Player** `MP_Radio` (Play on Open, Loop off). Create its **Media Sound Wave**.
3. In `BP_Kart` add a **Media Sound Component**, set its Media Player to `MP_Radio`, attach to the chassis, attenuation off (it plays through the player's ears).
4. BeginPlay: `MP_Radio → Open Source (SMS_99Pulstar)`. Add `IA_Radio` (M key) to toggle mute.
5. If WMF refuses the stream, check the TLS certificate on port 8443 is one Windows trusts; a self-signed certificate blocks playback. Fallback: enable the **Electra** media player plugin and retry.
6. Commit.

## 6. Performance pass (120 fps target)
1. `stat fps`, `stat unit` in PIE. Lumen is already off via config; verify Project Settings → Rendering shows Global Illumination = None, Reflections = None.
2. Landscape LOD distribution 1.75, road spline meshes LOD 3 levels.
3. Foliage: none in the slice.
4. If short of 120 at 1440p, set `r.ScreenPercentage 85` and turn off Nanite for the road meshes.
5. Commit.

## 7. Package and record
1. Platforms → Windows → **Package Project**. Config is already Shipping, staging to `N:\ROCKLAND-GAMES\Builds`.
2. Launch `Builds\Windows\CantaKart.exe`. Drive one clean lap.
3. Record 60 seconds with OBS (Display Capture of the game window, 1080p60, MP4) to `N:\ROCKLAND-GAMES\Builds\CantaKart-lap-YYYY-MM-DD.mp4`.
4. Do NOT upload the build or the recording anywhere. Stage it and tell Naomi.
5. Write `Docs\REPORT.md`. Commit.

## Rules that apply to every asset name and every line of text
ROCKLAND GAMES. No three-letter crime-game abbreviation. Pink paint, never gore. No real private people. No birth dates. Publish nothing.
