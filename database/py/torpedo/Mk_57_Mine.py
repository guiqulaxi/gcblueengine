# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-57 Mine'
    dbObj.natoClass='Mk-57 Mine'
    dbObj.mnModelType=9
    dbObj.mnType=138
    dbObj.cost=500000.000000
    dbObj.weight_kg=900.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1966.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMNMK-57.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='Mk-56 is aircraft laid version'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='uBlast150kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=5.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=22.000000
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=30.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Mine'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=400.000000
    dbObj.battery_kJ=9999.000000
    dbObj.batteryRate_kW=0.000000
    dbObj.maxSpeed_kts=5.000000
    dbObj.acceleration_ktsps=5.000000
    dbObj.sonarClass='Generic Passive'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=5.000000
    dbObj.weaponType=3
    dbObj.CalculateParams()
    return dbObj
