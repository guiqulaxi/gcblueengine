# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-48 Mod6'
    dbObj.natoClass='Mk-48 Mod6'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=3500000.000000
    dbObj.weight_kg=1660.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1995.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMK-48.6.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='as per Mod5, except a hair faster, and quite a bit quieter.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=290.000000
    dbObj.damageModel='uBlast300kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=80.387085
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T3:torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=30.000000
    dbObj.maxDepth_m=1000.000000
    dbObj.battery_kJ=2404.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=65.000000
    dbObj.acceleration_ktsps=4.000000
    dbObj.sonarClass='Mk-48 Torpedo Sonar'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=42.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
