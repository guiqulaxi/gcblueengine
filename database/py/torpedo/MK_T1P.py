# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='MK-T1P'
    dbObj.natoClass='MK-T1P'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=900.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='TEST'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/torp_unk.jpg'
    dbObj.mz3DModelFileName='set-65.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=75.000000
    dbObj.damageModel='uBlast100kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=25.001999
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=500.000000
    dbObj.battery_kJ=810.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=60.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Passive torpedo seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=40.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
