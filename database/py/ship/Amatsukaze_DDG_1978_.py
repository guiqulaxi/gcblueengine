# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Amatsukaze DDG(1978)'
    dbObj.natoClass='Amatsukaze DDG(1978)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1978.000000
    dbObj.finalYear=1995.911011
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','NOLR-6B','OPS-17','SPG-34','SPG-51 1','SPS-29','SQS-23 Active','SQS-23 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.044493
    dbObj.mfTurnRate_degps=2.055762
    dbObj.mfFuelCapacity_kg=560000.000000
    dbObj.mfFuelRate_kgps=0.399997
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Amatsukaze DDG durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Mk-13 GMLS','3/50 Mark 27 Twin','3/50 Mark 27 Twin','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-112 ASROC']
    dbObj.maMagazineClass=['76mm mk33 Store','Mk-13 Rotary Store 40','Japanese Ship Torpedo Racks']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[340.000000,300.000000,320.000000,30.000000,30.000000,300.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,0.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-51 1','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.577000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.402000
    airDetectionDBObject.irSignature_dB=20.572001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.200000
    dbObj.beam_m=13.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
