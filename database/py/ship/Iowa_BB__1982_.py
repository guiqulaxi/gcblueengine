# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Iowa BB (1982)'
    dbObj.natoClass='Iowa BB (1982)'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=100000000.000000
    dbObj.weight_kg=45000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.000000
    dbObj.finalYear=1993.000000
    dbObj.country='USA'
    dbObj.designation='BB'
    dbObj.imageList='iowa1984.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=270.299988
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPS-49 AS','SPS-67 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=0.025803
    dbObj.mfTurnRate_degps=0.741940
    dbObj.mfFuelCapacity_kg=3150000.000000
    dbObj.mfFuelRate_kgps=1.123301
    dbObj.mfToughness=685.000000
    dbObj.damageEffect='Iowa BB durability'
    dbObj.mnNumLaunchers=20
    dbObj.maLauncherClass=['16in Triple Mk-7','16in Triple Mk-7','16in Triple Mk-7','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','Mk-41 Mod1 VLS','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','Mk-137 SRBOC Launcher','Mk-137 SRBOC Launcher','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin']
    dbObj.maMagazineClass=['Iowa Secondary Magazine (1982)','Mk-41 VLS 32 Cell','Phalanx 0 x4 Store','Iowa Main Ammo Mag','Ship Helo Stores']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[4,1,2,3,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,30.000000,30.000000,30.000000,30.000000,0.000000,180.000000,180.000000,180.000000,180.000000,360.000000,360.000000,136.000000,136.000000,90.000000,90.000000,80.000000,80.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,45.000000,45.000000,315.000000,315.000000,0.000000,45.000000,135.000000,225.000000,315.000000,0.000000,0.000000,68.000000,292.000000,45.000000,315.000000,135.000000,225.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,20.000000,20.000000,20.000000,20.000000,90.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=59.344002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=31.584999
    airDetectionDBObject.irSignature_dB=25.315001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=15.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=23.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S09.Battle Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=11.330000
    dbObj.beam_m=32.970001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=212000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Quintuple Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
