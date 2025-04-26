# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='mk-24 Tigerfish'
    dbObj.natoClass='mk-24 Tigerfish'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=1551.300049
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoTIGERFISH.jpg'
    dbObj.mz3DModelFileName='65-76.xml'
    dbObj.notes='14,000 yards at 35kts, and 31,600 yards at 24 kts.  GCB can\'t adequately cope with the mixed ranges, and so im assuming an averaged performance.  Range will be set according to a 29.5kt run out to 22800yds. This requires 1373.75 seconds to complete. '
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='uBlast340kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-200.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=28.034649
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
    dbObj.maxDepth_m=440.000000
    dbObj.battery_kJ=1557.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='MK-50 Torpedo Sonar'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=24.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
