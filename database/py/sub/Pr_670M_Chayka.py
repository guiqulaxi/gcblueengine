# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Pr 670M Chayka'
    dbObj.natoClass='Charlie II'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=1000000000.000000
    dbObj.weight_kg=4300000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.994507
    dbObj.finalYear=1998.408569
    dbObj.country='Russia'
    dbObj.designation='SSGN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='charlie-1.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','MGK-300 Active','MGK-300 Bow Passive','MRP-25 SS','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=24.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=1.500000
    dbObj.mfFuelCapacity_kg=10000.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Pr 670M Chayka durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['533mm Charlie tube','533mm Charlie tube','533mm Charlie tube','533mm Charlie tube','533mm Charlie tube','533mm Charlie tube','Sub P-120 Launcher x8']
    dbObj.maMagazineClass=['Charlie torpedo magazine']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['T1','T2','T3','T4','T5','T6','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.900000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.900000
    airDetectionDBObject.irSignature_dB=8.900000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=13.670000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='RN175'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.000000
    dbObj.surfaceSpeed_kts=18.000000
    dbObj.mfMaxDepth_m=290.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=8.000000
    dbObj.CalculateParams()
    return dbObj
