# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='Gen90AT'
    dbObj.natoClass='Gen90AT'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=3.600000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList='0'
    dbObj.iconFileName='ball/gunammoico.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes='Can penetrate up to 120mm steel armorat 60? obliquity, or 310mm at 90?.  The projectile has a maximum range of 1800m, but maximum effective range is 1100m.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.000000
    dbObj.damageModel='SolidPen0.7kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=750.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.000000
    dbObj.maxRange_km=1.100000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=0
    dbObj.angleError_rad=0.001910
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
