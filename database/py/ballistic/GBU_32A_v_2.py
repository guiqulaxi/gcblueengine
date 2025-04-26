# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='GBU-32A(v)2'
    dbObj.natoClass='GBU-32A(v)2'
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
    dbObj.iconFileName='ball/icoGBU-32A.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='GPS guidance only.  Uses mk-83 as its payload.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=500.000000
    dbObj.damageModel='Blast200kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=200.000000
    dbObj.maxLaunchAlt_m=10000.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=40.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.003200
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass='GPS -Seeker-'
    dbObj.smartError_m=10.000000
    dbObj.lockOnAfterLaunch=True
    dbObj.CalculateParams()
    return dbObj
