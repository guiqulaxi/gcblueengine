# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Type-617 Torpedo'
    dbObj.natoClass='Type-617 Torpedo'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=600000.000000
    dbObj.weight_kg=1860.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Sweden'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoTYPE-617.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='[dewitt] Friedman. World Naval Weapon Systems. Some sources claim max speed of 60+ kts. Type 613 has increased range with two-speed motor and terminal homing.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast240kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=37.502998
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T1:very large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=200.000000
    dbObj.battery_kJ=1215.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=60.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Generic torpedo seeker'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=40.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
