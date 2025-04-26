# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='50mm (2in) FFAR Rockets'
    dbObj.natoClass='50mm (2in) FFAR Rockets'
    dbObj.mnModelType=24
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=3.400000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1948.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoSNEB 68.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.330000
    dbObj.damageModel='Blast1kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=920.000000
    dbObj.targetFlags=7
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.100000
    dbObj.maxRange_km=1.400000
    dbObj.probNoFaults=0.980000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=5
    dbObj.angleError_rad=0.004800
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
