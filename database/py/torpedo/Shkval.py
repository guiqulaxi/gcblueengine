# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Shkval'
    dbObj.natoClass='Shkval'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=420.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoSHKVAL.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='worked out necessary time given the 40kts acceleration, from a 10m/s start, to a peak of 200kts, for a range of 10km.  Battery value was a little better than 2 seconds too short, increased to 100.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=210.000000
    dbObj.damageModel='uBlast700kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=10.288888
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T6:Shkval'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=400.000000
    dbObj.battery_kJ=100.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=200.000000
    dbObj.acceleration_ktsps=40.000000
    dbObj.sonarClass='MK-50 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=200.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
