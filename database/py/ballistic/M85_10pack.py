# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='M85 10pack'
    dbObj.natoClass='M85 10pack'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=10.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList='0'
    dbObj.iconFileName='ball/gunammoico.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.000000
    dbObj.damageModel='BlastFrag10kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.000000
    dbObj.maxRange_km=100.000000
    dbObj.probNoFaults=0.990000
    dbObj.payloadClass='M85 DPICM'
    dbObj.payloadQuantity=10
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=100000.000000
    dbObj.ballisticType=1
    dbObj.angleError_rad=0.001088
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
