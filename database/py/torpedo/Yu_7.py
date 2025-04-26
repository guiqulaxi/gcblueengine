# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Yu-7'
    dbObj.natoClass='Yu-7'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=235.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1994.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoYU-7.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='[greengills] dewitt--should this be Yu-7?  Amram--Yes, it should be.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=60.000000
    dbObj.damageModel='uBlast50kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=13.010300
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T4:small torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=450.000000
    dbObj.battery_kJ=562.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=45.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Yu-7 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=20.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
