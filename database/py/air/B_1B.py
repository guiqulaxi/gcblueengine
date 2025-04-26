# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='B-1B'
    dbObj.natoClass='B-1B'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=290000000.000000
    dbObj.weight_kg=87100.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Bomber'
    dbObj.imageList='b1b.jpg'
    dbObj.iconFileName='air/AdvicoB1B.jpg'
    dbObj.mz3DModelFileName='B-1B Lancer.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-161A ECM','ALQ-161A ESM','APQ-164','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Generic Advanced Designator']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=750.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=95000.000000
    dbObj.mfFuelRate_kgps=5.300000
    dbObj.mfToughness=3.000000
    dbObj.damageEffect='B-1B durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['B-1B Bay','B-1B Bay','B-1B Bay','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['B1','B2','B3','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APQ-164','APQ-164','APQ-164','','']
    dbObj.launcherFireControl2=['Generic Advanced Designator','Generic Advanced Designator','Generic Advanced Designator','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=14.080000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_HP_4_M0.85'
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
    dbObj.maxTakeoffWeight_kg=216000.000000
    dbObj.maxAltitude_m=18000.000000
    dbObj.climbRate_mps=20.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=40.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=260000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=548000.000000
    dbObj.abThrustSpeedSlope=0.000000
    dbObj.mfAfterburnFuelRate_kgps=20.000000
    dbObj.mfCdpsub=4.500000
    dbObj.mfCdptran=6.000000
    dbObj.mfCdpsup=7.000000
    dbObj.mfMcm=1.200000
    dbObj.mfMsupm=1.250000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[0.950000,0.900000,0.850000,0.800000,0.700000,0.500000,0.300000,0.200000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,0.850000,0.920000,1.000000,1.400000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
