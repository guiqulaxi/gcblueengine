# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='RBU-DC-RUR-4A Weapon Alfa'
    dbObj.natoClass='RBU-DC-RUR-4A Weapon Alfa'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=40.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1950.000000
    dbObj.finalYear=2999.000000
    dbObj.country='TEST'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoDC_Unk.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='uBlast115kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=16
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=50.000000
    dbObj.minRange_km=0.000000
    dbObj.maxRange_km=0.250000
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=2.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=330.000000
    dbObj.battery_kJ=999999.000000
    dbObj.batteryRate_kW=0.000000
    dbObj.maxSpeed_kts=22.500000
    dbObj.acceleration_ktsps=22.500000
    dbObj.sonarClass='Generic Passive'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=22.500000
    dbObj.weaponType=2
    dbObj.CalculateParams()
    return dbObj
