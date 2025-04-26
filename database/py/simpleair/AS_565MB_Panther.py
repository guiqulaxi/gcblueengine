# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='AS 565MB Panther'
    dbObj.natoClass='AS 565MB Panther'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=0.000000
    dbObj.weight_kg=2380.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Italy'
    dbObj.designation='ASW'
    dbObj.imageList='as355.jpg'
    dbObj.iconFileName='air/AdvicoAS565MB.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','ORB 32']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=165.000000
    dbObj.mfAccel_ktsps=4.000000
    dbObj.mfTurnRate_degps=18.000000
    dbObj.mfFuelCapacity_kg=907.000000
    dbObj.mfFuelRate_kgps=0.094000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='AS 565MB Panther durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['AS565 Launcher','AS565 Launcher','24 DIFAR Launcher','8 DICASS Launcher','8 LOFAR Launcher']
    dbObj.maMagazineClass=['Cargo 3']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=4.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.460000
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
    dbObj.maxTakeoffWeight_kg=4300.000000
    dbObj.maxAltitude_m=3400.000000
    dbObj.climbRate_mps=6.500000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=3600.000000
    dbObj.CalculateParams()
    return dbObj
