import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Mi-25'
    dbObj.natoClass='Mi-25 Hind'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=15000000.000000
    dbObj.weight_kg=8500.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1972.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Attack'
    dbObj.imageList='mi24.jpg'
    dbObj.iconFileName='air/AdvicoMI25.JPG'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes='Just copied Mi-24D. I read somewhere that avionics are different but I couldn\'t find a good reference'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','FLIR-15','Laser-20km','RWR-1.5']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=180.000000
    dbObj.mfAccel_ktsps=15.000000
    dbObj.mfTurnRate_degps=25.000000
    dbObj.mfFuelCapacity_kg=1472.000000
    dbObj.mfFuelRate_kgps=0.150000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Mi-25 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Hind-D Turret','Hind-D Inner Hardpoints','Hind-D Outer Hardpoints','Hind-D Wingtips','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=['Cargo 4']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[270.000000,5.000000,5.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Laser-20km','Laser-20km','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.390000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.520000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='AirIR1'
    airDetectionDBObject.IR_ModelB='AirIR1'
    airDetectionDBObject.IR_ModelC='AirIR1'
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
    dbObj.maxTakeoffWeight_kg=11500.000000
    dbObj.maxAltitude_m=4500.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=1.750000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
