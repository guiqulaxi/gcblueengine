import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F-16C/D Blk 25'
    dbObj.natoClass='F-16C/D Blk 25'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=8272.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='f16a.jpg'
    dbObj.iconFileName='air/AdvicoF16CD25.jpg'
    dbObj.mz3DModelFileName='f-16.xml'
    dbObj.notes='I have found wet and dry SFC values for the F100-PW-229 engine, which is used for the F-16C/D Block 52, and for the F110-GE-129 used by the F-16 C Block 50.  I have wet SFC\'s for the remaining engines used in the PW series, their dry values will be extrapolated.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALR-69 RWR','APG-66(v)2','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1300.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=3228.000000
    dbObj.mfFuelRate_kgps=1.380190
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F-16C/D Blk 25 durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['F-16 Blk25 2-8','F-16 Blk25 2-8','F-16 Blk25 3-7','F-16 Blk25 4-6','F-16 Blk1 5','ALE-40 CMD','ALE-40 CMD','M61A Cannon']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APG-66(v)2','APG-66(v)2','APG-66(v)2','APG-66(v)2','APG-66(v)2','','','APG-66(v)2']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=4.770000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.460000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_S_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_S_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_S_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=19187.000000
    dbObj.maxAltitude_m=16764.000000
    dbObj.climbRate_mps=255.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=1800.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=15.000000
    dbObj.maintenanceMin_s=5400.000000
    dbObj.maintenanceMax_s=5400.000000
    dbObj.militaryThrust_N=63900.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=105720.000000
    dbObj.abThrustSpeedSlope=0.002730
    dbObj.mfAfterburnFuelRate_kgps=5.760680
    dbObj.mfCdpsub=0.800000
    dbObj.mfCdptran=1.400000
    dbObj.mfCdpsup=1.600000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=126.040001
    dbObj.stallSpeed_mps=65.334000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,1.000000,0.840000,0.640000,0.180000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.060000,1.080000,1.060000,1.030000,1.000000,1.160000,3.000000,10.000000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
