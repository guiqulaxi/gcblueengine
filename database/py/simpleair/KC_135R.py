import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='KC-135R'
    dbObj.natoClass='KC-135R'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=39600000.000000
    dbObj.weight_kg=44663.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1957.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Tanker'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoKC135R.jpg'
    dbObj.mz3DModelFileName='civilairliner.xml'
    dbObj.notes='Scott Daniels [lancaster123]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=504.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=5.000000
    dbObj.mfFuelCapacity_kg=90719.000000
    dbObj.mfFuelRate_kgps=0.100000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='KC-135R durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=['KC-135R CARGO']
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
    airDetectionDBObject.RCS_dBsm=20.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=17.049999
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_LP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=146000.000000
    dbObj.maxAltitude_m=15200.000000
    dbObj.climbRate_mps=8.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=3
    dbObj.fuelOut_kgps=50.650002
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=3600.000000
    dbObj.CalculateParams()
    return dbObj
