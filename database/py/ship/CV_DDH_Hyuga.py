# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV/DDH Hyuga'
    dbObj.natoClass='CV/DDH Hyuga'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=19000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2009.209961
    dbObj.finalYear=3000.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','FCS-3 AS','NOLQ-3','NOLQ-3C ECM','OPS-20','OQQ-21 Active']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.094448
    dbObj.mfTurnRate_degps=1.052963
    dbObj.mfFuelCapacity_kg=2090000.000000
    dbObj.mfFuelRate_kgps=1.548135
    dbObj.mfToughness=1512.000000
    dbObj.damageEffect='CV/DDH Hyuga durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['Mk-41 Mod4 VLS','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','324mm Torpedo Tube x 3 (Port)','324mm Torpedo Tube x 3 (Stbd)']
    dbObj.maMagazineClass=['Carrier Fuel Supply','Hyuga Aircraft Stores','Mk-41 VLS Mod4 16 Cell','Phalanx Store']
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[360.000000,150.000000,150.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[135.000000,300.000000,60.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[10.000000,10.000000,10.000000,10.000000,10.000000]
    dbObj.launcherFireControl=['FCS-3 AS','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=50.716999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.760000
    airDetectionDBObject.irSignature_dB=24.521000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=14.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.000000
    dbObj.beam_m=33.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=100000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Hyuga Flightdeck'
    dbObj.CalculateParams()
    return dbObj
