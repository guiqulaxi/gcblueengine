# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Ticonderoga CG Baseline 1'
    dbObj.natoClass='Ticonderoga CG Baseline 1'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=9957000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.060059
    dbObj.finalYear=3000.000000
    dbObj.country='USA'
    dbObj.designation='CG'
    dbObj.imageList='tico.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='TicoMk26.xml'
    dbObj.notes=''
    dbObj.length_m=173.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPG-62 16','SPS-49(v)7','SPS-55','SPY-1A','SQS-53B Active','SQS-53B Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.500000
    dbObj.mfAccel_ktsps=0.171945
    dbObj.mfTurnRate_degps=1.404239
    dbObj.mfFuelCapacity_kg=1393980.000000
    dbObj.mfFuelRate_kgps=1.290711
    dbObj.mfToughness=759.000000
    dbObj.damageEffect='Ticonderoga CG Baseline 1 durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Mk-26 Mod0','Mk-26 Mod1','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','5/54 Mark 45 Mods 0 - 2','5/54 Mark 45 Mods 0 - 2','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['SH-60 2.2 Support','127mm Mk-45 1200 rounds','Phalanx 0 x2 Store','Mk-26 Mod0 + Mod1 Store']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,160.000000,160.000000,0.000000,0.000000,300.000000,270.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,95.000000,265.000000,90.000000,270.000000,0.000000,180.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-62 16','SPG-62 16','Phalanx FC','Phalanx FC','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=49.518002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.520000
    airDetectionDBObject.irSignature_dB=26.936001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S07.Cruiser Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=10.200000
    dbObj.beam_m=16.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=80000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
