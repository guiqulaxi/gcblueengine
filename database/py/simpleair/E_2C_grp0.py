# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='E-2C grp0'
    dbObj.natoClass='E-2C grp0'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=17090.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.000000
    dbObj.finalYear=1987.000000
    dbObj.country='USA'
    dbObj.designation='AEW'
    dbObj.imageList='e2c-001.jpg;e2c-020914.jpg'
    dbObj.iconFileName='air/AdvicoE2C0.jpg'
    dbObj.mz3DModelFileName='e2c.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALR-73 ESM','APS-138','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=338.000000
    dbObj.mfAccel_ktsps=6.000000
    dbObj.mfTurnRate_degps=9.000000
    dbObj.mfFuelCapacity_kg=5624.000000
    dbObj.mfFuelRate_kgps=0.250000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='E-2C grp0 durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
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
    airDetectionDBObject.RCS_dBsm=10.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=11.100000
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
    dbObj.maxTakeoffWeight_kg=23391.000000
    dbObj.maxAltitude_m=9300.000000
    dbObj.climbRate_mps=13.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=28800.000000
    dbObj.maintenanceMax_s=28800.000000
    dbObj.CalculateParams()
    return dbObj
