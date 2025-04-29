# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='L5 Mod 4'
    dbObj.natoClass='L5 Mod 4'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=700000.000000
    dbObj.weight_kg=935.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1980.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoL5.4.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='http://www.navweaps.com/Weapons/WTFR_PostWWII.htm'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast200kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=16
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.250000
    dbObj.maxRange_km=9.903055
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
    dbObj.maxDepth_m=550.000000
    dbObj.battery_kJ=550.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='MK-46 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=35.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
