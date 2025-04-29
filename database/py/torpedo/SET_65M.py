# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='SET-65M'
    dbObj.natoClass='SET-65M'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=410.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1972.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoSET-65M.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='couldnt find source for difference between original set-65 and modernized version -65m.  granted it a superior seeker with 30% greater range.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=205.000000
    dbObj.damageModel='uBlast200kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=18.869822
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
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=400.000000
    dbObj.battery_kJ=917.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=40.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='SET-65M Seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=26.400000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
