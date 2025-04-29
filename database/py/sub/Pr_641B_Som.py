# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Pr 641B Som'
    dbObj.natoClass='Tango'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=2640000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.997314
    dbObj.finalYear=2999.997314
    dbObj.country='Russia'
    dbObj.designation='SSN'
    dbObj.imageList='tango.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','MGK-400 Active','MGK-400 Bow Passive','MRK-50 SS','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=15.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=600000.000000
    dbObj.mfFuelRate_kgps=0.500000
    dbObj.mfToughness=120.000000
    dbObj.damageEffect='Pr 641B Som durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube']
    dbObj.maMagazineClass=['Sub 24']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.300000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.300000
    airDetectionDBObject.irSignature_dB=7.300000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=12.392000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='RK175'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.200000
    dbObj.surfaceSpeed_kts=13.000000
    dbObj.mfMaxDepth_m=250.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=4.000000
    dbObj.CalculateParams()
    return dbObj
