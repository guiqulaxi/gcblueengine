# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 82 DDG'
    dbObj.natoClass='Type 82 DDG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=20000000.000000
    dbObj.weight_kg=7700000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.239990
    dbObj.finalYear=1987.000000
    dbObj.country='UK'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-82.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-4','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 1022','Type-184 Active','Type-184 Passive','Type-909 FC','Type-992 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.035951
    dbObj.mfTurnRate_degps=1.460660
    dbObj.mfFuelCapacity_kg=1078000.000000
    dbObj.mfFuelRate_kgps=0.937383
    dbObj.mfToughness=250.000000
    dbObj.damageEffect='Type 82 DDG durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['Sea Dart Twin Rail Launcher','114mm/55(4.5in) Mark 8 Mod 0','30mm/75 GCM-AO3-2','30mm/75 GCM-AO3-2']
    dbObj.maMagazineClass=['30mm GCM-A03-2 x2 Store','114mm/55(4.5in) mk8 800 rounds','Sea Dart magazine 40']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[360.000000,300.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type-909 FC','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.842999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.552000
    airDetectionDBObject.irSignature_dB=23.861000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.500000
    dbObj.beam_m=16.760000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Pad'
    dbObj.CalculateParams()
    return dbObj
