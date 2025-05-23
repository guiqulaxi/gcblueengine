# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Tu-128M'
    dbObj.natoClass='Fiddler B'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=26008.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1979.000000
    dbObj.finalYear=1990.000000
    dbObj.country='Russia'
    dbObj.designation='Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoTU128M.jpg'
    dbObj.mz3DModelFileName='tu-22.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','RP-SM Smerch-M']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1200.000000
    dbObj.mfAccel_ktsps=12.890000
    dbObj.mfTurnRate_degps=8.000000
    dbObj.mfFuelCapacity_kg=14854.000000
    dbObj.mfFuelRate_kgps=3.999960
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Tu-128M durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['R-4.3 Launcher','R-4.4 Launcher']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['RP-SM Smerch-M','RP-SM Smerch-M']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.970000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_VL_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_VL_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_VL_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=43013.000000
    dbObj.maxAltitude_m=15600.000000
    dbObj.climbRate_mps=40.000000
    dbObj.gmax=2.500000
    dbObj.minimumRunway_m=1350.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=150000.000000
    dbObj.militaryThrustSpeedSlope=0.000800
    dbObj.mfAfterburnThrust_N=215800.000000
    dbObj.abThrustSpeedSlope=0.001900
    dbObj.mfAfterburnFuelRate_kgps=12.607720
    dbObj.mfCdpsub=2.160000
    dbObj.mfCdptran=2.700000
    dbObj.mfCdpsup=1.800000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=110.000000
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[0.940000,0.830000,0.700000,0.590000,0.480000,0.370000,0.200000,0.070000,0.010000,0.010000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,1.050000,1.110000,1.300000,2.000000,4.000000,10.000000,999.000000]
    dbObj.CalculateParams()
    return dbObj
