# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 11661 Yastreb'
    dbObj.natoClass='Gepard'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1930000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2003.660034
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=102.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Cross Dome AS/SS','ESM-5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MGK-365 Zvezda M-1 Active','MGK-365 Zvezda M-1 Passive','MGK-365 Zvezda M-1 TA']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.233196
    dbObj.mfTurnRate_degps=2.568922
    dbObj.mfFuelCapacity_kg=270200.000000
    dbObj.mfFuelRate_kgps=0.150110
    dbObj.mfToughness=149.000000
    dbObj.damageEffect='Pr 11661 Yastreb durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['SA-N-4 x2 Launcher','SS-N-25 x4 Launcher x2','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','533mm torpedo x2 tubes','533mm torpedo x2 tubes','76 mm/59 (3in) AK-176']
    dbObj.maMagazineClass=['AK-630 x2 Store','Pr11661 Ammo Mag']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,0.000000,240.000000,240.000000,40.000000,40.000000,270.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,0.000000,180.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,20.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Cross Dome AS/SS','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=38.828999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.306999
    airDetectionDBObject.irSignature_dB=23.483000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.700000
    dbObj.beam_m=13.760000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=38000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
