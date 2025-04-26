# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Poolster Improved AOR'
    dbObj.natoClass='Poolster Improved AOR'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=17357000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.485962
    dbObj.finalYear=2012.110962
    dbObj.country='Netherlands'
    dbObj.designation='AOR'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes='I don\'t know its range, using amsterdam class AOR as reference.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AWARE-4','Decca 1226','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SCOUT']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=40.000000
    dbObj.mfAccel_ktsps=0.022718
    dbObj.mfTurnRate_degps=1.329198
    dbObj.mfFuelCapacity_kg=1909270.000000
    dbObj.mfFuelRate_kgps=0.789209
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Poolster Improved AOR durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['30mm/77 GAU-8/A Goalkeeper']
    dbObj.maMagazineClass=['Goalkeeper x1 Store','Poolster Fuel Cargo','Poolster Buoy Cargo','Poolster Weapons Cargo']
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[290.000000]
    dbObj.launcherAz_deg=[180.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=53.138000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.330999
    airDetectionDBObject.irSignature_dB=18.599001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S003.Merchant Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.400000
    dbObj.beam_m=20.299999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=21000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
