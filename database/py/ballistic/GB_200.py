# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='GB-200'
    dbObj.natoClass='GB-200'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=500.000000
    dbObj.weight_kg=200.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoGB-200.jpg'
    dbObj.mz3DModelFileName='mk-82.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=200.000000
    dbObj.damageModel='Pen70kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=4
    dbObj.minLaunchAlt_m=200.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=20.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=1
    dbObj.angleError_rad=0.004200
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
