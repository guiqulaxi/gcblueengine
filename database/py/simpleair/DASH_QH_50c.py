# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='DASH QH-50c'
    dbObj.natoClass='DASH QH-50c'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=20000000.000000
    dbObj.weight_kg=524.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='ASW'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoQH50C.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=[]
    sensorPlatformDBObject.sensorAz=[]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=80.000000
    dbObj.mfAccel_ktsps=4.000000
    dbObj.mfTurnRate_degps=9.000000
    dbObj.mfFuelCapacity_kg=106.400002
    dbObj.mfFuelRate_kgps=0.033100
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='DASH QH-50c durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['QH-50C Launcher']
    dbObj.maMagazineClass=[]
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
    airDetectionDBObject.RCS_dBsm=3.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.260000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_S_1'
    airDetectionDBObject.IR_ModelB='IR_Rot_S_1'
    airDetectionDBObject.IR_ModelC='IR_Rot_S_1'
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
    dbObj.maxTakeoffWeight_kg=1036.000000
    dbObj.maxAltitude_m=5000.000000
    dbObj.climbRate_mps=10.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
