# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='F-17P Mod2'
    dbObj.natoClass='F-17P Mod2'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=750000.000000
    dbObj.weight_kg=1410.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1985.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoF-17P.2.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='Extrapolated from Base model int he same manner as was done for the F-17 Mod1.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=50.000000
    dbObj.damageModel='uBlast250kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=59.886475
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T1:very large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=12.000000
    dbObj.maxDepth_m=600.000000
    dbObj.battery_kJ=3326.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.000000
    dbObj.acceleration_ktsps=8.000000
    dbObj.sonarClass='MU-90 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=24.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
