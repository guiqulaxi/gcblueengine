# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='A-244S'
    dbObj.natoClass='A-244S'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=235.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1972.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Italy'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoA-244S.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=34.000000
    dbObj.damageModel='uBlast50kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=16
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=7.633841
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T4:small torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=40.000000
    dbObj.maxDepth_m=520.000000
    dbObj.battery_kJ=418.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.500000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='A-244S Seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=23.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
