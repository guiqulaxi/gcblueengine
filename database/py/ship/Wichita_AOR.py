# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Wichita AOR'
    dbObj.natoClass='Wichita AOR'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=37360000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1969.432007
    dbObj.finalYear=1983.000000
    dbObj.country='USA'
    dbObj.designation='AOR'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes=''
    dbObj.length_m=201.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Mk-91 FCS','SPS-64 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=0.008909
    dbObj.mfTurnRate_degps=0.682811
    dbObj.mfFuelCapacity_kg=4109600.000000
    dbObj.mfFuelRate_kgps=0.924108
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Wichita AOR durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','3/50 Mark 33','3/50 Mark 33','3/50 Mark 33','3/50 Mark 33']
    dbObj.maMagazineClass=['76mm mk33 x2 store','Sea Sparrow Reloads','Wichita Cargo - Ammo','Wichita Cargo - Fuel']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[1,0,2,3]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[340.000000,270.000000,270.000000,135.000000,225.000000]
    dbObj.launcherAz_deg=[180.000000,35.000000,325.000000,135.000000,225.000000]
    dbObj.launcherEl_deg=[40.000000,270.000000,270.000000,320.000000,320.000000]
    dbObj.launcherFireControl=['Mk-91 FCS','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=58.132000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.891001
    airDetectionDBObject.irSignature_dB=22.277000
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
    dbObj.draft_m=11.000000
    dbObj.beam_m=29.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=32000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
