# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='KAB-500Kr'
    dbObj.natoClass='KAB-500Kr'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=5000.000000
    dbObj.weight_kg=460.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoKAB-500KR.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Pen500kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=500.000000
    dbObj.maxLaunchAlt_m=5000.000000
    dbObj.minRange_km=0.250000
    dbObj.maxRange_km=30.000000
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
    dbObj.sensorClass='TV seeker 15km'
    dbObj.smartError_m=4.000000
    dbObj.lockOnAfterLaunch=True
    dbObj.CalculateParams()
    return dbObj
