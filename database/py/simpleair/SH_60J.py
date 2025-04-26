# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='SH-60J'
    dbObj.natoClass='SH-60J'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=20000000.000000
    dbObj.weight_kg=5000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation='ASW'
    dbObj.imageList='sh60f.jpg'
    dbObj.iconFileName='air/AdvicoSH60J.JPG'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AQS-13F DS Active','AQS-13F DS Passive','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=140.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=18.000000
    dbObj.mfFuelCapacity_kg=1870.560059
    dbObj.mfFuelRate_kgps=0.168000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='SH-60J durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['SH-60B Left Inner','SH-60B Right','CM Ejector','CM Ejector','5 DICASS Launcher','5 LOFAR Launcher','15 DIFAR Launcher']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','ALE-139','ALE-139','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.390000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.360000
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
    dbObj.maxTakeoffWeight_kg=9750.000000
    dbObj.maxAltitude_m=5790.000000
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
