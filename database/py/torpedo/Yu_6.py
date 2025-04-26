# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Yu-6'
    dbObj.natoClass='Yu-6'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=1660.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=2005.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoYU-6.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='[greengills] dewitt--should this be Yu-6?  Amram--Yes, it should be.'
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
    dbObj.maxRange_km=95.635223
    dbObj.probNoFaults=0.950000
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
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=800.000000
    dbObj.battery_kJ=2860.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=65.000000
    dbObj.acceleration_ktsps=4.000000
    dbObj.sonarClass='Yu-6 Torpedo Sonar'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=20.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
