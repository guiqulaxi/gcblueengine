from math import *
from random import *
from UnitCommands import *

class Point:
    x = 0
    y = 0

# SM is ScenarioManager object
def CreateScenario(SM):




    alliance_a = 1
    alliance_b = 2
    SM.SetScenarioDescription('Tutorial scenario for air operations\n')
    SM.SetScenarioName('Air Operations Tutorial')



    SM.CreateAlliance(alliance_a, 'Training')
    SM.CreateAlliance(alliance_b, 'OPFOR')
    SM.SetUserAlliance(1)
    SM.SetScenarioLoaded(1)
    SM.SetDateTime(2005, 10, 31, 10, 0, 0)
    SM.SetStartTheater(119.6, 25)  # (lon, lat) in degrees, negative is West or South

    # AddOverlayGraphics(SM)


    unit = SM.GetDefaultUnit()

    ### Alliance A units

    tainan_lon = 120.205556
    tainan_lat = 22.950278
    baseName = 'Tainan AB'
    AddAirbase(SM, baseName, tainan_lon, tainan_lat, 0, alliance_a)
    AddAircraftToBase(SM, baseName, 'F-16C', 'Tiger', 4)
    AddAircraftToBase(SM, baseName, 'E2-T', 'Hawkeye', 1)
    AddDefaultTaiwanStores(SM, baseName)


    sam1_lon = tainan_lon - 0.1
    sam1_lat = tainan_lat + 0.2

    
    unit = SM.GetDefaultUnit()
    unit.className = 'Tien Kung-II'
    unit.unitName = 'Sky Bow-1'
    unit.SetPosition(sam1_lon, sam1_lat, 0)  # lon, lat, alt
    unit.heading = 0
    unit.speed = 0
    SM.AddUnitToAlliance(unit, alliance_a)
    UI = SM.GetUnitInterface(unit.unitName)
    if (alliance_a == 2):
        UI.AddTask('Patrol', 2.0, 0)
        UI.AddTask('EngageAll', 3.0, 0)



    unit = SM.GetDefaultUnit()
    unit.className = 'F-16C'
    unit.unitName = 'Dart-1'
    unit.SetPosition(120.0, 24.1, 5000)  # lon, lat, alt
    unit.heading = 290
    unit.speed = 450
    unit.throttle = 0.8
    SM.AddUnitToAlliance(unit, alliance_a)
    UI = SM.GetUnitInterface(unit.unitName)


    unit = SM.GetDefaultUnit()
    unit.className = 'F-16C'
    unit.unitName = 'Dart-2'
    unit.SetPosition(120.0, 24.2, 1000)  # lon, lat, alt
    unit.heading = 290
    unit.speed = 450
    unit.throttle = 0.8
    SM.AddUnitToAlliance(unit, alliance_a)
    UI = SM.GetUnitInterface(unit.unitName)




    
    ### Alliance B (OPFOR) units

    
    rally_lon = sam1_lon - 1.5
    rally_lat = sam1_lat + 0.2


        
    for n in range(0, 4):
        unit = SM.GetDefaultUnit()
        unit.className = 'Su-30MKK'
        unit.unitName = 'Hunter-%d' % n
        unit.SetPosition(rally_lon+0.1*n, rally_lat-0.1, 4500)
        unit.speed = 410
        unit.throttle = 0.8
        SM.AddUnitToAlliance(unit, alliance_b)
        UI = SM.GetUnitInterface(unit.unitName)
        
        AddWaypointOrderDeg(UI, sam1_lon-0.5, sam1_lat+0.1*n)
        AddWaypointOrderDeg(UI, sam1_lon-1.2, sam1_lat+0.1*n)
        UI.SetNavLoopState(1)





    # create intel text based on random locations of platforms
    intel_a = 'NO ADDITIONAL INTELLIGENCE AVAILABLE.\n'
    
    
    intel_b = 'NO ADDITIONAL INTELLIGENCE AVAILABLE.\n'

    #CreateBriefing(SM, alliance_a, alliance_b, intel_a, intel_b)

    ### Add goals for each side
    AddGoals(SM, alliance_a, alliance_b)


def AddAirbase(SM, base_name, lon_deg, lat_deg, orientation_deg, alliance):
    unit = SM.GetDefaultUnit()

    unit.className = 'Airstrip'
    unit.unitName = base_name
    unit.SetPosition(lon_deg, lat_deg, 0)
    unit.heading = orientation_deg
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, alliance)
    SM.AddToUnitMagazine(base_name, 'Fuel', 100000)

# adds aircraft to base, attempts to add to fastest launch position first
def AddAircraftToBase(SM, base_name, aircraft_class, root_name, quantity):
    for n in range(0, quantity):
        unitName = '%s-%d' % (root_name, n)
        # AddUnitToFlightDeck(<carrier name>,<unit class>,<name>, <location>)
        # <location>: 1 = HANGAR, 2 = DECK, 3 = CATAPULT/RUNWAY 
        SM.AddUnitToFlightDeck(base_name, aircraft_class, unitName, 3)

