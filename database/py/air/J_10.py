# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='J-10'
    dbObj.natoClass='J-10'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=9750.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2005.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='Fighter Multi'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoJ10.jpg'
    dbObj.mz3DModelFileName='f-16.xml'
    dbObj.notes='unknown fuel capacity, assuming a fuel fraction of 0.3'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','KLJ-10','SPO-32 Pastel ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1300.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=2925.000000
    dbObj.mfFuelRate_kgps=1.507300
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='J-10 durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['J-10 OWing 1-11','J-10 MWing 2-10','J-10 IWing 3-9','J-10 Fuselage 4-8','J-10 Center 6','CM Ejector','CM Ejector','23mm Type 23']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=0.000000
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
    dbObj.maxTakeoffWeight_kg=18500.000000
    dbObj.maxAltitude_m=18000.000000
    dbObj.climbRate_mps=315.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=350.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=15.000000
    dbObj.maintenanceMin_s=5400.000000
    dbObj.maintenanceMax_s=5400.000000
    dbObj.militaryThrust_N=79400.000000
    dbObj.militaryThrustSpeedSlope=0.000950
    dbObj.mfAfterburnThrust_N=122600.000000
    dbObj.abThrustSpeedSlope=0.002400
    dbObj.mfAfterburnFuelRate_kgps=6.669600
    dbObj.mfCdpsub=1.265000
    dbObj.mfCdptran=1.725000
    dbObj.mfCdpsup=1.150000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.780000,0.650000,0.530000,0.390000,0.190000,0.030000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,1.050000,1.100000,1.350000,2.100000,2.500000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
