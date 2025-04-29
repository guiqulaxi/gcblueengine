# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='F-117'
    dbObj.natoClass='F-117'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=50000.000000
    dbObj.weight_kg=13800.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.000000
    dbObj.finalYear=2008.000000
    dbObj.country='USA'
    dbObj.designation='Bomber'
    dbObj.imageList='f117.jpg'
    dbObj.iconFileName='air/AdvicoF117.jpg'
    dbObj.mz3DModelFileName='unknown.xml'
    dbObj.notes='Armament significantly increased as per http://www.f-117a.com/Specs.html.  Not only is it reasonable, the site is incredibly detailed in all other respects suggesting its accurate here too.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['F-117 DLIR','F-117 FLIR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=580.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=4.000000
    dbObj.mfFuelCapacity_kg=5000.000000
    dbObj.mfFuelRate_kgps=0.866000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F-117 durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['F-117-Bays']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[0.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['F-117 DLIR']
    dbObj.launcherFireControl2=['F-117 FLIR']
    dbObj.launcherIsReloadable=[False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-15.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.280000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='F-117M0.85'
    airDetectionDBObject.IR_ModelB='F-117M0.85'
    airDetectionDBObject.IR_ModelC='F-117M0.85'
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
    dbObj.maxTakeoffWeight_kg=23800.000000
    dbObj.maxAltitude_m=20000.000000
    dbObj.climbRate_mps=40.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=7200.000000
    dbObj.maintenanceMax_s=14400.000000
    dbObj.CalculateParams()
    return dbObj
