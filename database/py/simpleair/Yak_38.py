import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Yak-38'
    dbObj.natoClass='Yak-38 Forger-A'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=7385.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Strike Fighter'
    dbObj.imageList='yak38.jpg;yak38-2.jpg'
    dbObj.iconFileName='air/AdvicoYak38.jpg'
    dbObj.mz3DModelFileName='Yak-38.xml'
    dbObj.notes='Dont have capability for Kh-23 command only or beam-rider? need to add approximation'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Generic Airborne AS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=690.000000
    dbObj.mfAccel_ktsps=25.000000
    dbObj.mfTurnRate_degps=12.000000
    dbObj.mfFuelCapacity_kg=2000.000000
    dbObj.mfFuelRate_kgps=0.550000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Yak-38 durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['Yak-38 Station 1','Yak-38 Station 2','GSh-6-23']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,20.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.530000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=11300.000000
    dbObj.maxAltitude_m=12000.000000
    dbObj.climbRate_mps=70.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
