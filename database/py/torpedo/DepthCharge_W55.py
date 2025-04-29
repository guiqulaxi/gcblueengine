# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='DepthCharge-W55'
    dbObj.natoClass='DepthCharge-W55'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=500.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1969.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoDCW55.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='NuclearUW-5kT'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=5.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=999.000000
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=999.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=2000.000000
    dbObj.battery_kJ=999999.000000
    dbObj.batteryRate_kW=0.000000
    dbObj.maxSpeed_kts=7.000000
    dbObj.acceleration_ktsps=1.000000
    dbObj.sonarClass='Generic Passive'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=7.000000
    dbObj.weaponType=2
    dbObj.CalculateParams()
    return dbObj
