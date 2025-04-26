# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='DM2A4.3'
    dbObj.natoClass='DM2A4.3'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=750000.000000
    dbObj.weight_kg=1162.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1988.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoDM2A4.3.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='This is the medium size model, with 3 batteries.  weight is assumed.  It carries a 260kg warhead, leaving 1110, assumed guidance, structure, and propulsion account got 25% of that leaving the remainder for the batteries, given 4 batteries at a weight of 1370kg, that would make each battery 208.125kg, thus this torpedoes weight of 1162.  Depth is assumed(see DM2A4.4).'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=50.000000
    dbObj.damageModel='uBlast260kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=47.249149
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T2:large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=12.000000
    dbObj.maxDepth_m=1000.000000
    dbObj.battery_kJ=2041.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=45.000000
    dbObj.acceleration_ktsps=9.000000
    dbObj.sonarClass='DM2A4 Seeker'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=30.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
