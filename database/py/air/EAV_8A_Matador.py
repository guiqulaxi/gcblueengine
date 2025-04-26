# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='EAV-8A Matador'
    dbObj.natoClass='EAV-8A Matador'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=5600.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.000000
    dbObj.finalYear=1997.000000
    dbObj.country='Spain'
    dbObj.designation='Strike Fighter'
    dbObj.imageList='av8s.jpg'
    dbObj.iconFileName='air/AdvicoHarrierEAV8A.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Laser-20km']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=574.830017
    dbObj.mfAccel_ktsps=24.639999
    dbObj.mfTurnRate_degps=29.879999
    dbObj.mfFuelCapacity_kg=2311.000000
    dbObj.mfFuelRate_kgps=1.300000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='EAV-8A Matador durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['AV-8A 1-5','AV-8A 2-4','AV-8A 3']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['Laser-20km','Laser-20km','Laser-20km']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.190000
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
    dbObj.maxTakeoffWeight_kg=11400.000000
    dbObj.maxAltitude_m=15500.000000
    dbObj.climbRate_mps=70.000000
    dbObj.gmax=8.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=74898.210938
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=96138.000000
    dbObj.abThrustSpeedSlope=0.000000
    dbObj.mfAfterburnFuelRate_kgps=2.840000
    dbObj.mfCdpsub=0.750000
    dbObj.mfCdptran=1.500000
    dbObj.mfCdpsup=2.500000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.000000
    dbObj.cruiseSpeed_mps=140.000000
    dbObj.stallSpeed_mps=0.000000
    dbObj.thrustTable=[0.950000,0.900000,0.880000,0.850000,0.800000,0.750000,0.700000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,0.900000,0.950000,1.100000,1.500000,2.000000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
