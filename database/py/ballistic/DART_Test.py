# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='DART test'
    dbObj.natoClass='DART test'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=4.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/gunammoico.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='0.3 mils accuracy, this is, simply, crazy, at 6km range this is a CEP of just 3.6m, 1.8m radius.  Considering the warhead has a detonation range of 10m, then its likely to detonate ahead of the target, very small fragspread values may be workable.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Harmless'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=2245.000000
    dbObj.targetFlags=11
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=6000.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=6.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass='DART Test'
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=200.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.000260
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
