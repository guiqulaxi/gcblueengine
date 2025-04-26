# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Pr 671RTMK Shchuka'
    dbObj.natoClass='Victor III'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=4850000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1977.989014
    dbObj.finalYear=2999.997314
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
    sensorPlatformDBObject.sensorClass=['MGK-400 Active','MGK-400 Bow Passive','MGK-400 Port Flank Passive','MGK-400 Stbd Flank Passive','MRK-50 SS','Pelamida TA','Periscope-1','Zhaliv-P ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,270.000000,90.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Pr 671RTMK Shchuka durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','650mm torpedo tube','650mm torpedo tube']
    dbObj.maMagazineClass=['Russian Torpedo Racking']
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
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.300000
    airDetectionDBObject.irSignature_dB=9.300000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=14.198000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='RN180'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.000000
    dbObj.surfaceSpeed_kts=22.500000
    dbObj.mfMaxDepth_m=335.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=0.000000
    dbObj.batteryCharge_kW=0.000000
    dbObj.CalculateParams()
    return dbObj
