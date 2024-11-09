from math import *
from random import *
from UnitCommands import *

class Point:
    x = 0
    y = 0
def LoadDatabase(DM):
    cdd =DM.Clear()
    # DM.AddOrUpdateObject()
# SM is ScenarioManager object
def CreateScenario(SM):


    alliance_a = 1
    alliance_b = 2
    SM.SetScenarioDescription('Tutorial scenario for surface operations\n')
    SM.SetScenarioName('Surface Operations Tutorial')



    SM.CreateAlliance(alliance_a, 'Training')
    SM.SetAllianceDefaultCountry(alliance_a, 'Training')
    SM.SetAlliancePlayable(1, 1)
    SM.CreateAlliance(alliance_b, 'OPFOR')
    SM.SetAllianceDefaultCountry(alliance_b, 'OPFOR')
    SM.SetAlliancePlayable(2, 1)

    SM.SetDateTime(2005, 10, 31, 10, 0, 0)
    SM.SetStartTheater(119.6, 25)  # (lon, lat) in degrees, negative is West or South
    SM.SetScenarioLoaded(1)
    SM.SetUserAlliance(1)

    #AddOverlayGraphics(SM)
   

    unit = SM.GetDefaultUnit()

    ### Alliance A units




    unit = SM.GetDefaultUnit()
    unit.className = 'Satelite'
    unit.unitName = 'Satelite-1'
    #double a_km, double e, double i_deg,
    #double Omega_deg, double omega_deg,
    #double M_deg, double tp
    unit.SetOrbit(12164.173, 0.01, 0.02,0.3,0.4,0,0)  
    
    SM.AddUnitToAlliance(unit, alliance_a)
    UI = SM.GetUnitInterface(unit.unitName)
  










    









