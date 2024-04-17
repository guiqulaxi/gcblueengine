from math import *
from random import *
from UnitCommands import *

class Point:
    x = 0
    y = 0

# SM is ScenarioManager object
def CreateScenario(SM):

    SM.SetUserAlliance(1)


    alliance_a = 1
    alliance_b = 2
    SM.SetScenarioDescription('Tutorial scenario for submarine and ASW operations\n')
    SM.SetScenarioName('Submarine and ASW Operations Tutorial')
    SM.SetSideCode(1)



    SM.CreateAlliance(alliance_a, 'Training')
    SM.CreateAlliance(alliance_b, 'OPFOR')
    SM.SetScenarioLoaded(1)
    SM.SetDateTime(2005, 10, 31, 10, 0, 0)
    SM.SetStartTheater(119.6, 25)  # (lon, lat) in degrees, negative is West or South

    AddOverlayGraphics(SM)


    unit = SM.GetDefaultUnit()

    ### Alliance A units

    tainan_lon = 120.205556
    tainan_lat = 22.950278



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


    unit = SM.GetDefaultUnit()
    unit.className = 'Kilo-877E SSK'
    unit.unitName = 'Yuanzheng 65'
    unit.SetPosition(loc_chengkung.x-0.1, loc_chengkung.y-0.05, -52)  # lon, lat, alt
    unit.heading = 250
    unit.speed = 3
    SM.AddUnitToAlliance(unit, alliance_a)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'TEST-71MKE', 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'TEST-71MKE', 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'TEST-71MKE', 1)

    SM.AddToUnitMagazine(unit.unitName, '53-65M', 4)
    SM.AddToUnitMagazine(unit.unitName, 'TEST-71MKE', 6)
    UI = SM.GetUnitInterface(unit.unitName)


    
    ### Alliance B (OPFOR) units

    
    rally_lon = loc_chengkung.x
    rally_lat = loc_chengkung.y


        



    unit = SM.GetDefaultUnit()
    unit.className = 'Patrol Boat'
    unit.unitName = 'Target Boat 1'
    unit.SetPosition(rally_lon - 0.05, rally_lat + 0.05, 0)  # lon, lat, alt
    unit.heading = 190
    unit.speed = 5
    SM.AddUnitToAlliance(unit, alliance_b)

    unit = SM.GetDefaultUnit()
    unit.className = 'Patrol Boat'
    unit.unitName = 'Target Boat 2'
    unit.SetPosition(rally_lon - 0.1, rally_lat + 0.05, 0)  # lon, lat, alt
    unit.heading = 190
    unit.speed = 5
    SM.AddUnitToAlliance(unit, alliance_b)

    unit = SM.GetDefaultUnit()
    unit.className = 'Patrol Boat'
    unit.unitName = 'Target Boat 3'
    unit.SetPosition(rally_lon - 0.8, rally_lat + 0.05, 0)  # lon, lat, alt
    unit.heading = 190
    unit.speed = 5
    SM.AddUnitToAlliance(unit, alliance_b)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kilo-877E SSK'
    unit.unitName = 'Yuanzheng 165'
    unit.SetPosition(loc_chengkung.x, loc_chengkung.y-0.33, -40)  # lon, lat, alt
    unit.heading = 270
    unit.speed = 5
    SM.AddUnitToAlliance(unit, alliance_b)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kilo-877E SSK'
    unit.unitName = 'Yuanzheng 166'
    unit.SetPosition(loc_chengkung.x-0.1, loc_chengkung.y-0.1, -40)  # lon, lat, alt
    unit.heading = 270
    unit.speed = 8
    SM.AddUnitToAlliance(unit, alliance_b)



    # create intel text based on random locations of platforms
    intel_a = 'NO ADDITIONAL INTELLIGENCE AVAILABLE.\n'
    
    
    intel_b = 'NO ADDITIONAL INTELLIGENCE AVAILABLE.\n'

    CreateBriefing(SM, alliance_a, alliance_b, intel_a, intel_b)

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
def CreateBriefing(BM, alliance_a, alliance_b, intel_a, intel_b):  

    a_tasks = 'TASKING ORDERS:\n\n'
    a_tasks += 'SEE MANUAL FOR TUTORIAL INSTRUCTIONS\n'
    a_tasks += '\n'
    a_tasks += intel_a

    b_tasks = 'TASKING ORDERS:\n\n'
    b_tasks += 'OPFOR SIDE, THIS TEXT SHOULD NEVER BE SEEN\n'
    b_tasks += intel_b

    BM.SetSimpleBriefing(alliance_a, a_tasks)
    BM.SetSimpleBriefing(alliance_b, b_tasks)

 
    BM.SetEventTime(0)
    BM.Pause()
    BM.PauseAudio()
    BM.SetBriefingMode(1)  # 0 - normal tactical display, 1 - briefing disp
    BM.Set3DMode(1)   # 0 - off, 1 - small, 2 - med, 3 - full screen
    if (alliance_a == 1):
        BM.ConsoleText(a_tasks)
    else:
        BM.ConsoleText(b_tasks)


    BM.Set3DMode(1)
    BM.SetBriefingMode(0) # leave briefing mode
    BM.PlayAudio('tension1',0)   # name, seek time from beginning of song
    BM.Resume()    # resumes game


def AddOverlayGraphics(SM):
    #SM.OverlayText('Taipei', 121.533, 25.083)

    # China airbases
    #SM.OverlayText('Longtian AB', 119.417, 25.583)
    #SM.OverlayText('Fuzhou AB', 119.367, 26.0167)
    #SM.OverlayText('Chin Chiang AB', 118.583, 24.783)
    #SM.OverlayText('Chang-Chou AB', 117.667, 24.583)
    #SM.OverlayText('Shantou AB', 116.75, 23.417)
    SM.OverlayText('Mei-Xian AB', 116.133, 24.25)
    #SM.OverlayText('Ningbo', 121.550, 29.867) # port, fleet HQ

    # Taiwan airbases
    #SM.OverlayText('Cha Shan AB', 121.617, 24.0167)
    #SM.OverlayText('Chiayi AB', 120.392778, 23.461667)
    #SM.OverlayText('Ching Chuan Kang AB', 120.620556, 24.264444)
    #SM.OverlayText('Hsinchu AB', 120.939167, 24.818056)
    #SM.OverlayText('Pingtung AB North', 120.477778, 22.695278)
    #SM.OverlayText('Pingtung AB South', 120.461667, 22.672222)
    SM.OverlayText('Tainan AB', 120.205556, 22.950278)
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







