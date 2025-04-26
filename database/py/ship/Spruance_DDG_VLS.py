# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Spruance DDG VLS'
    dbObj.natoClass='Spruance DDG VLS'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=8040000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.040039
    dbObj.finalYear=1993.959961
    dbObj.country='USA'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Mk-91 FCS','Phalanx FC','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPS-40B','SPS-55','SQR-19B TA','SQS-53C Active','SQS-53C Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.176580
    dbObj.mfTurnRate_degps=1.547102
    dbObj.mfFuelCapacity_kg=1125600.000000
    dbObj.mfFuelRate_kgps=1.042213
    dbObj.mfToughness=607.000000
    dbObj.damageEffect='Spruance DDG durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Mk-41 Mod1 VLS','Mk-41 Mod1 VLS','Mk-41 Mod1 VLS','SeaSparrow x8 Launcher','5/54 Mark 45 Mods 0 - 2','5/54 Mark 45 Mods 0 - 2','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher']
    dbObj.maMagazineClass=['SH-2F 2.3 Support','Phalanx 1 x2 Store','127mm Mk-45 1200 rounds','Mk-41 VLS Mod1 61 Cell']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,300.000000,320.000000,290.000000,290.000000,220.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,1.000000,2.000000,180.000000,0.000000,180.000000,45.000000,250.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,90.000000,90.000000,40.000000,0.000000,0.000000,0.000000,0.000000,40.000000,40.000000]
    dbObj.launcherFireControl=['','','','Mk-91 FCS','SPS-55','SPS-55','Phalanx FC','Phalanx FC','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=48.124001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.973000
    airDetectionDBObject.irSignature_dB=24.840000
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
    dbObj.draft_m=8.800000
    dbObj.beam_m=16.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=80000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
