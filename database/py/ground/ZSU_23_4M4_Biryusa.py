# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='ZSU-23-4M4 Biryusa'
    dbObj.natoClass='ZSU-23-4M4 Biryusa'
    dbObj.mnModelType=17
    dbObj.mnType=258
    dbObj.cost=0.000000
    dbObj.weight_kg=14000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1999.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='SPAAG'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='rapier-towed.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h','Gun Dish']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=23.799999
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=212.500000
    dbObj.mfFuelRate_kgps=0.099890
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Generic3'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['ZSU-23-4M4 Biryusa Launcher','ZSU-23-4M4 Biryusa Launcher 2']
    dbObj.maMagazineClass=['ZSU-23-4M4 Biryusa Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.000000
    airDetectionDBObject.RCS_Model='Default'
    airDetectionDBObject.opticalCrossSection_dBsm=-3.000000
    airDetectionDBObject.irSignature_dB=14.000000
    airDetectionDBObject.IR_ModelA='Default'
    airDetectionDBObject.IR_ModelB='Default'
    airDetectionDBObject.IR_ModelC='Default'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
