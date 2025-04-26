# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='FJ-3 Fury'
    dbObj.natoClass='FJ-3 Fury'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=5535.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1954.000000
    dbObj.finalYear=1960.000000
    dbObj.country='USA'
    dbObj.designation='Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoFJ3.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=617.000000
    dbObj.mfAccel_ktsps=22.389999
    dbObj.mfTurnRate_degps=14.000000
    dbObj.mfFuelCapacity_kg=1701.975952
    dbObj.mfFuelRate_kgps=0.734000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='FJ-3 Fury durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['0.50in(12.7mm) Browning M2(300)(x2)','0.50in(12.7mm) Browning M2(300)(x2)','0.50in(12.7mm) Browning M2(300)(x2)','F-86 Wing1','F-86 Rockets','F-86 Wing2']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[10.000000,10.000000,10.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.300000
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
    dbObj.maxTakeoffWeight_kg=8523.000000
    dbObj.maxAltitude_m=14900.000000
    dbObj.climbRate_mps=44.000000
    dbObj.gmax=6.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=34200.000000
    dbObj.militaryThrustSpeedSlope=0.002973
    dbObj.mfAfterburnThrust_N=34200.000000
    dbObj.abThrustSpeedSlope=0.002973
    dbObj.mfAfterburnFuelRate_kgps=0.734000
    dbObj.mfCdpsub=0.466670
    dbObj.mfCdptran=0.700000
    dbObj.mfCdpsup=0.560000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.300000
    dbObj.cruiseSpeed_mps=90.000000
    dbObj.stallSpeed_mps=45.000000
    dbObj.thrustTable=[0.880000,0.770000,0.670000,0.576000,0.445000,0.325000,0.010000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[0.980000,0.950000,0.900000,0.950000,1.100000,1.500000,2.500000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
