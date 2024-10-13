Tutorial/SurfaceOperations.py 100
#添加联盟
alliance_a=1
SM.CreateAlliance(alliance_a, 'Training')
alliance_b=2
SM.CreateAlliance(alliance_b, 'OPFOR')
#加载/清除想定
SM=ScenarioManager
SM.LoadScenario('scenarios/Tutorial/SateliteOperations.py')
SM.ClearScenario()
#设置想定推演速度
SM.SetTimeAccel(10)
#设置航向
UI = ScenarioManager.GetUnitInterface("JDS Atago")
UI.SetHeading(90)

#干预起飞飞机
UI = ScenarioManager.GetUnitInterface("Chinese Airbase")
if(UI.HasFlightPort()):
    FP=UI.GetFlightPortInfo()
    id=FP.GetUnitID(1)
    FP.LaunchID(id)

UI = ScenarioManager.GetUnitInterface('JDS Atago')
if(UI.HasFlightPort()):
    FP=UI.GetFlightPortInfo()
    id=FP.GetUnitID(0)
    FP.LaunchID(id)   

#任务起飞飞机
UI = ScenarioManager.GetUnitInterface("Chinese Airbase")
if(UI.HasFlightPort()):
    FP=UI.GetFlightPortInfo()
    FP.AddAircraftToMission(mission_id, 'Eye-1')
    FP.AddAircraftToMission(mission_id, 'Eye-2')
    FP.SetMissionLaunchTime(mission_id, '05:00:00+0m+R0.1')
    FP.SetMissionDatum(mission_id, 0.0000000, 0.0000000)
    FP.SetMissionLandingTarget(mission_id, '')
    FP.SetMissionWaveQuantity(mission_id, 1)
    FP.SetMissionType(mission_id, '')
    FP.SetMissionPatrolArea(mission_id, '0.1611244,1.1077020,0.1580731,1.1047943,0.1600506,1.1047943,0.1622030,1.1075993,')
    FP.AddMissionWaypointAdvanced(mission_id, 0.1648380, 1.1067290, 2000.0, 200.0)
    FP.SetMissionWaypointTasks(mission_id, 0, 'WaitForGroup,EngageAll')
    FP.AddMissionWaypointAdvanced(mission_id, 0.1621050, 1.1070160, 3000.0, 300.0)
    FP.SetMissionWaypointTasks(mission_id, 1, 'AirPatrolArea,EngageAll')

#攻击

def TargetAndEngageWith(UI, target_id, launcher):
    UI.SetTarget(target_id)
    if (UI.IsLauncherEffective(launcher)):
        LaunchTarget(UI, launcher)
    else:
        UI.SetTarget(-1)   # launcher is not effective vs. target, clear target
        UI.DisplayMessage('Canceling launch, not effective vs. target.') 

Tutorial/SurfaceOperations.py 100
target_id =UI.GetTarget()
if(target_id!)
UI.SetTarget(target_id)
    # anAffiliation: UNKNOWN = 0, FRIENDLY = 1, NEUTRAL = 2, HOSTILE = 3
    #
    # anClassMask:
    # PTYPE_SURFACE 0x0010
    # PTYPE_AIR 0x0020
    # PTYPE_MISSILE 0x0040
    # PTYPE_SUBSURFACE 0x0080
    # PTYPE_FIXED 0x0100
    # int anClassMask, float afMaxRange_km, UINT8 anAffiliation
UI = ScenarioManager.GetUnitInterface("Cheng Kung")
track_list = UI.GetTrackList(0x00F0,100, 3)
nTracks = track_list.Size()
for n in range(0, nTracks):
    track_info = track_list.GetTrack(n)
    target_id=track_info.ID
    UI.SetTarget(target_id)
    break
launcher_info = UI.GetBestLauncher()
launcher = launcher_info.Launcher  
if(launcher!=-1)  
    UI.Launch(launcher, 1)
#添加平台
#添加船
SM =ScenarioManager
alliance_a = 1
unit = SM.GetDefaultUnit()
unit.className = 'Cheng Kung FFG'
unit.unitName = 'Cheng Kung'
loc_chengkung = Point()
loc_chengkung.x = 119.7
loc_chengkung.y = 24.2
unit.SetPosition(loc_chengkung.x, loc_chengkung.y, 0)  # lon, lat, alt
unit.heading = 270
unit.speed = 5
SM.AddUnitToAlliance(unit, alliance_a)
SM.AddUnitToFlightDeck(unit.unitName, 'SH-60B', 'Ferret-1', 3)

SM.AddToUnitMagazine(unit.unitName, 'Fuel', 50000)
SM.AddToUnitMagazine(unit.unitName, '76mm Mk-75', 300)
SM.AddToUnitMagazine(unit.unitName, 'Mk-46 Mod5', 16)
SM.AddToUnitMagazine(unit.unitName, 'DICASS Sonobuoy', 48)
UI = SM.GetUnitInterface(unit.unitName)
#跳转位置
UI = ScenarioManager.GetUnitInterface("Cheng Kung")
UI.SetLongitude(120);
UI.SetLatitude(30);
#添加潜艇
SM =ScenarioManager
alliance_a = 1
unit = SM.GetDefaultUnit()
unit.className = 'Kilo-877E SSK'
unit.unitName = 'Yuanzheng 65'
unit.SetPosition(119, 24, -52)  # lon, lat, alt
unit.heading = 250
unit.speed = 3
SM.AddUnitToAlliance(unit, alliance_a)
SM.SetUnitLauncherItem(unit.unitName, 3, 'TEST-71MKE', 1)
SM.SetUnitLauncherItem(unit.unitName, 4, 'TEST-71MKE', 1)
SM.SetUnitLauncherItem(unit.unitName, 5, 'TEST-71MKE', 1)

