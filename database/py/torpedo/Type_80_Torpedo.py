# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Type-80 Torpedo'
    dbObj.natoClass='Type-80 Torpedo'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=600000.000000
    dbObj.weight_kg=650.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoTYPE-80.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='As its superior to NT37 in both speed and range, I have bumped the battery and speed of NT37 by 10% each, yielding 21% greater range.  44.8km@26.2kts, 19.9km@39.6kts, equates to 27.5km in GCB owing to 50/50 run.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast150kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=21.831738
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
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=305.000000
    dbObj.battery_kJ=1697.500000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=25.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Type-80 Seeker'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=40.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
