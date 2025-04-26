# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Super Lynx Mk 88A'
    dbObj.natoClass='Super Lynx Mk 88A'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=20000000.000000
    dbObj.weight_kg=3291.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation='ASW'
    dbObj.imageList='lnyxHAS3.jpg'
    dbObj.iconFileName='air/AdvicoLynxMk88A.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AQS-18 DS Active','AQS-18 DS Passive','ESM-1','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Sea Spray Mk3']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=174.000000
    dbObj.mfAccel_ktsps=10.100000
    dbObj.mfTurnRate_degps=22.000000
    dbObj.mfFuelCapacity_kg=790.000000
    dbObj.mfFuelRate_kgps=0.115680
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Super Lynx Mk 88A durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['Lynx HAS.2 left Pylon','Lynx HAS.2 right Pylon']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.390000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.490000
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
    dbObj.maxTakeoffWeight_kg=5330.000000
    dbObj.maxAltitude_m=2575.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
