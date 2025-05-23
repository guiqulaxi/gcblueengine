# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='AH-64A'
    dbObj.natoClass='AH-64A'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=15400000.000000
    dbObj.weight_kg=5165.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Attack'
    dbObj.imageList='ah64.jpg'
    dbObj.iconFileName='air/AdvicoAH64A.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Apache FLIR','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Laser-20km']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=158.000000
    dbObj.mfAccel_ktsps=12.500000
    dbObj.mfTurnRate_degps=35.000000
    dbObj.mfFuelCapacity_kg=1400.000000
    dbObj.mfFuelRate_kgps=0.120000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='AH-64A durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['30mm M230 Chain Gun','AH-64 pylons 1-5','AH-64 pylons 2-4']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[270.000000,5.000000,5.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Laser-20km','Laser-20km']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.390000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.870000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_S_2V'
    airDetectionDBObject.IR_ModelB='IR_Rot_S_2V'
    airDetectionDBObject.IR_ModelC='IR_Rot_S_2V'
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
    dbObj.maxTakeoffWeight_kg=10433.000000
    dbObj.maxAltitude_m=6400.000000
    dbObj.climbRate_mps=12.700000
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
