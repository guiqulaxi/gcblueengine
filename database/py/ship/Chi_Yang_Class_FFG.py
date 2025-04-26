# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Chi Yang Class FFG'
    dbObj.natoClass='Chi Yang Class FFG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4066000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1969.280029
    dbObj.finalYear=1994.579956
    dbObj.country='Taiwan'
    dbObj.designation='FF'
    dbObj.imageList='ohp.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes='[phoenixegmh]'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DA-08','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SQR-19 TA','SQS-26 Active','SQS-26 Passive','SQS-35 VDS Active','SQS-35 VDS','STIR 180']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000,180.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.037486
    dbObj.mfTurnRate_degps=1.838951
    dbObj.mfFuelCapacity_kg=569240.000000
    dbObj.mfFuelRate_kgps=0.509155
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Chi Yang Class FFG durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['127mm/54 (5in) Mk42','Mk-16 4x ABL','Mk-16 4x ABL','Mk-32 2 Torpedo Mount','Mk-32 2 Torpedo Mount','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-26 Mod0','Mk-26 Mod0','Mk-22 GMLS','Mk-22 GMLS']
    dbObj.maMagazineClass=['SH-2F 1.1 Support','127mm Mk-42 500 Rounds','Phalanx 0 x1 Store']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','FW SM-1','FW SM-1','SB SM-1','PT SM-1']
    dbObj.launcherFOV_deg=[320.000000,300.000000,300.000000,40.000000,40.000000,330.000000,180.000000,180.000000,100.000000,100.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,0.000000,90.000000,270.000000,180.000000,360.000000,360.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','STIR 180','STIR 180','STIR 180','STIR 180']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.682999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.480000
    airDetectionDBObject.irSignature_dB=21.653999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.540000
    dbObj.beam_m=14.250000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=35000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='OHP Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
