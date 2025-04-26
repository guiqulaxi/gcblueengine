# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F-35A'
    dbObj.natoClass='F-35A'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=160000000.000000
    dbObj.weight_kg=13300.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2015.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoF35A.jpg'
    dbObj.mz3DModelFileName='f-35.xml'
    dbObj.notes='Contributed by greengills - it does not use the AGM-84, this has been stripped.  It does have external hardpoints, these have been added, AIM-152 doesn\'t exist, this has been stripped.  '
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AAQ-37 DAS','ALR-94 RWR','APG-81','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1060.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=8391.500000
    dbObj.mfFuelRate_kgps=4.500000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F-35A durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['GAU-22/A 25mm','F-35A Internal 1','F-35A Internal 2','F-35 Wing1','F-35 Wing2','F-35 Wing3','AN/ALE-47 CMD','AN/ALE-47 CMD']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','CM1','CM2']
    dbObj.launcherFOV_deg=[20.000000,0.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APG-81','APG-81','APG-81','APG-81','APG-81','APG-81','','']
    dbObj.launcherFireControl2=['AAQ-37 DAS','AAQ-37 DAS','AAQ-37 DAS','AAQ-37 DAS','AAQ-37 DAS','AAQ-37 DAS','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-30.000000
    airDetectionDBObject.RCS_Model='F35RCS'
    airDetectionDBObject.opticalCrossSection_dBsm=6.800000
    airDetectionDBObject.irSignature_dB=-3.000000
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
    dbObj.maxTakeoffWeight_kg=31800.000000
    dbObj.maxAltitude_m=18800.000000
    dbObj.climbRate_mps=255.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=125000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=191000.000000
    dbObj.abThrustSpeedSlope=0.002000
    dbObj.mfAfterburnFuelRate_kgps=18.000000
    dbObj.mfCdpsub=1.350000
    dbObj.mfCdptran=2.200000
    dbObj.mfCdpsup=2.000000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.830000,0.770000,0.650000,0.480000,0.250000,0.100000,0.050000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,0.850000,0.800000,0.800000,1.060000,2.500000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
