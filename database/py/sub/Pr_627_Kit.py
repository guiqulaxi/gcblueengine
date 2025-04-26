# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Pr 627 Kit'
    dbObj.natoClass='November'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=3118000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1958.959961
    dbObj.finalYear=1990.496948
    dbObj.country='Russia'
    dbObj.designation='SSN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['MGK-200 Active','MGK-200 Bow Passive','MRK-10 SS','Periscope-1','Zhaliv-P ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Pr 627 Kit durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube']
    dbObj.maMagazineClass=['Russian Sub 20']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['533mm','533mm','533mm','533mm','533mm','533mm','533mm','533mm']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.800000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.800000
    airDetectionDBObject.irSignature_dB=7.800000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=12.689000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='RN160'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.400000
    dbObj.surfaceSpeed_kts=15.200000
    dbObj.mfMaxDepth_m=240.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=0.000000
    dbObj.batteryCharge_kW=0.000000
    dbObj.CalculateParams()
    return dbObj
