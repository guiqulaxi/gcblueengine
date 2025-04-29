# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Su-25'
    dbObj.natoClass='Frogfoot'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=11000000.000000
    dbObj.weight_kg=10700.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Strike Fighter'
    dbObj.imageList='su25.jpg'
    dbObj.iconFileName='air/AdvicoSU25.jpg'
    dbObj.mz3DModelFileName='su-27.xml'
    dbObj.notes='No afterburner but gave it a 5% reserve for \'afterburner\' mode'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DISS-7 AS','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Laser-15km','SPO-15 RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=490.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=3500.000000
    dbObj.mfFuelRate_kgps=1.800000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Su-25 durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['Su-25 W1','Su-25 W2','Su-25 W3','Su-25 W4','AO-17A 30 mm','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','Gun','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,20.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['DISS-7 AS','Laser-15km','Laser-15km','Laser-15km','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.190000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=7.710000
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
    dbObj.maxTakeoffWeight_kg=18600.000000
    dbObj.maxAltitude_m=8000.000000
    dbObj.climbRate_mps=58.000000
    dbObj.gmax=6.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=90000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=94500.000000
    dbObj.abThrustSpeedSlope=0.000000
    dbObj.mfAfterburnFuelRate_kgps=1.000000
    dbObj.mfCdpsub=1.100000
    dbObj.mfCdptran=2.000000
    dbObj.mfCdpsup=1.700000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.800000,0.750000,0.300000,0.100000,0.010000,0.010000,0.010000,0.010000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,1.000000,1.200000,1.400000,2.000000,3.000000,4.000000,8.000000]
    dbObj.CalculateParams()
    return dbObj
