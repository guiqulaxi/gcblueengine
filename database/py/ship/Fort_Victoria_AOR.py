# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Fort Victoria AOR'
    dbObj.natoClass='Fort Victoria AOR'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=36580000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1993.537964
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='AOR'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes='unknown range, assuming 9000nm at 16kts.'
    dbObj.length_m=203.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','Type 1007','Type 996']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=0.014726
    dbObj.mfTurnRate_degps=0.685930
    dbObj.mfFuelCapacity_kg=4023800.000000
    dbObj.mfFuelRate_kgps=1.103914
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Fort Victoria AOR durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1']
    dbObj.maMagazineClass=['Phalanx 0 x2 Store','Poolster Fuel Cargo','Poolster Buoy Cargo','Poolster Weapons Cargo']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[320.000000,320.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['Phalanx FC','Phalanx FC']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=57.993999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.923000
    airDetectionDBObject.irSignature_dB=18.879999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=32.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S003.Merchant Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=10.000000
    dbObj.beam_m=30.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=23904.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Quintuple Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
