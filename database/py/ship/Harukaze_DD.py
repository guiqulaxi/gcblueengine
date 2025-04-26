# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Harukaze DD'
    dbObj.natoClass='Harukaze DD'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2340000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1956.317993
    dbObj.finalYear=1959.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-42_temp.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPS-5','SPS-6','SQS-29 Active','SQS-29 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.040730
    dbObj.mfTurnRate_degps=2.471056
    dbObj.mfFuelCapacity_kg=327600.000000
    dbObj.mfFuelRate_kgps=0.272998
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Harukaze DD durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['5/38 Mark 12','5/38 Mark 12','5/38 Mark 12','40mm Bofors Mk12','40mm Bofors Mk12','Hedgehog','Hedgehog','Kgun x4','Kgun x4','DC Rack 12']
    dbObj.maMagazineClass=['127mm mk12/16 900 round','40mm Bofors x2 Magazine','Japanese ASW Magazine']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','Stbd Kgun','Port Kgun','Aft DC Rack']
    dbObj.launcherFOV_deg=[300.000000,330.000000,300.000000,340.000000,340.000000,30.000000,30.000000,10.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,180.000000,0.000000,180.000000,0.000000,0.000000,90.000000,270.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=40.084000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.361000
    airDetectionDBObject.irSignature_dB=20.419001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.400000
    dbObj.beam_m=10.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=15000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
