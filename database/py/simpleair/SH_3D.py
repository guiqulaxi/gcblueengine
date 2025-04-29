# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='SH-3D'
    dbObj.natoClass='SH-3D'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=16000000.000000
    dbObj.weight_kg=5003.700195
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=1995.000000
    dbObj.country='USA'
    dbObj.designation='ASW'
    dbObj.imageList='sh3h.jpg'
    dbObj.iconFileName='air/AdvicoSH3D.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AQS-13B DS Active','AQS-13B DS Passive','ASQ-81 MAD','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','LN-66 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=138.100006
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=14.000000
    dbObj.mfFuelCapacity_kg=1941.000000
    dbObj.mfFuelRate_kgps=0.159590
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='SH-3D durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['SH-2F Launcher','10 DICASS Launcher','10 LOFAR Launcher','30 DIFAR Launcher']
    dbObj.maMagazineClass=['Cargo 3']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.810000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.750000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_L_2'
    airDetectionDBObject.IR_ModelB='IR_Rot_L_2'
    airDetectionDBObject.IR_ModelC='IR_Rot_L_2'
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
    dbObj.maxTakeoffWeight_kg=8664.000000
    dbObj.maxAltitude_m=4481.000000
    dbObj.climbRate_mps=11.000000
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
