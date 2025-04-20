import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Vastergotland'
    dbObj.natoClass='Vastergotland'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=1494000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1987.905029
    dbObj.finalYear=2005.000000
    dbObj.country='Sweden'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['CSU 83-2 Active','CSU 83-2 Bow Passive','CSU 83-2 Port Flank Passive','CSU 83-2 Stbd Flank Passive','ESM-1','Periscope-1','Scanter 2001']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,270.000000,90.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=1.300000
    dbObj.mfTurnRate_degps=6.000000
    dbObj.mfFuelCapacity_kg=3401660.000000
    dbObj.mfFuelRate_kgps=1.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Vastergotland durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['Gotland 400mm','Gotland 400mm','Gotland 400mm','Gotland 533mm','Gotland 533mm','Gotland 533mm','Gotland 533mm','Gotland 533mm','Gotland 533mm']
    dbObj.maMagazineClass=['Gotland Torpedo Racks']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=6.300000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=0.300000
    airDetectionDBObject.irSignature_dB=4.300000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=7.170000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='SwK190'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.600000
    dbObj.surfaceSpeed_kts=10.000000
    dbObj.mfMaxDepth_m=300.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=16.000000
    dbObj.CalculateParams()
    return dbObj
