import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Test Aircraft'
    dbObj.natoClass='Test Aircraft'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=20000000.000000
    dbObj.weight_kg=90000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=1940.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList='tu95.jpg'
    dbObj.iconFileName='air/jet_unk.jpg'
    dbObj.mz3DModelFileName='tu-95.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AEW radar 2','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Jammer 100W']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=400.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=8.000000
    dbObj.mfFuelCapacity_kg=870000.000000
    dbObj.mfFuelRate_kgps=1.700000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Test Aircraft durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['Bear G Kh-22 Launcher']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0]
    dbObj.launcherName=['Kh-22 Launcher']
    dbObj.launcherFOV_deg=[0.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=20.250000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=16.480000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_VL_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_VL_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_VL_H_TP_4_M0.85'
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
    dbObj.maxTakeoffWeight_kg=188000.000000
    dbObj.maxAltitude_m=15000.000000
    dbObj.climbRate_mps=50.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=30.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
