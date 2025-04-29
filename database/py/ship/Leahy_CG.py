# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Leahy CG'
    dbObj.natoClass='Leahy CG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=7590000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1962.589966
    dbObj.finalYear=1971.000000
    dbObj.country='USA'
    dbObj.designation='CA'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='TicoMk26.xml'
    dbObj.notes=''
    dbObj.length_m=162.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPG-55 4','SPS-10','SPS-37','SPS-39A','SQS-26 Active','SQS-26 Passive','WLR-1H ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.045070
    dbObj.mfTurnRate_degps=1.549416
    dbObj.mfFuelCapacity_kg=1062600.000000
    dbObj.mfFuelRate_kgps=0.516537
    dbObj.mfToughness=759.000000
    dbObj.damageEffect='Leahy CG durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['Mk-10 GMLS','Mk-10 GMLS','Mk-112 ASROC','3/50 Mark 33','3/50 Mark 33','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['76mm mk33 x2 store','Mk-10 Store 80','Mk-32 Torpedo Racks']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[330.000000,330.000000,300.000000,180.000000,180.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,265.000000,95.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-55 4','SPG-55 4','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.749001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.839001
    airDetectionDBObject.irSignature_dB=24.823999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.900000
    dbObj.beam_m=16.760000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=85000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Pad'
    dbObj.CalculateParams()
    return dbObj
