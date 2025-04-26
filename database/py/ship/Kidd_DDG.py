# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Kidd DDG'
    dbObj.natoClass='Kidd DDG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=9200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.229980
    dbObj.finalYear=1999.729980
    dbObj.country='USA'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SPG-51D 8','SPS-48(E) AS','SPS-49(v)5','SPS-55','SQS-53B Active','SQS-53B Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.166100
    dbObj.mfTurnRate_degps=1.455745
    dbObj.mfFuelCapacity_kg=1288000.000000
    dbObj.mfFuelRate_kgps=1.192582
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Kidd DDG durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Mk-26 Mod0','Mk-26 Mod1','5/54 Mark 45 Mods 0 - 2','5/54 Mark 45 Mods 0 - 2','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['SH-60 1.2 Support','Mk-26 Mod0 + Mod1 Store','127mm Mk-45 1200 rounds','Phalanx 0 x1 Store']
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,330.000000,320.000000,300.000000,0.000000,0.000000,330.000000,330.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,90.000000,270.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-51D 8','SPG-51D 8','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=49.001999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.382999
    airDetectionDBObject.irSignature_dB=24.875999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.600000
    dbObj.beam_m=16.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=80000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='OHP Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
