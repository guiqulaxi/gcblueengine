# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Wessex HAS.3'
    dbObj.natoClass='Wessex HAS.3'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=0.000000
    dbObj.weight_kg=3767.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=1990.000000
    dbObj.country='UK'
    dbObj.designation='ASW'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoWessex3.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARI 5955','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Type 195 DS Active']
    sensorPlatformDBObject.sensorAz=[180.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=106.000000
    dbObj.mfAccel_ktsps=6.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=1043.000000
    dbObj.mfFuelRate_kgps=0.115000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Wessex HAS.3 durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['Wessex Launcher','Wessex Launcher']
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
    airDetectionDBObject.RCS_dBsm=4.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.040000
    airDetectionDBObject.irSignature_dB=0.000000
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
    dbObj.maxTakeoffWeight_kg=6136.000000
    dbObj.maxAltitude_m=3660.000000
    dbObj.climbRate_mps=6.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=10800.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
