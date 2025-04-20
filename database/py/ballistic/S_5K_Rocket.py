import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='S-5K Rocket'
    dbObj.natoClass='S-5K Rocket'
    dbObj.mnModelType=24
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=3.640000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1955.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoS-5K.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes='altered according to janes air launched weapons'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.330000
    dbObj.damageModel='Pen2kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=550.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.200000
    dbObj.maxRange_km=3.500000
    dbObj.probNoFaults=0.960000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=5
    dbObj.angleError_rad=0.030000
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
