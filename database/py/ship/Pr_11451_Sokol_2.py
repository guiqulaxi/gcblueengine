# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 11451 Sokol-2'
    dbObj.natoClass='Mukha'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=470000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.099976
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='PG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-4','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-329 Shelon VDS','Peel Cone AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=60.500000
    dbObj.mfAccel_ktsps=1.578152
    dbObj.mfTurnRate_degps=7.231384
    dbObj.mfFuelCapacity_kg=65800.000000
    dbObj.mfFuelRate_kgps=0.178318
    dbObj.mfToughness=31.000000
    dbObj.damageEffect='Pr 11451 Sokol-2 durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','76 mm/59 (3in) AK-176']
    dbObj.maMagazineClass=['AK-630 x2 Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,240.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=29.627001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=20.349001
    airDetectionDBObject.irSignature_dB=23.097000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S001.Merchant Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.260000
    dbObj.beam_m=9.890000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=48500.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=6.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
