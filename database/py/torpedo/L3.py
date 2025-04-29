# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='L3'
    dbObj.natoClass='L3'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=910.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1960.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoL3.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=50.000000
    dbObj.damageModel='uBlast200kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=3.433917
    dbObj.probNoFaults=0.950000
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
    dbObj.maxTurnRate_degps=10.000000
    dbObj.maxDepth_m=300.000000
    dbObj.battery_kJ=267.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=25.000000
    dbObj.acceleration_ktsps=2.500000
    dbObj.sonarClass='L3 Torpedo Seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=25.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
