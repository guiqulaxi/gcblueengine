# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 10410 Svetlyak'
    dbObj.natoClass='Svetlyak'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=375000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1988.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='wPG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=49.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-4','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Palm Frond SS','Peel Cone AS/SS','Sheksna VDS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=0.207220
    dbObj.mfTurnRate_degps=5.594219
    dbObj.mfFuelCapacity_kg=52500.000000
    dbObj.mfFuelRate_kgps=0.116666
    dbObj.mfToughness=26.000000
    dbObj.damageEffect='Pr 10410 Svetlyak durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','406mm torpedo tube x2','76 mm/59 (3in) AK-176','SA-N-5 x4 launcher']
    dbObj.maMagazineClass=['AK-630 x1 Store','Pr10410 Ammo Mag']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[270.000000,0.000000,240.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=28.156000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.337999
    airDetectionDBObject.irSignature_dB=17.452000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.200000
    dbObj.beam_m=9.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=16200.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
