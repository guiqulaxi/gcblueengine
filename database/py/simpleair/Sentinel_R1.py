import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Sentinel R1'
    dbObj.natoClass='Sentinel R1'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=22600.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2008.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='EW'
    dbObj.imageList='a330.jpg'
    dbObj.iconFileName='air/AdvicoSentinelR1.jpg'
    dbObj.mz3DModelFileName='civilairliner.xml'
    dbObj.notes='Alec Walker'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Sentinel','Sentinel']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,270.000000,90.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=513.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=4.000000
    dbObj.mfFuelCapacity_kg=21850.000000
    dbObj.mfFuelRate_kgps=0.735000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Sentinel R1 durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.510000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_H_LP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=44453.000000
    dbObj.maxAltitude_m=15545.000000
    dbObj.climbRate_mps=7.270000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=1900.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=3600.000000
    dbObj.CalculateParams()
    return dbObj
