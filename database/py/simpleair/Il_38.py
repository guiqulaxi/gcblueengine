# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Il-38'
    dbObj.natoClass='Il-38 May'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=5000000.000000
    dbObj.weight_kg=35000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1968.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='ASW'
    dbObj.imageList='Il-38_May.jpg'
    dbObj.iconFileName='air/AdvicoIL38.jpg'
    dbObj.mz3DModelFileName='tu-142.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AEW radar 0','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=390.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=7.000000
    dbObj.mfFuelCapacity_kg=9000.000000
    dbObj.mfFuelRate_kgps=0.190000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Il-38 durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['17 DICASS Launcher','17 LOFAR Launcher','41 DIFAR Launcher','Il-38 Weapon Bay']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=20.250000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=13.300000
    airDetectionDBObject.irSignature_dB=30.000000
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
    dbObj.maxTakeoffWeight_kg=65000.000000
    dbObj.maxAltitude_m=11000.000000
    dbObj.climbRate_mps=13.000000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
