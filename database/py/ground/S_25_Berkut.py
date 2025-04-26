# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='S-25 Berkut'
    dbObj.natoClass='SA-1 Guild'
    dbObj.mnModelType=17
    dbObj.mnType=256
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1954.000000
    dbObj.finalYear=1982.000000
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
    sensorPlatformDBObject.sensorClass=['B-200','Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h','R-113']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=0.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Generic3'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher','S-25 Berkut Launcher']
    dbObj.maMagazineClass=['S-25 Berkut Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['B-200','B-200','B-200','B-200','B-200','B-200','B-200','B-200','B-200','B-200']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=22.781513
    airDetectionDBObject.RCS_Model='Default'
    airDetectionDBObject.opticalCrossSection_dBsm=16.780001
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
