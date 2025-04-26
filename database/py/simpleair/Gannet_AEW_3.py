# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Gannet AEW.3'
    dbObj.natoClass='Gannet AEW.3'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=6590.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1959.000000
    dbObj.finalYear=1977.400024
    dbObj.country='UK'
    dbObj.designation='AEW'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoGannetAEW3.jpg'
    dbObj.mz3DModelFileName='e2c.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APS-20E','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=217.000000
    dbObj.mfAccel_ktsps=8.000000
    dbObj.mfTurnRate_degps=12.000000
    dbObj.mfFuelCapacity_kg=2223.000000
    dbObj.mfFuelRate_kgps=0.123500
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Gannet AEW.3 durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[]
    dbObj.launcherName=[]
    dbObj.launcherFOV_deg=[]
    dbObj.launcherAz_deg=[]
    dbObj.launcherEl_deg=[]
    dbObj.launcherFireControl=[]
    dbObj.launcherFireControl2=[]
    dbObj.launcherIsReloadable=[]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=8.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=10.000000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_H_TP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_H_TP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_H_TP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=10200.000000
    dbObj.maxAltitude_m=7600.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
