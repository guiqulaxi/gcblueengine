import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Kfir C.10'
    dbObj.natoClass='Kfir C.10'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=7825.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2010.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Israel'
    dbObj.designation='Fighter'
    dbObj.imageList='kfirce.jpg'
    dbObj.iconFileName='air/AdvicoKFIRC10.jpg'
    dbObj.mz3DModelFileName='kfir.xml'
    dbObj.notes='Marcos. http://www.timawa.net/forum/index.php?topic=2507.15'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['EL/L-8222','EL/M-2032 AA','EL/M-2032 AG','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','SPS-2000']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1317.000000
    dbObj.mfAccel_ktsps=15.000000
    dbObj.mfTurnRate_degps=13.000000
    dbObj.mfFuelCapacity_kg=2572.000000
    dbObj.mfFuelRate_kgps=1.500000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Kfir C.10 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Kfir 07-06','Kfir 05-04','Kfir 03-02','Kfir 01','DM/A-202 Chaff','DM/A-202 Flare']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['EL/M-2032 AA','EL/M-2032 AA','EL/M-2032 AA','EL/M-2032 AA','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=4.770000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.800000
    airDetectionDBObject.irSignature_dB=0.000000
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
    dbObj.maxTakeoffWeight_kg=16500.000000
    dbObj.maxAltitude_m=17680.000000
    dbObj.climbRate_mps=233.000000
    dbObj.gmax=7.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=9.000000
    dbObj.maintenanceMin_s=7200.000000
    dbObj.maintenanceMax_s=7200.000000
    dbObj.militaryThrust_N=52900.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=83400.000000
    dbObj.abThrustSpeedSlope=0.007000
    dbObj.mfAfterburnFuelRate_kgps=6.500000
    dbObj.mfCdpsub=0.800000
    dbObj.mfCdptran=2.200000
    dbObj.mfCdpsup=2.000000
    dbObj.mfMcm=1.050000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[1.000000,0.950000,0.850000,0.800000,0.750000,0.650000,0.300000,0.100000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.990000,0.920000,0.850000,0.820000,0.950000,1.500000,2.000000,1.800000,2.000000]
    dbObj.CalculateParams()
    return dbObj
