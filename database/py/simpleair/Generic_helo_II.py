# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Generic helo II'
    dbObj.natoClass='Generic helo II'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=20000000.000000
    dbObj.weight_kg=5000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='air/helo_unk.jpg'
    dbObj.mz3DModelFileName='rah-66.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Generic radar']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=150.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=1000.000000
    dbObj.mfFuelRate_kgps=1.000000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Generic helo II durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['ASM Launcher']
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
    airDetectionDBObject.RCS_dBsm=10.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=7.900000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_M_1'
    airDetectionDBObject.IR_ModelB='IR_Rot_M_1'
    airDetectionDBObject.IR_ModelC='IR_Rot_M_1'
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
    dbObj.maxTakeoffWeight_kg=50000.000000
    dbObj.maxAltitude_m=1000.000000
    dbObj.climbRate_mps=20.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
