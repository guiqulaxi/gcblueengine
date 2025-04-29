# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Shirane DDH(1992)'
    dbObj.natoClass='Shirane DDH(1992)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=6800000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1992.000000
    dbObj.finalYear=2015.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=159.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','NOLQ-1','OLR-9B','OPS-12','OPS-28','OQR-1 TA','OQS-101 Active','OQS-101 Passive','Phalanx FC','SQS-35(J) VDS','WM-25']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.035807
    dbObj.mfTurnRate_degps=1.616006
    dbObj.mfFuelCapacity_kg=952000.000000
    dbObj.mfFuelRate_kgps=0.940239
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Shirane DDH durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','127mm/54 (5in) Mk42','127mm/54 (5in) Mk42','20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-112 ASROC']
    dbObj.maMagazineClass=['SH-3 3.3 Support','127mm Mk-42 500 Rounds','Phalanx 0 x2 Store','Sea Sparrow Reloads']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,320.000000,330.000000,170.000000,170.000000,30.000000,30.000000,300.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,180.000000,90.000000,270.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['WM-25','','','Phalanx FC','Phalanx FC','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.033001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.372999
    airDetectionDBObject.irSignature_dB=20.726999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.300000
    dbObj.beam_m=17.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=70000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Triple Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
