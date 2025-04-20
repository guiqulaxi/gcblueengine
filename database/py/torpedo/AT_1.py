import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='AT-1'
    dbObj.natoClass='AT-1'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=500000.000000
    dbObj.weight_kg=560.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoAT-1.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='Warhead size is given as a range of 70-160, using the average of the two, 115kg.  it does not have a two speed motor.  it performs a cirular search with a 60-70m radius, this gives turn rate, since 65m yields a roughly 204m circumference, and at 27 kts it can cover this in 170148s, 360° in that time is 24.48733°/sec.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast115kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=5.370800
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=10.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T3:torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=24.500000
    dbObj.maxDepth_m=400.000000
    dbObj.battery_kJ=360.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=29.000000
    dbObj.acceleration_ktsps=2.000000
    dbObj.sonarClass='AT-2M seeker'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=29.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
