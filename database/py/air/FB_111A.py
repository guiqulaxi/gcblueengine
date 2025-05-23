# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='FB-111A'
    dbObj.natoClass='FB-111A'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=290000000.000000
    dbObj.weight_kg=22262.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1968.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Bomber'
    dbObj.imageList='fb111.jpg'
    dbObj.iconFileName='air/AdvicoFB111A.jpg'
    dbObj.mz3DModelFileName='tu-22.xml'
    dbObj.notes='set for 4200 - 4300 km range on internal fuel. http://www.castleairmuseum.org/generaldynamics_fb111a.html'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-161A ESM','APQ-164','AVQ-12 LASER','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1287.000000
    dbObj.mfAccel_ktsps=6.510000
    dbObj.mfTurnRate_degps=23.320000
    dbObj.mfFuelCapacity_kg=15325.700195
    dbObj.mfFuelRate_kgps=3.310000
    dbObj.mfToughness=3.000000
    dbObj.damageEffect='FB-111A durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['FB-111 Bay1','FB-111 Bay2','FB-111 2-5','FB-111 3-4','CM Ejector','CM Ejector']
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
    airDetectionDBObject.opticalCrossSection_dBsm=8.160000
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
    dbObj.maxTakeoffWeight_kg=54076.000000
    dbObj.maxAltitude_m=20000.000000
    dbObj.climbRate_mps=101.599998
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=40.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=109865.601562
    dbObj.militaryThrustSpeedSlope=0.001000
    dbObj.mfAfterburnThrust_N=181033.593750
    dbObj.abThrustSpeedSlope=0.003500
    dbObj.mfAfterburnFuelRate_kgps=11.000000
    dbObj.mfCdpsub=1.200000
    dbObj.mfCdptran=2.600000
    dbObj.mfCdpsup=2.200000
    dbObj.mfMcm=1.000000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=102.190002
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[0.900000,0.780000,0.730000,0.680000,0.600000,0.480000,0.280000,0.050000,0.010000,0.010000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,1.100000,1.200000,1.400000,2.300000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