# default stores for Taiwan airbase
def AddDefaultTaiwanStores(SM, base_name):
    SM.AddToUnitMagazine(base_name, 'AGM-65D', 50)
    SM.AddToUnitMagazine(base_name, 'AGM-88', 50)
    SM.AddToUnitMagazine(base_name, 'AIM-9M', 50)
    SM.AddToUnitMagazine(base_name, 'AIM-120C', 50)
    SM.AddToUnitMagazine(base_name, 'GB-200', 50)
    SM.AddToUnitMagazine(base_name, 'Fuel', 500000)


# default stores for China airbase
def AddDefaultChinaStores(SM, base_name):
    SM.AddToUnitMagazine(base_name, 'R-27R', 50)
    SM.AddToUnitMagazine(base_name, 'R-73M', 50)
    SM.AddToUnitMagazine(base_name, 'YJ-6', 50)
    SM.AddToUnitMagazine(base_name, 'GB-500', 50)
    SM.AddToUnitMagazine(base_name, 'Fuel', 500000)



def AddGoals(SM, side_a, side_b):
    
    # alliance 1 goals

    time_1 = SM.TimeGoal()
    time_1.SetPassTimeout(3600)

    SM.SetAllianceGoal(side_a, time_1)
    
    # alliance 2 goals
    time_2 = SM.TimeGoal()
    time_2.SetFailTimeout(3600)

    SM.SetAllianceGoal(side_b, time_2)
    

# BM is BriefingManager (same as ScenarioManager for now) object
# def CreateBriefing(BM, alliance_a, alliance_b, intel_a, intel_b):

#     a_tasks = 'TASKING ORDERS:\n\n'
#     a_tasks += 'SEE MANUAL FOR TUTORIAL INSTRUCTIONS\n'
#     a_tasks += '\n'
#     a_tasks += intel_a

#     b_tasks = 'TASKING ORDERS:\n\n'
#     b_tasks += 'OPFOR SIDE, THIS TEXT SHOULD NEVER BE SEEN\n'
#     b_tasks += intel_b

#     BM.SetSimpleBriefing(alliance_a, a_tasks)
#     BM.SetSimpleBriefing(alliance_b, b_tasks)

 
#     BM.SetEventTime(0)
#     BM.Pause()
#     BM.PauseAudio()
#     BM.SetBriefingMode(1)  # 0 - normal tactical display, 1 - briefing disp
#     BM.Set3DMode(1)   # 0 - off, 1 - small, 2 - med, 3 - full screen
#     if (alliance_a == 1):
#         BM.ConsoleText(a_tasks)
#     else:
#         BM.ConsoleText(b_tasks)


#     BM.Set3DMode(1)
#     BM.SetBriefingMode(0) # leave briefing mode
#     BM.PlayAudio('tension1',0)   # name, seek time from beginning of song
#     BM.Resume()    # resumes game


#def AddOverlayGraphics(SM):
    #SM.OverlayText('Taipei', 121.533, 25.083)

    # China airbases
    #SM.OverlayText('Longtian AB', 119.417, 25.583)
    #SM.OverlayText('Fuzhou AB', 119.367, 26.0167)
    #SM.OverlayText('Chin Chiang AB', 118.583, 24.783)
    #SM.OverlayText('Chang-Chou AB', 117.667, 24.583)
    #SM.OverlayText('Shantou AB', 116.75, 23.417)
    #SM.OverlayText('Mei-Xian AB', 116.133, 24.25)
    #SM.OverlayText('Ningbo', 121.550, 29.867) # port, fleet HQ

    # Taiwan airbases
    #SM.OverlayText('Cha Shan AB', 121.617, 24.0167)
    #SM.OverlayText('Chiayi AB', 120.392778, 23.461667)
    #SM.OverlayText('Ching Chuan Kang AB', 120.620556, 24.264444)
    #SM.OverlayText('Hsinchu AB', 120.939167, 24.818056)
    #SM.OverlayText('Pingtung AB North', 120.477778, 22.695278)
    #SM.OverlayText('Pingtung AB South', 120.461667, 22.672222)
    #SM.OverlayText('Tainan AB', 120.205556, 22.950278)
    #SM.OverlayText('Taitung AB', 121.181944,  22.793056)
    #SM.OverlayText('Tsoying', 120.28, 22.704444) # port

# returns random point along line from (x1, y1) to (x2, y2)
def GetRandomAlongLine(x1, y1, x2, y2):
    p = Point()
    s = random()
    p.x = x1 + s * (x2-x1)
    p.y = y1 + s * (y2-y1)
    return p

# returns random point within r of (x, y)
def GetRandomWithinCircle(x, y, r):
    angle = 2*pi * random()
    r_rand = r * random()
    p = Point()
    p.x = x + r_rand * sin(angle)
    p.y = y + r_rand * cos(angle)
    return p

# returns random point within box (x1, y1) to (x2, y2)
def GetRandomWithinBox(x1, y1, x2, y2):
    p = Point()
    s1 = random()
    s2 = random()
    p.x = x1 + s1 * (x2-x1)
    p.y = y1 + s2 * (y2-y1)
    return p







