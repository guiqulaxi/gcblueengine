# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='GBU-15/B'
    dbObj.natoClass='GBU-15/B'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=200000.000000
    dbObj.weight_kg=454.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoGBU-15.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='GBU-15(V)2/B imaging IR. No need for laser designator.  Uses mk-83 as its payload.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Blast420kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=200.000000
    dbObj.maxLaunchAlt_m=12000.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=15.000000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=20.000000
    dbObj.acceptsUserCommands=True
    dbObj.detonationRange_m=3.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.002900
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass='Maverick Infrared'
    dbObj.smartError_m=5.000000
    dbObj.lockOnAfterLaunch=True
    dbObj.CalculateParams()
    return dbObj
