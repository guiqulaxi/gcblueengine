# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Arleigh Burke IIA DDGHM'
    dbObj.natoClass='Arleigh Burke IIA DDGHM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=1000000000.000000
    dbObj.weight_kg=9200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2000.630005
    dbObj.finalYear=3000.000000
    dbObj.country='USA'
    dbObj.designation='DD'
    dbObj.imageList='burkeIIa.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPG-62 12','SPS-67(V)3 SS','SPY-1D','SQS-53C Active','SQS-53C Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.202706
    dbObj.mfTurnRate_degps=1.470448
    dbObj.mfFuelCapacity_kg=1288000.000000
    dbObj.mfFuelRate_kgps=1.626249
    dbObj.mfToughness=715.000000
    dbObj.damageEffect='Arleigh Burke IIA DDGHM durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['Mk-41 Mod2 VLS','Mk-41 Mod2 VLS','Mk-41 Mod2 VLS','ESSM 4x4 Launcher','ESSM 4x4 Launcher','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','5/62 Mark 45 Mod 4','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['SH-60 2.2 Support','Mk-41 VLS Mod2 96 Cell','127mm Mk-45 680 rounds','Phalanx 1 x2 Store']
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,300.000000,300.000000,270.000000,270.000000,0.000000,0.000000,320.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,90.000000,270.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,90.000000,90.000000,40.000000,40.000000,0.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-62 12','SPG-62 12','SPG-62 12','SPG-62 12','SPG-62 12','Phalanx FC','Phalanx FC','','','SPY-1D','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=45.992001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.416000
    airDetectionDBObject.irSignature_dB=27.327000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.300000
    dbObj.beam_m=20.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=106000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Burke Helo Deck'
    dbObj.CalculateParams()
    return dbObj
