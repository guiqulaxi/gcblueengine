# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F-111E'
    dbObj.natoClass='F-111E'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=290000000.000000
    dbObj.weight_kg=22808.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Bomber'
    dbObj.imageList='f111.jpg'
    dbObj.iconFileName='air/AdvicoF111E.jpg'
    dbObj.mz3DModelFileName='tu-22.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-161A ESM','APQ-164','AVQ-12 LASER','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1263.000000
    dbObj.mfAccel_ktsps=8.030000
    dbObj.mfTurnRate_degps=23.969999
    dbObj.mfFuelCapacity_kg=15325.700195
    dbObj.mfFuelRate_kgps=3.900000
    dbObj.mfToughness=3.000000
    dbObj.damageEffect='F-111E durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['F-111 Bay1','F-111 Bay2','F-111 2-5','F-111 3-4','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['B1','B2','OW','IW','CM2','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APQ-164','APQ-164','APQ-164','APQ-164','','']
    dbObj.launcherFireControl2=['AVQ-12 LASER','AVQ-12 LASER','AVQ-12 LASER','AVQ-12 LASER','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=7.940000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_H_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_H_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_H_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=45350.000000
    dbObj.maxAltitude_m=20000.000000
    dbObj.climbRate_mps=131.179993
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=900.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=40.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=95667.101562
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=164631.406250
    dbObj.abThrustSpeedSlope=0.002000
    dbObj.mfAfterburnFuelRate_kgps=12.000000
    dbObj.mfCdpsub=1.200000
    dbObj.mfCdptran=2.500000
    dbObj.mfCdpsup=2.200000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=102.190002
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[1.000000,0.780000,0.600000,0.500000,0.400000,0.350000,0.250000,0.200000,0.010000,0.010000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.250000,1.800000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
