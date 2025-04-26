# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='Patriot PAC-2'
    dbObj.natoClass='Patriot PAC-2'
    dbObj.mnModelType=10
    dbObj.mnType=256
    dbObj.cost=100000000.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.000000
    dbObj.finalYear=2050.000000
    dbObj.country='USA'
    dbObj.designation='SAM'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='roland2-site.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MPQ-53']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=0.000000
    dbObj.mfAccel_ktsps=0.000000
    dbObj.mfTurnRate_degps=0.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=40.000000
    dbObj.damageEffect='Generic3'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['PAC-2 Launcher']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[360.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['MPQ-53']
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
