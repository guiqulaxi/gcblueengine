import pygcb
def CreateDBObject():
    dbObj=pygcb.tcBallisticDBObject()
    dbObj.mzClass='375 Bofors ASRL x4'
    dbObj.natoClass='375 Bofors ASRL x4'
    dbObj.mnModelType=14
    dbObj.mnType=512
    dbObj.cost=0.000000
    dbObj.weight_kg=400.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='ball/icoSUASRL375.jpg'
    dbObj.mz3DModelFileName='mk-84.xml'
    dbObj.notes='DetonationRange_m is altitude AGL that payload is released. Max of 16 for payload quantity. I don\'t know anything about the rocket itself, assuming 100kg w/45kG warhead.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=1000.000000
    dbObj.damageModel='Harmless'
    dbObj.damageEffect='ToughWeapon'
    dbObj.launchSpeed_mps=300.000000
    dbObj.targetFlags=20
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=99999.000000
    dbObj.minRange_km=0.300000
    dbObj.maxRange_km=3.600000
    dbObj.probNoFaults=1.000000
    dbObj.payloadClass='RBU-Rocket-375mm Bofors ASRL'
    dbObj.payloadQuantity=4
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10000.000000
    dbObj.ballisticType=0
    dbObj.angleError_rad=0.001600
    dbObj.burstCount=1
    dbObj.burstDuration_s=0.000000
    dbObj.clusterCount=1
    dbObj.clusterEffectRadius_m=0.000000
    dbObj.sensorClass=''
    dbObj.smartError_m=0.000000
    dbObj.lockOnAfterLaunch=False
    dbObj.CalculateParams()
    return dbObj
