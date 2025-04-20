import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='C-130H'
    dbObj.natoClass='C-130H'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=38800.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Cargo'
    dbObj.imageList='c130.jpg'
    dbObj.iconFileName='air/AdvicoC130H.jpg'
    dbObj.mz3DModelFileName='c-130.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALR-2002 RWR','AN/AAR-54 MAWS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=318.000000
    dbObj.mfAccel_ktsps=6.000000
    dbObj.mfTurnRate_degps=9.000000
    dbObj.mfFuelCapacity_kg=20100.000000
    dbObj.mfFuelRate_kgps=0.100000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='C-130H durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['AN/ALE-47 CMD','AN/ALE-47 CMD','AN/AAQ-24 Nemesis DIRCM']
    dbObj.maMagazineClass=['C-130H Cargo Bay']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['CM1','CM2','CM2']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=15.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.100000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_TP_4_M0.85'
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
    dbObj.maxTakeoffWeight_kg=69750.000000
    dbObj.maxAltitude_m=10000.000000
    dbObj.climbRate_mps=9.000000
    dbObj.gmax=2.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=10000.000000
    dbObj.maintenanceMax_s=10000.000000
    dbObj.CalculateParams()
    return dbObj
