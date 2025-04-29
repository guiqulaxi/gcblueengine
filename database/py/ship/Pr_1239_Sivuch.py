# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1239 Sivuch'
    dbObj.natoClass='Bora'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1050000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1998.209961
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='PGG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=63.900002
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Cross Dome AS/SS','ESM-5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Half Hat']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=52.700001
    dbObj.mfAccel_ktsps=0.305529
    dbObj.mfTurnRate_degps=4.854979
    dbObj.mfFuelCapacity_kg=147000.000000
    dbObj.mfFuelRate_kgps=0.195998
    dbObj.mfToughness=81.000000
    dbObj.damageEffect='Pr 1239 Sivuch durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','76 mm/59 (3in) AK-176','SA-N-4 x2 Launcher','SS-N-22 x4 Launcher x2']
    dbObj.maMagazineClass=['AK-630 x2 Store']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[270.000000,340.000000,300.000000,320.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,40.000000,20.000000]
    dbObj.launcherFireControl=['','','','Cross Dome AS/SS','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=34.862999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.025999
    airDetectionDBObject.irSignature_dB=26.323999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S13.HoverCraft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.300000
    dbObj.beam_m=17.200001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=40000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
