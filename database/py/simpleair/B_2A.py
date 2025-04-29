# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='B-2A'
    dbObj.natoClass='B-2A'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=750000000.000000
    dbObj.weight_kg=71700.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1997.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Bomber'
    dbObj.imageList='b2.jpg'
    dbObj.iconFileName='air/AdvicoB2A.jpg'
    dbObj.mz3DModelFileName='b-2.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APQ-181','APR-50 ESM','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Generic Advanced Designator']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=525.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=55000.000000
    dbObj.mfFuelRate_kgps=1.350000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='B-2A durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['B-2A Bay','B-2A Bay','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['B1','B2','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Generic Advanced Designator','Generic Advanced Designator','Generic Advanced Designator','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-32.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=16.650000
    airDetectionDBObject.irSignature_dB=20.000000
    airDetectionDBObject.IR_ModelA='B-2M0.85'
    airDetectionDBObject.IR_ModelB='B-2M0.85'
    airDetectionDBObject.IR_ModelC='B-2M0.85'
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
    dbObj.maxTakeoffWeight_kg=170000.000000
    dbObj.maxAltitude_m=15000.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=50.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
