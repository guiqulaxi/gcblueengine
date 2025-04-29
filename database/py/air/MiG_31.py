# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='MiG-31'
    dbObj.natoClass='Foxhound'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=60000000.000000
    dbObj.weight_kg=21800.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Fighter'
    dbObj.imageList='mig31.jpg'
    dbObj.iconFileName='air/AdvicoMiG31.jpg'
    dbObj.mz3DModelFileName='mig-29.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','NIIP N-007 S-800 Zaslon','SPO-15 RWR','TP-8 IRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1620.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=14200.000000
    dbObj.mfFuelRate_kgps=5.000000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='MiG-31 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['GSh-6-23','MiG-31 Weapon Mount','MiG-31 Weapon Mount','MiG-31 Fuel Mount','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['Gun','','','','CM1','CM2']
    dbObj.launcherFOV_deg=[20.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','NIIP N-007 S-800 Zaslon','NIIP N-007 S-800 Zaslon','','','']
    dbObj.launcherFireControl2=['','TP-8 IRST','TP-8 IRST','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.120000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.180000
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
    dbObj.maxTakeoffWeight_kg=46300.000000
    dbObj.maxAltitude_m=24000.000000
    dbObj.climbRate_mps=210.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=100000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=220000.000000
    dbObj.abThrustSpeedSlope=0.002000
    dbObj.mfAfterburnFuelRate_kgps=12.000000
    dbObj.mfCdpsub=0.800000
    dbObj.mfCdptran=2.500000
    dbObj.mfCdpsup=2.200000
    dbObj.mfMcm=1.000000
    dbObj.mfMsupm=1.300000
    dbObj.cruiseSpeed_mps=110.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.800000,0.800000,0.850000,0.800000,0.500000,0.200000,0.050000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,1.000000,1.100000,1.250000,1.900000,3.000000,6.000000,8.000000]
    dbObj.CalculateParams()
    return dbObj
