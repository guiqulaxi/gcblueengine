# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Type-89 Torpedo'
    dbObj.natoClass='Type-89 Torpedo'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=600000.000000
    dbObj.weight_kg=1000.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1992.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoTYPE-89.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='42kyds at 55kts, 54kyds at 40, '
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast260kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=49.863300
    dbObj.probNoFaults=0.900000
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
    dbObj.maxDepth_m=900.000000
    dbObj.battery_kJ=1762.300049
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=55.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Type-89 Seeker'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=40.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
