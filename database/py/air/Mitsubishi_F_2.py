# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Mitsubishi F-2'
    dbObj.natoClass='Mitsubishi F-2'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=127000000.000000
    dbObj.weight_kg=9527.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2000.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation='F'
    dbObj.imageList='f16a.jpg'
    dbObj.iconFileName='air/AdvicoF2.jpg'
    dbObj.mz3DModelFileName='f-16.xml'
    dbObj.notes='[phoenixegmh]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALR-69 RWR','APG-77','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','FLIR-15','LANTIRN']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1300.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=3228.000000
    dbObj.mfFuelRate_kgps=1.704570
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Mitsubishi F-2 durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Mitsubishi F-2 1-11','Mistubishi F-2 2-10','Mitsubishi F-2 3-9','Mitsubishi F-2 4-8','Mitsubishi F-2 4L-8L','Mitsubishi F-2 5-7','Mitsubishi F-2 6','ALE-40 CMD','ALE-40 CMD','M61A Cannon']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,5.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APG-77','APG-77','APG-77','APG-77','APG-77','APG-77','APG-77','','','APG-77']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=0.800000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.460000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_S_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_S_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_S_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=22090.000000
    dbObj.maxAltitude_m=18000.000000
    dbObj.climbRate_mps=315.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=1800.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=15.000000
    dbObj.maintenanceMin_s=5400.000000
    dbObj.maintenanceMax_s=5400.000000
    dbObj.militaryThrust_N=76000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=125000.000000
    dbObj.abThrustSpeedSlope=0.002000
    dbObj.mfAfterburnFuelRate_kgps=7.114570
    dbObj.mfCdpsub=0.800000
    dbObj.mfCdptran=1.400000
    dbObj.mfCdpsup=1.600000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,1.000000,0.840000,0.640000,0.180000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.060000,1.080000,1.060000,1.030000,1.000000,1.160000,3.000000,10.000000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
