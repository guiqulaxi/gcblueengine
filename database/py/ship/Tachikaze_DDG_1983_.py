# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Tachikaze DDG(1983)'
    dbObj.natoClass='Tachikaze DDG(1983)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4800000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.000000
    dbObj.finalYear=2010.480957
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','OPS-11','OPS-17','OQS-3 Active','OQS-3 Passive','Phalanx FC','SPG-51C 1','SPS-52B']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.040376
    dbObj.mfTurnRate_degps=1.863721
    dbObj.mfFuelCapacity_kg=672000.000000
    dbObj.mfFuelRate_kgps=0.533329
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Tachikaze DDG durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Mk-13 Mod4 GMLS','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','127mm/54 (5in) Mk42','127mm/54 (5in) Mk42','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-112 ASROC']
    dbObj.maMagazineClass=['Phalanx 0 x2 Store','127mm Mk-42 500 Rounds','Japanese Ship Torpedo Racks','Mk-13 Mod4 Rotary Store 40']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,0.000000,0.000000,300.000000,300.000000,170.000000,170.000000,30.000000,30.000000,300.000000]
    dbObj.launcherAz_deg=[180.000000,90.000000,270.000000,0.000000,180.000000,90.000000,270.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-51C 1','','','','','Phalanx FC','Phalanx FC','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.764000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.091999
    airDetectionDBObject.irSignature_dB=20.624001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.600000
    dbObj.beam_m=14.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
