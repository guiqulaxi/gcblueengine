# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='MiG-23'
    dbObj.natoClass='MiG-23'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=10000000.000000
    dbObj.weight_kg=10460.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=1997.000000
    dbObj.country='Russia'
    dbObj.designation='Fighter'
    dbObj.imageList='mig23.jpg'
    dbObj.iconFileName='air/AdvicoMiG23.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes='4600kg internal fuel. One 800 liter drop tank with 639 kg. http://www.fas.org/nuke/guide/russia/airdef/mig-23.htm . Took ferry range of 2820 from wikipedia. Scaled by 0.88 for drop tank, gives about 2500-2600 km range'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['RP-21 Sapfir','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','SPO-15 RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1350.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=16.000000
    dbObj.mfFuelCapacity_kg=3530.000000
    dbObj.mfFuelRate_kgps=1.750000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='MiG-23 durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['MiG-23 Fuselage','MiG-23 W1','MiG-23 W2']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['F','Wing','IW']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['RP-21 Sapfir','RP-21 Sapfir','RP-21 Sapfir']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.620000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.260000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_VL_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_VL_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_VL_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=20670.000000
    dbObj.maxAltitude_m=18500.000000
    dbObj.climbRate_mps=240.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=83600.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=127000.000000
    dbObj.abThrustSpeedSlope=0.004000
    dbObj.mfAfterburnFuelRate_kgps=10.000000
    dbObj.mfCdpsub=1.000000
    dbObj.mfCdptran=2.400000
    dbObj.mfCdpsup=2.000000
    dbObj.mfMcm=1.140000
    dbObj.mfMsupm=1.250000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.800000,0.750000,0.700000,0.550000,0.350000,0.100000,0.050000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,0.850000,0.850000,1.000000,1.400000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
