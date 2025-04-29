# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Luetjens DDG'
    dbObj.natoClass='Luetjens DDG'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1969.219971
    dbObj.finalYear=1993.000000
    dbObj.country='Germany'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes=''
    dbObj.length_m=133.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPG-51D 2','SPR-1 ESM','SPS-10','SPS-29','SPS-39','SQS-23 Active','SQS-23 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.053719
    dbObj.mfTurnRate_degps=1.876797
    dbObj.mfFuelCapacity_kg=630000.000000
    dbObj.mfFuelRate_kgps=0.583328
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Lutjens DDG durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Mk-13 GMLS','127mm/54 (5in) Mk42','127mm/54 (5in) Mk42','Mk-112 ASROC','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['127mm Mk-42 500 Rounds','Mk-13 Rotary Store 40 Lutjens','Mk-32 Torpedo Racks','Mk-112 ASROC Reloads']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,360.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-51D 2','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.344002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.148001
    airDetectionDBObject.irSignature_dB=21.681999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.100000
    dbObj.beam_m=14.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=70000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
