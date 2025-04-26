# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='Breda 40/70L'
    dbObj.natoClass='Breda 40/70L'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=0.960000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1960.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/gunammoico.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes='Marcos'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1.300000
    dbObj.damageModel='SolidProjectile'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=1005.000000
    dbObj.targetFlags=11
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=12.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=2
    dbObj.angleError_rad=0.002720
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
