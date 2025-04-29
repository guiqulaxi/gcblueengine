# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='APR-2E'
    dbObj.natoClass='APR-2E'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=575.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoAPR-2E.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast100kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=16
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=7.037600
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T3:torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=24.500000
    dbObj.maxDepth_m=400.000000
    dbObj.battery_kJ=360.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=38.000000
    dbObj.acceleration_ktsps=2.000000
    dbObj.sonarClass='AT-2M seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=38.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
