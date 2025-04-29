# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV (R05/6/7) Invincible'
    dbObj.natoClass='CV (R05/6/7) Invincible'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=20600000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.520020
    dbObj.finalYear=2999.989990
    dbObj.country='UK'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='incv.xml'
    dbObj.notes=''
    dbObj.length_m=210.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-8','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 1022','Type 2016 Active','Type 2016 Passive','Type 996','Type-909 FC']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.092339
    dbObj.mfTurnRate_degps=0.974516
    dbObj.mfFuelCapacity_kg=2266000.000000
    dbObj.mfFuelRate_kgps=1.618557
    dbObj.mfToughness=1086.000000
    dbObj.damageEffect='CV (R05/6/7) Invincible durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['Sea Dart Twin Rail Launcher','30mm/77 GAU-8/A Goalkeeper','30mm/77 GAU-8/A Goalkeeper','30mm/77 GAU-8/A Goalkeeper']
    dbObj.maMagazineClass=['Carrier Fuel Supply','Sea Dart magazine 40','Goalkeeper Store','Invincible Carrier Magazine']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,190.000000,185.000000]
    dbObj.launcherAz_deg=[0.000000,345.000000,225.000000,90.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type-909 FC','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=54.254002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=30.548000
    airDetectionDBObject.irSignature_dB=24.139999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=14.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S10.Carrier Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.800000
    dbObj.beam_m=36.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=97200.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Invincible flight deck'
    dbObj.CalculateParams()
    return dbObj
