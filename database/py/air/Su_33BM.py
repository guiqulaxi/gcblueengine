import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Su-33BM'
    dbObj.natoClass='Su-33BM'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=55000000.000000
    dbObj.weight_kg=18400.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2010.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='su27-34p04.jpg;su27-2.jpg;su27-34p03.jpg;su27-06.jpg'
    dbObj.iconFileName='air/AdvicoSU33BM.jpg'
    dbObj.mz3DModelFileName='su-27.xml'
    dbObj.notes='Contributed by greengills'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Irbis-E','Khibiny-M ECM','NIIP N-012','OEPS-30 IRST','SPO-32 Pastel ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1435.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=22.500000
    dbObj.mfFuelCapacity_kg=9400.000000
    dbObj.mfFuelRate_kgps=5.100000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Su-33BM durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['GSh-30-1 30mm','Su-30 F','Su-30 W1','Su-30 W2','APP-15 CMD (Left Bank)','APP-15 CMD (Right Bank)']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','Fslg','Tips','Wings','CM1','CM2']
    dbObj.launcherFOV_deg=[20.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Irbis-E','Irbis-E','Irbis-E','Irbis-E','','']
    dbObj.launcherFireControl2=['OEPS-30 IRST','OEPS-30 IRST','OEPS-30 IRST','OEPS-30 IRST','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=4.030000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.090000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=33000.000000
    dbObj.maxAltitude_m=19800.000000
    dbObj.climbRate_mps=325.000000
    dbObj.gmax=8.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=149000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=245160.000000
    dbObj.abThrustSpeedSlope=0.001300
    dbObj.mfAfterburnFuelRate_kgps=13.600000
    dbObj.mfCdpsub=1.200000
    dbObj.mfCdptran=2.200000
    dbObj.mfCdpsup=2.000000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.800000,0.750000,0.700000,0.500000,0.300000,0.100000,0.050000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,0.850000,0.850000,1.000000,1.400000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
