# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='MD-500 ASW'
    dbObj.natoClass='MD-500 ASW'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=0.000000
    dbObj.weight_kg=599.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1977.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Taiwan'
    dbObj.designation='ASW'
    dbObj.imageList='bo105.jpg'
    dbObj.iconFileName='air/AdvicoMD500ASW.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='[phoenixegmh]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ASQ-81 MAD','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','RDR-1400C']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=160.000000
    dbObj.mfAccel_ktsps=6.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=200.000000
    dbObj.mfFuelRate_kgps=0.060000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='MD-500 ASW durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['MD500 ASW Launcher']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[0.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=5.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.600000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_M_2'
    airDetectionDBObject.IR_ModelB='IR_Rot_M_2'
    airDetectionDBObject.IR_ModelC='IR_Rot_M_2'
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
    dbObj.maxTakeoffWeight_kg=1361.000000
    dbObj.maxAltitude_m=4205.000000
    dbObj.climbRate_mps=8.000000
    dbObj.gmax=2.500000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=30.000000
    dbObj.maintenanceMin_s=10800.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
