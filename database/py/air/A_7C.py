# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='A-7C'
    dbObj.natoClass='A-7C'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=28000000.000000
    dbObj.weight_kg=7815.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1968.833008
    dbObj.finalYear=1981.000000
    dbObj.country='USA'
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoA7C.jpg'
    dbObj.mz3DModelFileName='A-7D_SEA.xml'
    dbObj.notes='    '
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','APQ-126','APR-25 RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=800.000000
    dbObj.mfAccel_ktsps=22.389999
    dbObj.mfTurnRate_degps=14.000000
    dbObj.mfFuelCapacity_kg=4546.299805
    dbObj.mfFuelRate_kgps=0.950000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='A-7C durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['A7 1-8','A7 2-7','A7 3-6','A7 Chin','20mm Colt Mk-12 Cannon (600)','ALE-29 CMs','ALE-29 CMs']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.420000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.200000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=19051.000000
    dbObj.maxAltitude_m=12496.000000
    dbObj.climbRate_mps=40.099998
    dbObj.gmax=7.000000
    dbObj.minimumRunway_m=1500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=54269.199219
    dbObj.militaryThrustSpeedSlope=0.002200
    dbObj.mfAfterburnThrust_N=54269.199219
    dbObj.abThrustSpeedSlope=0.002200
    dbObj.mfAfterburnFuelRate_kgps=0.950000
    dbObj.mfCdpsub=0.650000
    dbObj.mfCdptran=0.975000
    dbObj.mfCdpsup=0.780000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=126.668999
    dbObj.stallSpeed_mps=49.592400
    dbObj.thrustTable=[0.855000,0.700000,0.560000,0.452000,0.347000,0.274000,0.170000,0.150000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[0.900000,0.870000,0.850000,0.875000,1.000000,1.250000,1.600000,10.000000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
