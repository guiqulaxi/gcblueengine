import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='AGM-130'
    dbObj.natoClass='AGM-130'
    dbObj.mnModelType=21
    dbObj.mnType=512
    dbObj.cost=900000.000000
    dbObj.weight_kg=1323.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1994.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoGBAGM130.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='modeling this as a glide bomb for now, could also try modeling using a missile with payload'
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
    dbObj.maxRange_km=70.000000
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=50.000000
    dbObj.acceptsUserCommands=True
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=3
    dbObj.angleError_rad=0.003200
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass='GPS -Seeker-'
    dbObj.smartError_m=5.000000
    dbObj.lockOnAfterLaunch=True
    dbObj.CalculateParams()
    return dbObj