SM.AddToUnitMagazine(unit.unitName, '53-65M', 4)
SM.AddToUnitMagazine(unit.unitName, 'TEST-71MKE', 6)
UI = SM.GetUnitInterface(unit.unitName)
#设置高度
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
UI.SetAltitude(-120)
#跳转位置
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
deg_to_rad = 0.01745329252
rad_to_deg = 57.2957795131
UI.MovePlatform(120*deg_to_rad,20*deg_to_rad)

#设置燃料
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
UI.SetFuelTest(0.5)
#设置毁伤
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
UI.ApplyDamage(10)
#设置毁伤
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
isPen = 0
kinetic_J = 0
explosive_kg = 0
blast_psi = 0.1 * float(blastPSI)
waterBlast_psi = 0
thermal_J_cm2 = 0
fragHits = 0
fragEnergy_J = 0
UI.ApplyAdvancedDamage(isPen, kinetic_J, explosive_kg, blast_psi, waterBlast_psi, thermal_J_cm2, fragHits, fragEnergy_J)
#删除平台
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
UI.DeletePlatform()
#设置是否可见
UI = ScenarioManager.GetUnitInterface("Yuanzheng 65")
UI.SetAlwaysVisible(0)
def AttackTarget(UI):
    UI.AddTask('InterceptTarget', 2.0, 0)   
    def InterceptTarget(TI): 
#开启传感器
UI.SetAllSensorState(1)
#发射
SM =ScenarioManager
alliance_a = 1
unit = SM.GetDefaultUnit()
unit.className = 'SH-60B'
unit.unitName = "Spruance DDG Seahawk 1"
unit.SetPosition(-9.607291, 62.140074, 510.2)
unit.heading = 92.36
unit.speed = 100.0
unit.cost = 20000000.0
SM.AddUnitToAlliance(unit, 1)
SM.SetUnitLauncherItem(unit.unitName, 0, 'Mk-46 Mod5', 1)
SM.SetUnitLauncherItem(unit.unitName, 1, '120 gallon tank', 1)
SM.SetUnitLauncherItem(unit.unitName, 2, '120 gallon tank', 1)
SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
SM.SetUnitLauncherItem(unit.unitName, 5, 'DICASS (80) Sonobuoy', 5)
SM.SetUnitLauncherItem(unit.unitName, 6, 'LOFAR (80) Sonobuoy', 5)
SM.SetUnitLauncherItem(unit.unitName, 7, 'DIFAR (80) Sonobuoy', 15)
UI = SM.GetUnitInterface(unit.unitName)
from UnitCommands import *
UI = ScenarioManager.GetUnitInterface("Spruance DDG Seahawk 1")
UI.SetAllSensorState(1)
LaunchDatum3D(UI,-9.607291,62.040074,510.2,5)
#批量添加
n=50
SM =ScenarioManager
alliance_a = 1
alliance_b = 2
for i in range(n):
    unit = SM.GetDefaultUnit()
    unit.className = 'SH-60B'
    unit.unitName = "Spruance DDG Seahawk "+str(i)
    unit.SetPosition(-9.607291+i/100., 63.140074+i/100., 510.2)
    unit.heading = 92.36
    unit.speed = 100.0
    unit.cost = 20000000.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Mk-46 Mod5', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, '120 gallon tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '120 gallon tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'DICASS (80) Sonobuoy', 5)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'LOFAR (80) Sonobuoy', 5)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'DIFAR (80) Sonobuoy', 15)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetAllSensorState(1)
    print(i)
for i in range(n):
    unit = SM.GetDefaultUnit()
    unit.className = 'Cheng Kung FFG'
    unit.unitName = 'Cheng Kung'+str(i)
    loc_chengkung = Point()
    loc_chengkung.x = 119.7
    loc_chengkung.y = 24.2
    unit.SetPosition(-9.707291+i/100., 62.140074+i/100., 0)  # lon, lat, alt
    unit.heading = 270
    unit.speed = 5
    SM.AddUnitToAlliance(unit, alliance_b)
    SM.AddUnitToFlightDeck(unit.unitName, 'SH-60B', 'Ferret-1', 3)

    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 50000)
    SM.AddToUnitMagazine(unit.unitName, '76mm Mk-75', 300)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-46 Mod5', 16)
    SM.AddToUnitMagazine(unit.unitName, 'DICASS Sonobuoy', 48)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetAllSensorState(1)
    print(i)
alliance_a = 2
for i in range(n):
    unit = SM.GetDefaultUnit()
    unit.className = 'SH-60B'
    unit.unitName = "Spruance DDG Seahawk b  "+str(i)
    unit.SetPosition(-9.607291+1/100, 62.140074+i/100, 510.2)
    unit.heading = 92.36
    unit.speed = 100.0
    unit.cost = 20000000.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Mk-46 Mod5', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, '120 gallon tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '120 gallon tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'DICASS (80) Sonobuoy', 5)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'LOFAR (80) Sonobuoy', 5)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'DIFAR (80) Sonobuoy', 15)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetAllSensorState(1)
    print(i)

