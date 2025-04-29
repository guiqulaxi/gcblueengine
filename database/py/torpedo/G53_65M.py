# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='53-65M'
    dbObj.natoClass='53-65M'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=900.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1969.000000
    dbObj.finalYear=1995.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/ico53-65M.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='based off of the assumption that the pre-enable range by default is 50%(some in game testing suggets this), battery life has been extended to allow the torpedo to reach  22km in normal usage.  if 50% is accurate, then the torpedo is covering 11km in pre-enable, and the remainder enabled.  at 30kts 11km takes 713 seconds, and at 44 kts 11km takes 486 seconds, for a total of 1200 seconds, not 980, which is only sufficient for 18km under normal usage.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='uBlast300kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-200.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=27.162666
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T2:large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=200.000000
    dbObj.battery_kJ=1200.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=44.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Passive wake homer'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=30.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
