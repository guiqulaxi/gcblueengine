# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Su-20'
    dbObj.natoClass='Fitter-C'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=1000000.000000
    dbObj.weight_kg=10050.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.000000
    dbObj.finalYear=1991.000000
    dbObj.country='Russia'
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoSU20.jpg'
    dbObj.mz3DModelFileName='SU-17M3 Fitter.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','SRD-5K']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1400.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=16.000000
    dbObj.mfFuelCapacity_kg=3630.000000
    dbObj.mfFuelRate_kgps=1.936500
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Su-20 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['30mm NR-30 x2','Su-17 Fuselage','Su-20 W1','Su-20 W2','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','CM1','CM2']
    dbObj.launcherFOV_deg=[20.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','SRD-5K','SRD-5K','SRD-5K','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=8.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.770000
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
    dbObj.maxTakeoffWeight_kg=18370.000000
    dbObj.maxAltitude_m=15600.000000
    dbObj.climbRate_mps=200.000000
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=1200.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=79492.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=109835.000000
    dbObj.abThrustSpeedSlope=0.002900
    dbObj.mfAfterburnFuelRate_kgps=5.787700
    dbObj.mfCdpsub=1.000000
    dbObj.mfCdptran=1.353000
    dbObj.mfCdpsup=1.650000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.300000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,1.000000,1.000000,0.740000,0.160000,0.050000,0.005000,0.001000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,0.970000,0.940000,1.100000,1.900000,3.000000,6.000000,6.000000]
    dbObj.CalculateParams()
    return dbObj
