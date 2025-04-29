# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 42 DDG Batch 1'
    dbObj.natoClass='Type 42 DDG Batch 1'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=20000000.000000
    dbObj.weight_kg=4100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.130005
    dbObj.finalYear=2005.530029
    dbObj.country='UK'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=119.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 1022','Type-184 Active','Type-184 Passive','Type-909 FC','Type-992 SS','UAA-2 ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.198649
    dbObj.mfTurnRate_degps=1.989197
    dbObj.mfFuelCapacity_kg=574000.000000
    dbObj.mfFuelRate_kgps=0.717494
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 42 DDG Batch 1 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','Sea Dart Twin Rail Launcher','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','114mm/55(4.5in) Mark 8 Mod 0']
    dbObj.maMagazineClass=['Lynx 1.2 Support','114mm/55(4.5in) mk8 800 rounds','Sea Dart magazine 22','Phalanx 0 x2 Store']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[175.000000,175.000000,300.000000,40.000000,40.000000,330.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,270.000000,90.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,40.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','Type-909 FC','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.737000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.622999
    airDetectionDBObject.irSignature_dB=23.688000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.800000
    dbObj.beam_m=14.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=55340.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Type-42 Helo Deck'
    dbObj.CalculateParams()
    return dbObj
