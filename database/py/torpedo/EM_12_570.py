# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='EM-12 570'
    dbObj.natoClass='EM-12 570'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=570.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1966.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMNEM12.570.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='2 year service life once deployed'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='uBlast320kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=5.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.000000
    dbObj.maxRange_km=0.001029
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=13.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-99.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Mine'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=360.000000
    dbObj.maxDepth_m=200.000000
    dbObj.battery_kJ=2.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=1.000000
    dbObj.acceleration_ktsps=1.000000
    dbObj.sonarClass='Generic Passive'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=1.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
