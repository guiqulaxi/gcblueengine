# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='KC-10A'
    dbObj.natoClass='KC-10A'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=88400000.000000
    dbObj.weight_kg=109328.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Tanker'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoKC10A.jpg'
    dbObj.mz3DModelFileName='civilairliner.xml'
    dbObj.notes='Scott Daniels [lancaster123]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=538.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=4.000000
    dbObj.mfFuelCapacity_kg=161480.000000
    dbObj.mfFuelRate_kgps=0.100000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='KC-10A durability'
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
    airDetectionDBObject.RCS_dBsm=20.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=17.049999
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_LP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=270808.000000
    dbObj.maxAltitude_m=12800.000000
    dbObj.climbRate_mps=7.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=1
    dbObj.fuelOut_kgps=20.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=3600.000000
    dbObj.CalculateParams()
    return dbObj
