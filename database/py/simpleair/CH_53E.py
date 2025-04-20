import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='CH-53E'
    dbObj.natoClass='CH-53E'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=16000000.000000
    dbObj.weight_kg=5382.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=1995.000000
    dbObj.country='USA'
    dbObj.designation='Cargo'
    dbObj.imageList='sh3h.jpg'
    dbObj.iconFileName='air/AdvicoCH53E.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='armament and dispensors stripped, is only armed with machine guns, no provisions for torpedos or buoys, its essentially a heavy helo transport for moving marines around.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','LN-66 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=144.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=2552.964111
    dbObj.mfFuelRate_kgps=0.162000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='CH-53E durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=['CH-53E Cargo']
    dbObj.magazineId=[0]
    dbObj.launcherId=[]
    dbObj.launcherName=[]
    dbObj.launcherFOV_deg=[]
    dbObj.launcherAz_deg=[]
    dbObj.launcherEl_deg=[]
    dbObj.launcherFireControl=[]
    dbObj.launcherFireControl2=[]
    dbObj.launcherIsReloadable=[]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.810000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=10.960000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_L_3'
    airDetectionDBObject.IR_ModelB='IR_Rot_L_3'
    airDetectionDBObject.IR_ModelC='IR_Rot_L_3'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-999.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTakeoffWeight_kg=9752.000000
    dbObj.maxAltitude_m=4500.000000
    dbObj.climbRate_mps=11.000000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
