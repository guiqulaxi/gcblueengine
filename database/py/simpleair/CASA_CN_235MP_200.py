# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='CASA CN-235MP-200'
    dbObj.natoClass='CASA CN-235MP-200'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=11700.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Columbia'
    dbObj.designation=''
    dbObj.imageList='casa235.jpg'
    dbObj.iconFileName='air/AdvicoCN235MP200.jpg'
    dbObj.mz3DModelFileName='c-130.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APS-504(V)5','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','WESCAM MX20']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=245.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=3124.000000
    dbObj.mfFuelRate_kgps=0.190000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='CASA CN-235MP-200 durability'
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
    airDetectionDBObject.RCS_dBsm=10.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=11.950000
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
    dbObj.maxTakeoffWeight_kg=15400.000000
    dbObj.maxAltitude_m=9145.000000
    dbObj.climbRate_mps=9.000000
    dbObj.gmax=2.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=27000.000000
    dbObj.maintenanceMax_s=27000.000000
    dbObj.CalculateParams()
    return dbObj
