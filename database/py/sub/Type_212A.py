# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Type 212A'
    dbObj.natoClass='Type 212A'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=7500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.017944
    dbObj.finalYear=2999.989990
    dbObj.country='Germany'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DBQS-40 Active','DBQS-40 Bow Passive','DBQS-40 Port Flank Passive','DBQS-40 Stbd Flank Passive','ESM-1','Periscope-1','TAS-3 TA','Type 1007(s)']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,270.000000,90.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=1.300000
    dbObj.mfTurnRate_degps=6.000000
    dbObj.mfFuelCapacity_kg=3401660.000000
    dbObj.mfFuelRate_kgps=1.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Type 212A durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm German Torpedo Tube','533mm German Torpedo Tube','533mm German Torpedo Tube','533mm German Torpedo Tube','533mm German Torpedo Tube','533mm German Torpedo Tube']
    dbObj.maMagazineClass=['Type 212 Torpedo Racks']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.700000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.700000
    airDetectionDBObject.irSignature_dB=10.700000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=3.720000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='GK190'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.400000
    dbObj.surfaceSpeed_kts=12.000000
    dbObj.mfMaxDepth_m=340.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=24.000000
    dbObj.CalculateParams()
    return dbObj
