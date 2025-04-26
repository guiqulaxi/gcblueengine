# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Oliver Hazard Perry FFGHM(Egypt)'
    dbObj.natoClass='Oliver Hazard Perry FFGHM(Egypt)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3513000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1996.709961
    dbObj.finalYear=2999.000000
    dbObj.country='Egypt'
    dbObj.designation='FFG'
    dbObj.imageList='ohp.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes='will perform the neutering at random amongst those that were still in servve, spread at a rate of one every 3 weeks, 1.5 years in total since it happened to 26 ships.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Mk-92 STIR Mod6','Phalanx FC','SLQ-32(v)2 ESM B.1','SLQ-32(v)2 ESM B.2','SLQ-32(v)2 ESM B.3','SPS-49(v)5','SPS-55','SQR-19B TA','SQS-56 Active','SQS-56 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.172211
    dbObj.mfTurnRate_degps=1.986355
    dbObj.mfFuelCapacity_kg=491820.000000
    dbObj.mfFuelRate_kgps=0.491816
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Oliver Hazard Perry FFGHM durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','76 mm/62 Mark 75','Mk-13 Mod4 GMLS','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['SH-60 1.1 Support','Mk-13 Mod4 Rotary Store 40','Phalanx 1 x1 Store','76mm/62 mk75 240 rounds']
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[350.000000,320.000000,300.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[180.000000,180.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,40.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','Mk-92 STIR Mod6','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=42.730999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.434000
    airDetectionDBObject.irSignature_dB=23.646999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.700000
    dbObj.beam_m=14.310000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=41000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='OHP Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
