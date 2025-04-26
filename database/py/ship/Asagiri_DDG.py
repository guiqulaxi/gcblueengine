# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Asagiri DDG'
    dbObj.natoClass='Asagiri DDG'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1988.000000
    dbObj.finalYear=2999.000000
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
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','OPS-24','OPS-28','OQR-1 TA','OQS-4 Active','OQS-4 Passive','Phalanx FC']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.167855
    dbObj.mfTurnRate_degps=1.907002
    dbObj.mfFuelCapacity_kg=588000.000000
    dbObj.mfFuelRate_kgps=0.816660
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Asagiri DDG durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','SeaSparrow x8 Launcher','76 mm/62 Mark 75 Compact','20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-112 ASROC']
    dbObj.maMagazineClass=['SH-60 1.2 Support','76mm/62 mk75 240 rounds','Phalanx 0 x2 Store','Sea Sparrow Reloads']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,330.000000,170.000000,170.000000,30.000000,30.000000,300.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,180.000000,0.000000,90.000000,270.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','OPS-28','','Phalanx FC','Phalanx FC','','','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.894001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.955000
    airDetectionDBObject.irSignature_dB=21.599001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.500000
    dbObj.beam_m=14.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=54000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
