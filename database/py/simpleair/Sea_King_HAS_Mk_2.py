# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Sea King HAS.Mk.2'
    dbObj.natoClass='Sea King HAS.Mk.2'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=20000000.000000
    dbObj.weight_kg=5382.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='ASW'
    dbObj.imageList='seakingHAS6.jpg'
    dbObj.iconFileName='air/AdvicoSeaKingHAS2A.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','ESM-1','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Type 195 DS Active']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=144.000000
    dbObj.mfAccel_ktsps=7.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=2552.964111
    dbObj.mfFuelRate_kgps=0.162000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Sea King HAS.Mk.2 durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['Sea king HAS.2 pylon','Sea king HAS.2 pylon','10 DICASS Launcher','10 LOFAR Launcher','30 DIFAR Launcher']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.390000
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
    dbObj.maxTakeoffWeight_kg=9752.000000
    dbObj.maxAltitude_m=4500.000000
    dbObj.climbRate_mps=10.300000
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
