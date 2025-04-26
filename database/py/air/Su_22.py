# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Su-22'
    dbObj.natoClass='Fitter-F'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=1000000.000000
    dbObj.weight_kg=10445.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1977.000000
    dbObj.finalYear=1995.000000
    dbObj.country='Russia'
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoSU22.jpg'
    dbObj.mz3DModelFileName='SU-17M3 Fitter.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Fon LRFD']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1400.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=16.000000
    dbObj.mfFuelCapacity_kg=3800.000000
    dbObj.mfFuelRate_kgps=2.087500
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Su-22 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['30mm NR-30 x2','Su-17 Fuselage','Su-22 W1','Su-22 W2','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','CM1','CM2']
    dbObj.launcherFOV_deg=[20.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Fon LRFD','Fon LRFD','Fon LRFD','','']
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
    dbObj.maxTakeoffWeight_kg=18940.000000
    dbObj.maxAltitude_m=15400.000000
    dbObj.climbRate_mps=200.000000
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=1300.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=78400.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=112700.000000
    dbObj.abThrustSpeedSlope=0.003700
    dbObj.mfAfterburnFuelRate_kgps=5.746100
    dbObj.mfCdpsub=1.145000
    dbObj.mfCdptran=1.700000
    dbObj.mfCdpsup=2.540000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.900000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,1.000000,1.000000,0.740000,0.230000,0.100000,0.005000,0.001000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,0.970000,0.940000,1.100000,1.900000,3.000000,6.000000,6.000000]
    dbObj.CalculateParams()
    return dbObj
