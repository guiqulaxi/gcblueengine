# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='Tien Kung-II'
    dbObj.natoClass='Tien Kung-II'
    dbObj.mnModelType=10
    dbObj.mnType=256
    dbObj.cost=20000000.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Taiwan'
    dbObj.designation='SAM'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='roland2-site.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h','Tien Kung AS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=0.000000
    dbObj.mfAccel_ktsps=0.000000
    dbObj.mfTurnRate_degps=0.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=20.000000
    dbObj.damageEffect='Generic3'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['Tien Kung Launcher']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[360.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[40.000000]
    dbObj.launcherFireControl=['Tien Kung AS']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[False]
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
