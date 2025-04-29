# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Virginia CGN B3'
    dbObj.natoClass='Virginia CGN B3'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=11670000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=1994.859985
    dbObj.country='USA'
    dbObj.designation='CA'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='TicoMk26.xml'
    dbObj.notes=''
    dbObj.length_m=178.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPG-51D 8','SPS-48C AS','SPS-49(v)5','SPS-55 SS','SQS-26 Active','SQS-26 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.081466
    dbObj.mfTurnRate_degps=1.312200
    dbObj.mfFuelCapacity_kg=1633800.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=759.000000
    dbObj.damageEffect='Virginia CGN durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['Mk-26 Mod0','Mk-26 Mod1','5/54 Mark 45 Mods 0 - 2','5/54 Mark 45 Mods 0 - 2','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-143 ABL','Mk-143 ABL']
    dbObj.maMagazineClass=['127mm Mk-45 1200 rounds','Mk-26 Mod0 + Mod1 Store','Phalanx 0 x2 Store','US Ship Torpedo Racks']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[1,0,2,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,270.000000,300.000000,0.000000,0.000000,220.000000,220.000000,40.000000,40.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,180.000000,0.000000,90.000000,270.000000,90.000000,270.000000,270.000000,90.000000,30.000000,330.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,40.000000,40.000000]
    dbObj.launcherFireControl=['SPG-51D 8','SPG-51D 8','','','','','Phalanx FC','Phalanx FC','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=50.551998
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.858000
    airDetectionDBObject.irSignature_dB=13.299000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.400000
    dbObj.beam_m=19.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
