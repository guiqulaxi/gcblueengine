# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Albion Class LPD'
    dbObj.natoClass='Albion Class LPD'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=225000000.000000
    dbObj.weight_kg=19558904.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2003.000000
    dbObj.finalYear=2999.989990
    dbObj.country='UK'
    dbObj.designation='LPD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes='[phoenixegmh]'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Centaur ESM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 1007','Type 996']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=18.000000
    dbObj.mfAccel_ktsps=0.027508
    dbObj.mfTurnRate_degps=0.830865
    dbObj.mfFuelCapacity_kg=2414160.000000
    dbObj.mfFuelRate_kgps=0.619010
    dbObj.mfToughness=254.000000
    dbObj.damageEffect='Albion Class LPD durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['30mm/77 GAU-8/A Goalkeeper','30mm/77 GAU-8/A Goalkeeper']
    dbObj.maMagazineClass=['Albion LPD Ammo Mag']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[270.000000,270.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=53.916000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=28.826000
    airDetectionDBObject.irSignature_dB=19.319000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S10.Carrier Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.100000
    dbObj.beam_m=28.900000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=42432.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Pad'
    dbObj.CalculateParams()
    return dbObj
