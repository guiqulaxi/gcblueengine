# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-37'
    dbObj.natoClass='Mk-37'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=600000.000000
    dbObj.weight_kg=650.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1957.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMK-37.1.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='Friedman. World Naval Weapon Systems Ed 5. 26kt 10kyds, or 17kt 23500yds. 50/50 run results in 13.1km range, setting for this in GCB.  Reality is not capable of a 50/50 run, its either high or low for full run.  requires 1235 seconds with this setting to complete a kill.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast150kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=16.529512
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
    dbObj.battery_kJ=1235.800049
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=26.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='Mk-37 Mod1 Seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=26.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
