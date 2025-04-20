import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='RBU-Hedgehog2'
    dbObj.natoClass='RBU-Hedgehog2'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=29.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoHedgehog.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='needs to deploy 24 submunitions, GCB limit is 16, as such, deploying 8 and then each of those will deploy a further three for 24 total.  Cannot do patterned deployments, must simply accept that it will be random.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Blast16kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=300.000000
    dbObj.targetFlags=20
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.000000
    dbObj.maxRange_km=0.250000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass='RBU-DC-Hedgehog'
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10000.000000
    dbObj.ballisticType=1
    dbObj.angleError_rad=0.200000
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=1
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
