# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='SST-4 Mod.0'
    dbObj.natoClass='SST-4 Mod.0'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=0.000000
    dbObj.weight_kg=1414.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoSST-4.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=260.000000
    dbObj.damageModel='uBlast250kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-300.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=15.142672
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
    dbObj.maxTurnRate_degps=40.000000
    dbObj.maxDepth_m=400.000000
    dbObj.battery_kJ=841.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='SST-4 M0 SH'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=23.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
