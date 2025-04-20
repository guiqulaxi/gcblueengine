import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F-15E'
    dbObj.natoClass='F-15E'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=29900000.000000
    dbObj.weight_kg=14300.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1979.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='f15c.jpg'
    dbObj.iconFileName='air/AdvicoF15E.jpg'
    dbObj.mz3DModelFileName='f-15E.xml'
    dbObj.notes='http://f-15e.info F-15E rarely use 3 external tanks, so use two tanks for range calculation. Assuming 5745 km ferry range with 2 tanks so about 4400 km with internal fuel only. Didnt bother to update thrust vs f-15c'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AAQ-33 SNIPER-XR','ALR-69 RWR','APG-70','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','LANTIRN']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1574.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=16.000000
    dbObj.mfFuelCapacity_kg=8380.000000
    dbObj.mfFuelRate_kgps=3.900000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F-15E durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['F-15E-STA28','F-15E-STA28AB','F-15E-STA28AB','F-15E-CFT-Outboard','F-15E-CFT-Inboard','F-15E-Centerline','ALE-45 Flare Dispenser','ALE-45 Chaff Dispenser','M61A Cannon']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['W1','W1','W2','OB','IB','C','CM','CM','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APG-70','APG-70','APG-70','APG-70','APG-70','APG-70','','','']
    dbObj.launcherFireControl2=['AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR','AAQ-33 SNIPER-XR','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.270000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.510000
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
    dbObj.maxTakeoffWeight_kg=36700.000000
    dbObj.maxAltitude_m=18200.000000
    dbObj.climbRate_mps=244.899994
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=1800.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=127837.398438
    dbObj.militaryThrustSpeedSlope=-0.000650
    dbObj.mfAfterburnThrust_N=258000.000000
    dbObj.abThrustSpeedSlope=0.003000
    dbObj.mfAfterburnFuelRate_kgps=12.000000
    dbObj.mfCdpsub=0.840000
    dbObj.mfCdptran=1.680000
    dbObj.mfCdpsup=2.400000
    dbObj.mfMcm=1.000000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=115.750000
    dbObj.stallSpeed_mps=69.449997
    dbObj.thrustTable=[0.870000,0.750000,0.700000,0.720000,0.675000,0.522000,0.200000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,0.900000,1.000000,1.100000,1.800000,2.500000,3.500000,4.000000]
    dbObj.CalculateParams()
    return dbObj
