import pygcb
def CreateDBObject():
    dbObj=pygcb.tcTorpedoDBObject()
    dbObj.mzClass='NT37E'
    dbObj.natoClass='NT37E'
    dbObj.mnModelType=9
    dbObj.mnType=130
    dbObj.cost=600000.000000
    dbObj.weight_kg=650.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1983.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='torp/icoNT-37E.jpg'
    dbObj.mz3DModelFileName='mk-46.xml'
    dbObj.notes='[dewitt] Friedman. World Naval Weapon Systems. Greater aquisition range,50-90% greater active, 100-200% greater passive owing to reduced noise and especially reduced flow noise.  Otherwise as NT37C.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='uBlast150kg'
    dbObj.damageEffect='SubDmg1'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=17
    dbObj.minLaunchAlt_m=-999.000000
    dbObj.maxLaunchAlt_m=0.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=28.580063
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
    dbObj.maxTurnRate_degps=20.000000
    dbObj.maxDepth_m=305.000000
    dbObj.battery_kJ=1543.199951
    dbObj.batteryRate_kW=1.000000
    dbObj.maxSpeed_kts=36.000000
    dbObj.acceleration_ktsps=3.000000
    dbObj.sonarClass='NT37E Seeker'
    dbObj.wireGuidance=True
    dbObj.preEnableSpeed_kts=36.000000
    dbObj.weaponType=1
    dbObj.CalculateParams()
    return dbObj
