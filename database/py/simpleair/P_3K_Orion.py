import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='P-3K Orion'
    dbObj.natoClass='P-3K Orion'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=36000000.000000
    dbObj.weight_kg=27890.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.000000
    dbObj.finalYear=2999.000000
    dbObj.country='New Zealand'
    dbObj.designation='ASuW'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoP3K.JPG'
    dbObj.mz3DModelFileName='P-3 Orion.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=[]
    sensorPlatformDBObject.sensorAz=[]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=410.000000
    dbObj.mfAccel_ktsps=15.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=28350.000000
    dbObj.mfFuelRate_kgps=1.559200
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='P-3K Orion durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['17 DICASS Launcher','17 LOFAR Launcher','50 DIFAR Launcher','P-3 9-18','P-3C 10-17','P-3C 11-16','P-3 12-15','P-3 13-14','P-3 Bay','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.140000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=14.520000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_H_TP_4_M0.85'
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
    dbObj.maxTakeoffWeight_kg=64410.000000
    dbObj.maxAltitude_m=10400.000000
    dbObj.climbRate_mps=16.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=1673.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
