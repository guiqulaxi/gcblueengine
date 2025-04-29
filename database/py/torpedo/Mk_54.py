# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-54'
    dbObj.natoClass='Mk-54'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=2900000.000000
    dbObj.weight_kg=240.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=2002.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMK-54.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='little to nothing is known of this weapon, other than it uses the mk-50 seeker, mk-46 drive section, has upgraded software, and uses many commercially obtained items to reduce its cost considerably.  Assuming this torpedo to be superior to the Mk-50 in every way from various points of improvement.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=67.500000
    dbObj.damageModel='Pen60kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=10000.000000
    dbObj.minRange_km=0.250000
    dbObj.maxRange_km=24.446398
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T3:torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=1500.000000
    dbObj.battery_kJ=792.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=60.000000
    dbObj.acceleration_ktsps=5.000000
    dbObj.sonarClass='Mk-54 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=35.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
