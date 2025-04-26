# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Kurushio SS'
    dbObj.natoClass='Kurushio SS'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=2424000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1955.620972
    dbObj.finalYear=1966.244995
    dbObj.country='Japan'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['JP Passive','Periscope-1','SJ','SV']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=8.500000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=339360.000000
    dbObj.mfFuelRate_kgps=0.094868
    dbObj.mfToughness=120.000000
    dbObj.damageEffect='Kurushio SS durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube','533mm Gato Tube']
    dbObj.maMagazineClass=['Sub 24']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,180.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=26.600000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.600000
    airDetectionDBObject.irSignature_dB=18.299999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=5.643000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='AK145'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.200000
    dbObj.surfaceSpeed_kts=20.000000
    dbObj.mfMaxDepth_m=350.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=2.890648
    dbObj.CalculateParams()
    return dbObj
