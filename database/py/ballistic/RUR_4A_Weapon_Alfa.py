# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='RUR-4A Weapon Alfa'
    dbObj.natoClass='RUR-4A Weapon Alfa'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=238.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1951.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoEDS25A.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Harmless'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=70.000000
    dbObj.targetFlags=20
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.250000
    dbObj.maxRange_km=0.900000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass='RBU-DC-RUR-4A Weapon Alfa'
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.000000
    dbObj.ballisticType=0
    dbObj.angleError_rad=0.006000
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=1
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
