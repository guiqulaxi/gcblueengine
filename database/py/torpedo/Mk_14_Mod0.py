# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-14 Mod0'
    dbObj.natoClass='Mk-14 Mod0'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=1490.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1931.000000
    dbObj.finalYear=1943.750000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoTPMK140.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='setting this according to the same methodology as described for the Mk-48 mod1/3.  Given faults, setting this with an 80% failure rate, and a custom high failure warhead to mimic running too deep or detonating early, and failing to detonate when hits did occur.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast230kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-20.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=0.100000
    dbObj.maxRange_km=4.093949
    dbObj.probNoFaults=0.200000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T2:large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=25.000000
    dbObj.maxDepth_m=5.000000
    dbObj.battery_kJ=173.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=46.000000
    dbObj.acceleration_ktsps=2.000000
    dbObj.sonarClass=''
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=46.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
