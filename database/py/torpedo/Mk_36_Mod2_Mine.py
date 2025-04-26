# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-36 Mod2 Mine'
    dbObj.natoClass='Mk-36 Mod2 Mine'
    dbObj.mnModelType=9
    dbObj.mnType=138
    dbObj.cost=500000.000000
    dbObj.weight_kg=907.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMNMK362.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='uBlast580kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=5.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=200.000000
    dbObj.minRange_km=0.100000
    dbObj.maxRange_km=1.000000
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=25.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Mine'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=120.000000
    dbObj.battery_kJ=99999.000000
    dbObj.batteryRate_kW=0.000000
    dbObj.maxSpeed_kts=15.000000
    dbObj.acceleration_ktsps=5.000000
    dbObj.sonarClass='Lofar 13'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=0.000000
    dbObj.weaponType=3
    dbObj.CalculateParams()
    return dbObj
