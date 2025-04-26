# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='46-36N'
    dbObj.natoClass='46-36N'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=935.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1937.000000
    dbObj.finalYear=1942.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/ico46-36N.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=205.000000
    dbObj.damageModel='uBlast200kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=5.357424
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
    dbObj.maxTurnRate_degps=10.000000
    dbObj.maxDepth_m=30.000000
    dbObj.battery_kJ=254.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=41.000000
    dbObj.acceleration_ktsps=1.200000
    dbObj.sonarClass=''
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=32.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
