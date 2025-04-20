import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='30mm PGU-14/B API'
    dbObj.natoClass='30mm PGU-14/B API'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=0.690000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/gunammoico.jpg'
    dbObj.mz3DModelFileName='5-inch.xml'
    dbObj.notes='0.69kg round, 14 round burst'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=12.840000
    dbObj.damageModel='SolidPen0.1kg'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=1070.000000
    dbObj.targetFlags=15
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=2400.000000
    dbObj.minRange_km=0.160000
    dbObj.maxRange_km=2.400000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    dbObj.ballisticType=2
    dbObj.angleError_rad=0.005000
    dbObj.burstCount=14
    dbObj.burstDuration_s=0.215400
    dbObj.clusterCount=0
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
