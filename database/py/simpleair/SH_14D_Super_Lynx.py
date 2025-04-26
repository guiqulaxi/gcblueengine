# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='SH-14D Super Lynx'
    dbObj.natoClass='SH-14D Super Lynx'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=0.000000
    dbObj.weight_kg=2740.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Netherlands'
    dbObj.designation='ASW'
    dbObj.imageList='sh14d.jpg'
    dbObj.iconFileName='air/AdvicoSH14D.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AWARE-4','DUAV-4 DS Active','DUAV-4 DS Passive','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Model 200HP','Seaspray Mk1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=281.000000
    dbObj.mfAccel_ktsps=6.000000
    dbObj.mfTurnRate_degps=18.000000
    dbObj.mfFuelCapacity_kg=1043.000000
    dbObj.mfFuelRate_kgps=0.110000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='SH-14D Super Lynx durability'
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
    airDetectionDBObject.RCS_dBsm=4.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.490000
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
    dbObj.maxTakeoffWeight_kg=3343.000000
    dbObj.maxAltitude_m=4000.000000
    dbObj.climbRate_mps=11.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=7200.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
