import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='F-17 Mod1'
    dbObj.natoClass='F-17 Mod1'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=750000.000000
    dbObj.weight_kg=1410.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1985.000000
    dbObj.finalYear=1988.000000
    dbObj.country='France'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoF-17.1.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='unknown balance of pre and enabled ranged, extrapolated from F-17 base model.  It achieves 29km at 24kts, or 18km at 35kts, for a differences in battery depletion of 2.35x.  F-17 mod1 achieves 20km at 35kts.  So, F-17 Mod1 battery=18km/35kts, which is 1049.7 seconds, times 2.35 is 2066.2 seconds, times 24 kts pre-enabled is 32.2km maximum.  this range is then treated as GCB will do it.  16.1km at 35 kts is 845.6 seconds, 16.1km at 24kts is 1233seconds, combines is a total battery capacity of 2079 seconds.'
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
    dbObj.maxRange_km=37.433552
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
    dbObj.battery_kJ=2079.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=35.000000
    dbObj.acceleration_ktsps=8.000000
    dbObj.sonarClass='MU-90 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=24.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
