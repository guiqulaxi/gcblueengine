import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='Bomblet-10kg'
    dbObj.natoClass='Bomblet-10kg'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=300.000000
    dbObj.weight_kg=10.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1960.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/mk82ico.jpg'
    dbObj.mz3DModelFileName='mk-82.xml'
    dbObj.notes='Set angleError_rad larger for more spread'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=250.000000
    dbObj.damageModel='Blast9kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=100.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.100000
    dbObj.maxRange_km=5.000000
    dbObj.probNoFaults=0.990000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=1
    dbObj.angleError_rad=0.002300
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
