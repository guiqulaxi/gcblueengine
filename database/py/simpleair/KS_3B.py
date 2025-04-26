# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='KS-3B'
    dbObj.natoClass='KS-3B'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=27000000.000000
    dbObj.weight_kg=12000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Tanker'
    dbObj.imageList='S-3B.jpg'
    dbObj.iconFileName='air/AdvicoKS3B.jpg'
    dbObj.mz3DModelFileName='viking.xml'
    dbObj.notes='fuel outflow sourced from http://dimo.com/inflight_refueling.htm.  Assuming one buddy outflow pod, and one 370 gallon tank, for a combined fuel of 2020kG, and a combined weight of 2320kg.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALR-76 ESM','APS-137','ASQ-81 MAD','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=429.000000
    dbObj.mfAccel_ktsps=15.000000
    dbObj.mfTurnRate_degps=12.000000
    dbObj.mfFuelCapacity_kg=7920.000000
    dbObj.mfFuelRate_kgps=0.323000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='KS-3B durability'
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
    airDetectionDBObject.RCS_dBsm=11.760000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=11.970000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_F_HP_2_M0.85'
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
    dbObj.maxAltitude_m=11000.000000
    dbObj.climbRate_mps=20.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=1
    dbObj.fuelOut_kgps=11.143000
    dbObj.fuelIn_kgps=30.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
