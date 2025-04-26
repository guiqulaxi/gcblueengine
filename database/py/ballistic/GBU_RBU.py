# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='GBU-RBU'
    dbObj.natoClass='GBU-RBU'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=3100.000000
    dbObj.weight_kg=468.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2002.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoGBU-32B.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='GPS guidance only.  Uses BLU-110/B as its payload.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=500.000000
    dbObj.damageModel='Harmless'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=800.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=10000.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=40.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass='Mk-9 DC'
    dbObj.payloadQuantity=12
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=500.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.003200
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=500.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
