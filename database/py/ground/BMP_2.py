# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='BMP-2'
    dbObj.natoClass='BMP-2'
    dbObj.mnModelType=17
    dbObj.mnType=258
    dbObj.cost=0.000000
    dbObj.weight_kg=5450.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='APC'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='rapier-towed.xml'
    dbObj.notes='[Redtail]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=24.330000
    dbObj.mfAccel_ktsps=2.500000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=462.000000
    dbObj.mfFuelRate_kgps=0.025330
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Generic4'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['30mm 2A42','Konkurs ATGM Launcher']
    dbObj.maMagazineClass=['BMP1 Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=14.000000
    airDetectionDBObject.RCS_Model='Default'
    airDetectionDBObject.opticalCrossSection_dBsm=14.000000
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
