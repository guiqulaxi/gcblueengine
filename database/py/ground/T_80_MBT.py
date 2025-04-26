# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcGroundDBObject()
    dbObj.mzClass='T-80 MBT'
    dbObj.natoClass='T-80 MBT'
    dbObj.mnModelType=17
    dbObj.mnType=258
    dbObj.cost=0.000000
    dbObj.weight_kg=5450.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='TANK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='rapier-towed.xml'
    dbObj.notes='road speed 70km, off road speed 48km, road range 440km, off road range assumed to be 352km, main fuel 1100 liters, auxiliary fuel 740 liters.  '
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20e','Eyeball 20/20f','Eyeball 20/20g','Eyeball 20/20h']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.238001
    dbObj.mfAccel_ktsps=3.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=1477.520020
    dbObj.mfFuelRate_kgps=0.058039
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Generic4'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['105mm generic tank cannon','125mm 2A46','12.7mm NSV']
    dbObj.maMagazineClass=['12.7mm store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=6.000000
    airDetectionDBObject.RCS_Model='Default'
    airDetectionDBObject.opticalCrossSection_dBsm=-9.000000
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
