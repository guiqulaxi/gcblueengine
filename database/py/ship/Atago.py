# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Atago'
    dbObj.natoClass='Atago'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=10100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2007.201050
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
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','FCS-2-21 1','NOLQ-2','OLT-3','OPS-20','OPS-28','OQR-2 TA','Phalanx FC','SPG-62 12','SPY-1D','SQS-53C Active','SQS-53C Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.146720
    dbObj.mfTurnRate_degps=1.358739
    dbObj.mfFuelCapacity_kg=1414000.000000
    dbObj.mfFuelRate_kgps=1.745664
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Atago durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['SSM-1B Quad','SSM-1B Quad','Mk-41 Mod2 VLS','Mk-41 Mod2 VLS','5/62 Mark 45 Mod 4','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['SH-60 1.2 Support','127mm Mk-45 680 rounds','Phalanx 1 x2 Store','Mk-41 VLS Mod2 96 Cell']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,360.000000,360.000000,330.000000,240.000000,340.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,0.000000,0.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,90.000000,90.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','SPG-62 12','SPG-62 12','','Phalanx FC','Phalanx FC','','']
    dbObj.launcherFireControl2=['','','FCS-2-21 1','FCS-2-21 1','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.391998
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.313999
    airDetectionDBObject.irSignature_dB=20.879999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
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
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
