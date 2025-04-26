# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Type-431 Torpedo'
    dbObj.natoClass='Type-431 Torpedo'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=600000.000000
    dbObj.weight_kg=350.000000
    dbObj.volume_m3=1.500000
    dbObj.initialYear=1987.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Sweden'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoTYPE-431.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='Pen50kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=16
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=46.184246
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T4:small torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=300.000000
    dbObj.battery_kJ=2565.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Generic torpedo seeker'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=15.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
