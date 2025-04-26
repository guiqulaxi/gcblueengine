# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='MIM-23 Hawk'
    dbObj.natoClass='Hawk'
    dbObj.mnModelType=17
    dbObj.mnType=256
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1959.000000
    dbObj.finalYear=1983.000000
    dbObj.country='USA'
    dbObj.designation='SAM'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='rapier-towed.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h','MPQ-33','MPQ-34','MPQ-35']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=0.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Generic3'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['MIM-23 Hawk Launcher','MIM-23 Hawk Launcher','MIM-23 Hawk Launcher','MIM-23 Hawk Launcher','MIM-23 Hawk Launcher','MIM-23 Hawk Launcher']
    dbObj.maMagazineClass=['MIM-23 Hawk Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[57.000000,57.000000,57.000000,57.000000,57.000000,57.000000]
    dbObj.launcherFireControl=['MPQ-33','MPQ-33','MPQ-33','MPQ-33','MPQ-33','MPQ-33']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.500000
    airDetectionDBObject.RCS_Model='Default'
    airDetectionDBObject.opticalCrossSection_dBsm=3.000000
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
