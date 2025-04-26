# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='9K37 Buk'
    dbObj.natoClass='SA-11 Gadfly'
    dbObj.mnModelType=17
    dbObj.mnType=256
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1978.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='SAM'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='rapier-towed.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['9S18','9S36','Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=0.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Generic3'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['9K37 Buk Launcher','9K37 Buk Launcher','9K37 Buk Launcher','9K37 Buk Launcher','9K37 Buk Launcher','9K37 Buk Launcher']
    dbObj.maMagazineClass=['9K37 Buk Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[57.000000,57.000000,57.000000,57.000000,57.000000,57.000000]
    dbObj.launcherFireControl=['9S36','9S36','9S36','9S36','9S36','9S36']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=18.281513
    airDetectionDBObject.RCS_Model='Default'
    airDetectionDBObject.opticalCrossSection_dBsm=10.780000
    airDetectionDBObject.irSignature_dB=20.000000
    airDetectionDBObject.IR_ModelA='Default'
    airDetectionDBObject.IR_ModelB='Default'
    airDetectionDBObject.IR_ModelC='Default'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
