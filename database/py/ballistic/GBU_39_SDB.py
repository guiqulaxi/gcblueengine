# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='GBU-39 SDB'
    dbObj.natoClass='GBU-39 SDB'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=20000.000000
    dbObj.weight_kg=129.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2001.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoGBU-39.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='Not effective vs moving targets. Used Wikipedia 110 km standoff. Blast100kg to model more potent explosives.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Blast100kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=200.000000
    dbObj.maxLaunchAlt_m=12000.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=110.000000
    dbObj.probNoFaults=0.990000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=40.000000
    dbObj.acceptsUserCommands=True
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.003200
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass='GPS -Seeker-'
    dbObj.smartError_m=6.500000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
