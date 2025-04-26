# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Lightning F.Mk.6'
    dbObj.natoClass='Lightning F.Mk.6'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=12718.900391
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='Fighter'
    dbObj.imageList='lightning_f3.jpg'
    dbObj.iconFileName='air/AdvicoLightningMK6.jpg'
    dbObj.mz3DModelFileName='lightning.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Airpass 23','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1200.000000
    dbObj.mfAccel_ktsps=14.980000
    dbObj.mfTurnRate_degps=14.620000
    dbObj.mfFuelCapacity_kg=2600.000000
    dbObj.mfFuelRate_kgps=3.700000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Lightning F.Mk.6 durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['ADEN 30mm','ADEN 30mm/Firestreak','ADEN 30mm/Firestreak','ADEN 30mm']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[20.000000,20.000000,20.000000,20.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.150000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_S_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_S_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_S_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=18932.000000
    dbObj.maxAltitude_m=26600.000000
    dbObj.climbRate_mps=327.950012
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=113128.921875
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=145894.312500
    dbObj.abThrustSpeedSlope=0.002800
    dbObj.mfAfterburnFuelRate_kgps=11.730000
    dbObj.mfCdpsub=0.750000
    dbObj.mfCdptran=2.300000
    dbObj.mfCdpsup=2.000000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=87.300003
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[1.000000,0.930000,0.850000,0.800000,0.700000,0.510000,0.240000,0.130000,0.050000,0.020000]
    dbObj.fuelEfficiencyTable=[0.970000,0.990000,1.020000,1.030000,1.010000,1.060000,1.500000,2.270000,5.140000,8.000000]
    dbObj.CalculateParams()
    return dbObj
