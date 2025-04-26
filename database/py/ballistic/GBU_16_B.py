# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='GBU-16/B'
    dbObj.natoClass='GBU-16/B'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=454.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoGBU-16.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='Need laser designator on attacking aircraft for this to work.  Uses mk-83 as its payload.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Blast200kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=200.000000
    dbObj.maxLaunchAlt_m=10000.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=15.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.002900
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass='Laser seeker 15km'
    dbObj.smartError_m=9.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
