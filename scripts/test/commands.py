Tutorial/SurfaceOperations.py 100
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
UI.Launch(launcher, 1)

def AttackTarget(UI):
    UI.AddTask('InterceptTarget', 2.0, 0)   
    def InterceptTarget(TI): 