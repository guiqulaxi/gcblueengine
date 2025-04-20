import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='F-17 Mod2'
    dbObj.natoClass='F-17 Mod2'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=750000.000000
    dbObj.weight_kg=1410.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1988.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoF-17.2.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='Extrapolated a little differently from how it was done with F-17mod1.  pre-enabled speed is unchanged, and no mention of greater pre-enabled range is given, enabled range is increased to 22,000m, and the enabled range is 20km.  If we can go faster at no cost in range, then we have more power to spend, and can gain in range in the pre-enabled phase.  GCB doesn\'t work like this however.  So I extrpolated as follows.  500m at 24kts is 38.26562 seconds, 500m at 40ktsis 22.95937 seconds.  Combined this is 61.225 seconds to cover 1km.  2079/61.225 then equals range in km, or 33.95672.  3 more seconds makes it 34km, so i granted the additional time as well.  '
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=50.000000
    dbObj.damageModel='uBlast250kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=42.842934
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T1:very large torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=12.000000
    dbObj.maxDepth_m=600.000000
    dbObj.battery_kJ=2082.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=40.000000
    dbObj.acceleration_ktsps=8.000000
    dbObj.sonarClass='MU-90 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=24.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
