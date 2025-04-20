import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='Mk-46 Mod5'
    dbObj.natoClass='Mk-46 Mod5'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=700000.000000
    dbObj.weight_kg=231.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1979.000000
    dbObj.finalYear=2015.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoMK-46.5.jpg'
    dbObj.mz3DModelFileName='mark46mod5.xml'
    dbObj.notes='Also using as Mk-60 CAPTOR torpedo'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast50kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=500.000000
    dbObj.minRange_km=0.250000
    dbObj.maxRange_km=13.745955
    dbObj.probNoFaults=0.950000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.000000
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='T4:small torpedo'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=450.000000
    dbObj.battery_kJ=668.000000
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=40.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='MK-46 Torpedo Sonar'
    dbObj.wireGuidance=False
    dbObj.preEnableSpeed_kts=26.700001
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
