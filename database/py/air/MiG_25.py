# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='MiG-25'
    dbObj.natoClass='MiG-25'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=25000000.000000
    dbObj.weight_kg=20000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1966.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Fighter'
    dbObj.imageList='mig25-1.jpg;mig25-2.jpg'
    dbObj.iconFileName='air/AdvicoMiG25.jpg'
    dbObj.mz3DModelFileName='mig-29.xml'
    dbObj.notes='updated from http://www.flymig.com/aircraft/MiG-25/'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','RP-25 Smerch radar','SPO-15 RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1835.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=12.000000
    dbObj.mfFuelCapacity_kg=14920.000000
    dbObj.mfFuelRate_kgps=10.378860
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='MiG-25 durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['MiG-25 W1','MiG-25 W2','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['OW','IW','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['RP-25 Smerch radar','RP-25 Smerch radar','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.520000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.420000
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
    dbObj.maxTakeoffWeight_kg=36720.000000
    dbObj.maxAltitude_m=27500.000000
    dbObj.climbRate_mps=208.000000
    dbObj.gmax=4.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=147102.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=219742.000000
    dbObj.abThrustSpeedSlope=0.003000
    dbObj.mfAfterburnFuelRate_kgps=33.571690
    dbObj.mfCdpsub=2.000000
    dbObj.mfCdptran=3.900000
    dbObj.mfCdpsup=3.000000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=30.000000
    dbObj.stallSpeed_mps=10.000000
    dbObj.thrustTable=[1.000000,1.025000,1.000000,1.000000,1.000000,0.800000,0.500000,0.300000,0.110000,0.030000]
    dbObj.fuelEfficiencyTable=[1.000000,1.050000,1.100000,1.150000,1.200000,1.300000,1.600000,2.175000,3.400000,6.000000]
    dbObj.CalculateParams()
    return dbObj
