# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='MiG-29SM'
    dbObj.natoClass='Fulcrum-C'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=30000000.000000
    dbObj.weight_kg=10900.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1985.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='mig29.jpg'
    dbObj.iconFileName='air/AdvicoMiG29SM.jpg'
    dbObj.mz3DModelFileName='mig-29.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','N-019M Sapfir-29 Slot Back','SPO-15 RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1320.000000
    dbObj.mfAccel_ktsps=17.200001
    dbObj.mfTurnRate_degps=36.400002
    dbObj.mfFuelCapacity_kg=3200.000000
    dbObj.mfFuelRate_kgps=2.500000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='MiG-29SM durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['MiG-29SM Centerline','MiG-29SM W1','MiG-29SM W2','MiG-29SM W3','30mm NR-30','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,10.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','N-019M Sapfir-29 Slot Back','N-019M Sapfir-29 Slot Back','N-019M Sapfir-29 Slot Back','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=8.990000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.880000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=18400.000000
    dbObj.maxAltitude_m=17250.000000
    dbObj.climbRate_mps=330.000000
    dbObj.gmax=9.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=98800.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=162800.000000
    dbObj.abThrustSpeedSlope=0.003000
    dbObj.mfAfterburnFuelRate_kgps=9.450000
    dbObj.mfCdpsub=0.800000
    dbObj.mfCdptran=2.100000
    dbObj.mfCdpsup=1.700000
    dbObj.mfMcm=1.100000
    dbObj.mfMsupm=1.400000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[1.000000,1.000000,0.900000,0.800000,0.650000,0.470000,0.200000,0.010000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,1.000000,1.050000,1.200000,1.700000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
