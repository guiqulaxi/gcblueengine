import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='S-8B 80mm'
    dbObj.natoClass='S-8B 80mm'
    dbObj.mnModelType=24
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=15.200000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1955.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoS-8B.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.330000
    dbObj.damageModel='Blast3.6kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=690.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=1.200000
    dbObj.maxRange_km=2.200000
    dbObj.probNoFaults=0.960000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=5
    dbObj.angleError_rad=0.020000
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
