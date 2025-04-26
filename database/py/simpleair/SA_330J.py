# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='SA-330J'
    dbObj.natoClass='SA-330J'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=20000000.000000
    dbObj.weight_kg=4273.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='Cargo'
    dbObj.imageList='sh60f.jpg'
    dbObj.iconFileName='air/AdvicoSA330J.JPG'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='http://www.evergreenaviation.com/ehi/specsheets/puma.html'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=138.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=1166.000000
    dbObj.mfFuelRate_kgps=0.161900
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='SA-330J durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=['Cargo 8']
    dbObj.magazineId=[0]
    dbObj.launcherId=[]
    dbObj.launcherName=[]
    dbObj.launcherFOV_deg=[]
    dbObj.launcherAz_deg=[]
    dbObj.launcherEl_deg=[]
    dbObj.launcherFireControl=[]
    dbObj.launcherFireControl2=[]
    dbObj.launcherIsReloadable=[]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.390000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.290000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='AirIR1'
    airDetectionDBObject.IR_ModelB='AirIR1'
    airDetectionDBObject.IR_ModelC='AirIR1'
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
    dbObj.maxTakeoffWeight_kg=7410.000000
    dbObj.maxAltitude_m=5029.000000
    dbObj.climbRate_mps=7.100000
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
