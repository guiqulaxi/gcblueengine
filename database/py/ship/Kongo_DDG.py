# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Kongo DDG'
    dbObj.natoClass='Kongo DDG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=9485000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1993.229980
    dbObj.finalYear=3000.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='NOT FINISHED'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','NOLQ-2','OLT-3','OPS-28','OQR-2 TA','OQS-102 Active','OQS-102 Passive','SPG-62 12','SPY-1D']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.154283
    dbObj.mfTurnRate_degps=1.396032
    dbObj.mfFuelCapacity_kg=1327900.000000
    dbObj.mfFuelRate_kgps=1.639369
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Kongo DDG durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1','127 mm/54 (5in) Compact','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','Mk-41 Mod2 VLS','Mk-41 Mod2 VLS','Mk-41 Mod2 VLS','Type 68 Triple Tubes','Type 68 Triple Tubes']
    dbObj.maMagazineClass=['SH-60 1.2 Support','127mm Mk-45 680 rounds','Phalanx 1 x2 Store','Mk-41 VLS Mod2 90 Cell']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,240.000000,90.000000,270.000000,0.000000,0.000000,0.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,40.000000,40.000000,90.000000,90.000000,90.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','SPG-62 12','SPG-62 12','SPG-62 12','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=49.201000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.211000
    airDetectionDBObject.irSignature_dB=21.827999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.200000
    dbObj.beam_m=21.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=100000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Pad'
    dbObj.CalculateParams()
    return dbObj
