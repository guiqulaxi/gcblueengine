# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='53-61M'
    dbObj.natoClass='53-61M'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=2050.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1969.000000
    dbObj.finalYear=1995.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/ico53-61M.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=205.000000
    dbObj.damageModel='uBlast305kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=25.493296
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T1:very large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=10.000000
    dbObj.maxDepth_m=40.000000
    dbObj.battery_kJ=901.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=55.000000
    dbObj.acceleration_ktsps=2.000000
    dbObj.sonarClass='Passive wake homer'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=35.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
