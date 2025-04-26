# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Cheng Kung FFG'
    dbObj.natoClass='Cheng Kung FFG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=500000000.000000
    dbObj.weight_kg=4105000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1993.349976
    dbObj.finalYear=2999.989990
    dbObj.country='Taiwan'
    dbObj.designation='FF'
    dbObj.imageList='chengkung-image3.jpg;chengkung-14601.jpg;chengkung-14602.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Mk-92 FC','SLQ-32(v)5 ECM','SLQ-32(v)5 ESM B.1','SLQ-32(v)5 ESM B.2','SLQ-32(v)5 ESM B.3','SPS-49(v)5','SPS-55','SQR-19 TA','SQS-56 Active','SQS-56 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.162305
    dbObj.mfTurnRate_degps=1.885870
    dbObj.mfFuelCapacity_kg=587015.000000
    dbObj.mfFuelRate_kgps=0.587010
    dbObj.mfToughness=250.000000
    dbObj.damageEffect='Cheng Kung FFG durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Hsiung Feng-II x8 Launcher','Mk-13 CK','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-32 SVTT','Mk-32 SVTT','76 mm/62 Mark 75']
    dbObj.maMagazineClass=['SH-60 1.1 Support','Cheng Kung Magazine','Phalanx 0 x1 Store']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['Feng-II Launcher','SM1 SAM Launcher','Mk-15 CIWS','Stbd Torpedo Launcher','Port Torpedo','Mk-75 Gun']
    dbObj.launcherFOV_deg=[0.000000,300.000000,270.000000,0.000000,0.000000,240.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,90.000000,270.000000,180.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Mk-92 FC','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.744999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.434000
    airDetectionDBObject.irSignature_dB=23.688999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=25.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.700000
    dbObj.beam_m=14.310000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=41000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='FFG-7 Helo Deck'
    dbObj.CalculateParams()
    return dbObj
