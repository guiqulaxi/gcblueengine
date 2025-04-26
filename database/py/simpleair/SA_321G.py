# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='SA-321G'
    dbObj.natoClass='SA-321G'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=10000000.000000
    dbObj.weight_kg=6863.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='ASW'
    dbObj.imageList='dauphin.jpg'
    dbObj.iconFileName='air/AdvicoSA321G.JPG'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='Wikipedia. Need to check this--was quickly created. Needs dipping sonar?'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','ORB-42 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=135.000000
    dbObj.mfAccel_ktsps=12.000000
    dbObj.mfTurnRate_degps=3.000000
    dbObj.mfFuelCapacity_kg=2000.000000
    dbObj.mfFuelRate_kgps=0.135000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='SA-321G durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['20 mm Mk12','Frelon Launcher']
    dbObj.maMagazineClass=['Cargo 3']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[5.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=16.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.270000
    airDetectionDBObject.irSignature_dB=33.000000
    airDetectionDBObject.IR_ModelA='AirIR1'
    airDetectionDBObject.IR_ModelB='AirIR1'
    airDetectionDBObject.IR_ModelC='AirIR1'
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
    dbObj.maxTakeoffWeight_kg=13000.000000
    dbObj.maxAltitude_m=3150.000000
    dbObj.climbRate_mps=6.700000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
