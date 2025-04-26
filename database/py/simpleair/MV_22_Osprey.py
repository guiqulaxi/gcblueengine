# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='MV-22 Osprey'
    dbObj.natoClass='MV-22 Osprey'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=35000000.000000
    dbObj.weight_kg=15032.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2007.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Cargo'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoCH46E.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='Didn\'t bother with light machine guns, basically transport only. Maybe we need a \'cargo hook\' parameter for sling loading in the future'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AN/AAR-47','APR-44 RWR','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=275.000000
    dbObj.mfAccel_ktsps=15.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=5228.899902
    dbObj.mfFuelRate_kgps=0.683100
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='MV-22 Osprey durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['CM Ejector','CM Ejector']
    dbObj.maMagazineClass=['CH-53E Cargo']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['CM','CM']
    dbObj.launcherFOV_deg=[0.000000,0.000000]
    dbObj.launcherAz_deg=[180.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=15.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.650000
    airDetectionDBObject.irSignature_dB=22.000000
    airDetectionDBObject.IR_ModelA='AirIR1'
    airDetectionDBObject.IR_ModelB='AirIR1'
    airDetectionDBObject.IR_ModelC='AirIR1'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-999.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTakeoffWeight_kg=27400.000000
    dbObj.maxAltitude_m=7620.000000
    dbObj.climbRate_mps=11.800000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
