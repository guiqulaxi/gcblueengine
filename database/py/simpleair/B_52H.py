# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='B-52H'
    dbObj.natoClass='B-52H'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=30000000.000000
    dbObj.weight_kg=83250.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1961.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Bomber'
    dbObj.imageList='b52h-1.jpg;b52h-2.jpg'
    dbObj.iconFileName='air/AdvicoB52H.jpg'
    dbObj.mz3DModelFileName='b-52.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AAQ-33 SNIPER-XR','ALQ-117','ALR-20 RWR','APQ-166','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=565.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=8.000000
    dbObj.mfFuelCapacity_kg=104850.000000
    dbObj.mfFuelRate_kgps=2.150000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='B-52H durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['B-52 Internal','B-52 Wing','B-52 Wing']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['Int','LW','RW']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=25.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.090000
    airDetectionDBObject.irSignature_dB=33.000000
    airDetectionDBObject.IR_ModelA='IR_FW_VL_H_LP_8_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_VL_H_LP_8_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_VL_H_LP_8_M0.85'
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
    dbObj.maxTakeoffWeight_kg=219600.000000
    dbObj.maxAltitude_m=15100.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=30.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
