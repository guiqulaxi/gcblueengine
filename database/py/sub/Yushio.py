# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Yushio'
    dbObj.natoClass='Yushio'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=2400000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.151245
    dbObj.finalYear=1985.000000
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
    sensorPlatformDBObject.sensorClass=['Periscope-1','ZLA-6 ESM','ZPS-6 AS/SS','ZQQ-4 Active','ZQQ-4 Bow Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=315000.000000
    dbObj.mfFuelRate_kgps=0.379860
    dbObj.mfToughness=120.000000
    dbObj.damageEffect='Yushio durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm Japanese Sub Tube Early','533mm Japanese Sub Tube Early','533mm Japanese Sub Tube Early','533mm Japanese Sub Tube Early','533mm Japanese Sub Tube Early','533mm Japanese Sub Tube Early']
    dbObj.maMagazineClass=['Sub 20']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=25.500000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.500000
    airDetectionDBObject.irSignature_dB=17.750000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=8.486000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='JK180'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.400000
    dbObj.surfaceSpeed_kts=12.000000
    dbObj.mfMaxDepth_m=275.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.613100
    dbObj.CalculateParams()
    return dbObj
