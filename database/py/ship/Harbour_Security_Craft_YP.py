# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Harbour Security Craft YP'
    dbObj.natoClass='Harbour Security Craft YP'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3900.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.099976
    dbObj.finalYear=3000.000000
    dbObj.country='USA'
    dbObj.designation='YP'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-0.5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Generic Radar 20km SS']
    sensorPlatformDBObject.sensorAz=[1.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=22.000000
    dbObj.mfAccel_ktsps=0.541274
    dbObj.mfTurnRate_degps=34.840103
    dbObj.mfFuelCapacity_kg=780.000000
    dbObj.mfFuelRate_kgps=0.019555
    dbObj.mfToughness=0.060000
    dbObj.damageEffect='Harbour Security Craft YP durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['0.30in GAU-17']
    dbObj.maMagazineClass=['.30cal x1 Ammo Box']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[240.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-1.588000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.029000
    airDetectionDBObject.irSignature_dB=16.188999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=0.700000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.000000
    dbObj.beam_m=2.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=330.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=1.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
