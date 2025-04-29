# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-9 DC'
    dbObj.natoClass='Mk-9 DC'
    dbObj.mnModelType=9
    dbObj.mnType=138
    dbObj.cost=0.000000
    dbObj.weight_kg=272.000000
    dbObj.volume_m3=0.300000
    dbObj.initialYear=1943.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoDCMK9.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast205kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=12.000000
    dbObj.targetFlags=16
    dbObj.minLaunchAlt_m=-5.000000
    dbObj.maxLaunchAlt_m=1000.000000
    dbObj.minRange_km=0.000000
    dbObj.maxRange_km=5.000000
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=2.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Mine'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=300.000000
    dbObj.battery_kJ=225.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=12.674000
    dbObj.acceleration_ktsps=2.000000
    dbObj.sonarClass=''
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=12.674000
    dbObj.weaponType=2
    dbObj.CalculateParams()
    return dbObj
