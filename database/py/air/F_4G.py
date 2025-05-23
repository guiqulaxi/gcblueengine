# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F-4G'
    dbObj.natoClass='F-4G'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=13104.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='f4e.jpg'
    dbObj.iconFileName='air/AdvicoF4G.jpg'
    dbObj.mz3DModelFileName='f-4.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APQ-120','APR-38 RHAW','AVQ-26 LASER','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1330.000000
    dbObj.mfAccel_ktsps=13.570000
    dbObj.mfTurnRate_degps=14.000000
    dbObj.mfFuelCapacity_kg=5690.000000
    dbObj.mfFuelRate_kgps=5.000000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F-4G durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['F-4G 1-9','F-4G 2-8','F-4G 3-7','F-4G 4-6','F-4G 5','ALE-29 CMs','ALE-29 CMs']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['OW','IW','FF','AF','C','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APQ-120','APQ-120','APQ-120','APQ-120','APQ-120','','']
    dbObj.launcherFireControl2=['AVQ-26 LASER','AVQ-26 LASER','AVQ-26 LASER','AVQ-26 LASER','AVQ-26 LASER','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.970000
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
    dbObj.maxTakeoffWeight_kg=28030.000000
    dbObj.maxAltitude_m=18300.000000
    dbObj.climbRate_mps=210.000000
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=105638.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=159303.000000
    dbObj.abThrustSpeedSlope=0.007000
    dbObj.mfAfterburnFuelRate_kgps=8.850000
    dbObj.mfCdpsub=0.690000
    dbObj.mfCdptran=2.400000
    dbObj.mfCdpsup=3.000000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=110.000000
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[0.900000,0.800000,0.700000,0.600000,0.500000,0.430000,0.200000,0.080000,0.010000,0.010000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,1.000000,1.000000,1.150000,1.700000,4.000000,60.000000,200.000000]
    dbObj.CalculateParams()
    return dbObj
