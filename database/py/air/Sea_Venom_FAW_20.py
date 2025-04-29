# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Sea Venom FAW.20'
    dbObj.natoClass='Sea Venom FAW.20'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=3274.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1954.000000
    dbObj.finalYear=1957.000000
    dbObj.country='UK'
    dbObj.designation='Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoSeaVenomFAW20.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AI 10','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=530.000000
    dbObj.mfAccel_ktsps=22.389999
    dbObj.mfTurnRate_degps=18.799999
    dbObj.mfFuelCapacity_kg=1173.000000
    dbObj.mfFuelRate_kgps=0.258500
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Sea Venom FAW.20 durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['20mm Hispano Cannon - Sea Venom','20mm Hispano Cannon - Sea Venom','20mm Hispano Cannon - Sea Venom','20mm Hispano Cannon - Sea Venom','Sea Venom Wings']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['20mm Cannon','20mm Cannon','20mm Cannon','20mm Cannon','Stores']
    dbObj.launcherFOV_deg=[20.000000,20.000000,20.000000,20.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.300000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=5670.000000
    dbObj.maxAltitude_m=13050.000000
    dbObj.climbRate_mps=24.400000
    dbObj.gmax=3.500000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=21581.000000
    dbObj.militaryThrustSpeedSlope=0.001000
    dbObj.mfAfterburnThrust_N=21581.000000
    dbObj.abThrustSpeedSlope=0.001000
    dbObj.mfAfterburnFuelRate_kgps=0.258500
    dbObj.mfCdpsub=0.750000
    dbObj.mfCdptran=1.500000
    dbObj.mfCdpsup=2.500000
    dbObj.mfMcm=0.700000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=90.000000
    dbObj.stallSpeed_mps=45.000000
    dbObj.thrustTable=[0.950000,0.900000,0.880000,0.750000,0.650000,0.440000,0.130000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,0.900000,0.950000,1.100000,1.500000,2.500000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
