# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Truxtun CGN (84)'
    dbObj.natoClass='Truxtun CGN (84)'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=8927000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.250000
    dbObj.finalYear=1995.699951
    dbObj.country='USA'
    dbObj.designation='CA'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='TicoMk26.xml'
    dbObj.notes=''
    dbObj.length_m=172.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)2 ESM B.1','SLQ-32(v)2 ESM B.2','SLQ-32(v)2 ESM B.3','SPG-55 4','SPS-10','SPS-43 AS','SPS-48C AS','SQS-26 Active','SQS-26 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.109009
    dbObj.mfTurnRate_degps=1.401190
    dbObj.mfFuelCapacity_kg=1249780.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=759.000000
    dbObj.damageEffect='Truxtun CGN durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Mk-10 GMLS','127mm/54 (5in) Mk42','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['SH-2F 1.1 Support','127mm Mk-42 500 Rounds','Phalanx 1 x2 Store','Mk-10 Store 60']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[330.000000,300.000000,0.000000,0.000000,260.000000,260.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,330.000000,150.000000,135.000000,225.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-55 4','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=48.806000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.539000
    airDetectionDBObject.irSignature_dB=13.114000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.300000
    dbObj.beam_m=18.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=70000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
