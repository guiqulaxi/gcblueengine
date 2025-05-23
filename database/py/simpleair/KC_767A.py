# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='KC-767A'
    dbObj.natoClass='KC-767A'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=175000000.000000
    dbObj.weight_kg=82500.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2007.000000
    dbObj.finalYear=2030.000000
    dbObj.country='USA'
    dbObj.designation='Tanker'
    dbObj.imageList='kc767.jpg'
    dbObj.iconFileName='air/AdvicoKC767A.jpg'
    dbObj.mz3DModelFileName='kc767.xml'
    dbObj.notes='assumed fuel flow at least equal to the KC-135, 1000 gallons/min., http://www.youtube.com/watch?feature=player_embedded&v=rzZsH-KARu4'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=495.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=3.000000
    dbObj.mfFuelCapacity_kg=73000.000000
    dbObj.mfFuelRate_kgps=2.000000
    dbObj.mfToughness=10.000000
    dbObj.damageEffect='KC-767A durability'
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
    airDetectionDBObject.RCS_dBsm=21.200001
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=17.270000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_TP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_TP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_TP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=187000.000000
    dbObj.maxAltitude_m=12000.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=2
    dbObj.fuelOut_kgps=50.650002
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
