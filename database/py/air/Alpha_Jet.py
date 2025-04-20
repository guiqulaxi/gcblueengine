import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Alpha Jet'
    dbObj.natoClass='Alpha Jet'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=3515.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1978.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoALPHA.jpg'
    dbObj.mz3DModelFileName='f-4.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=800.000000
    dbObj.mfAccel_ktsps=12.890000
    dbObj.mfTurnRate_degps=12.000000
    dbObj.mfFuelCapacity_kg=1520.000000
    dbObj.mfFuelRate_kgps=0.600000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Alpha Jet durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['27mm MLG 27 Alphajet','Alpha3','Alpha1','Alpha2','CM Ejector 2','CM Ejector 2']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[20.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,-40.000000,-40.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.530000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_S_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_S_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_S_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=8000.000000
    dbObj.maxAltitude_m=13700.000000
    dbObj.climbRate_mps=61.000000
    dbObj.gmax=6.000000
    dbObj.minimumRunway_m=520.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=26480.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=26480.000000
    dbObj.abThrustSpeedSlope=0.000000
    dbObj.mfAfterburnFuelRate_kgps=0.600000
    dbObj.mfCdpsub=0.270000
    dbObj.mfCdptran=0.350000
    dbObj.mfCdpsup=0.250000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.300000
    dbObj.cruiseSpeed_mps=110.000000
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[1.000000,1.000000,0.900000,0.750000,0.550000,0.250000,0.080000,0.010000,0.010000,0.010000]
    dbObj.fuelEfficiencyTable=[0.940000,0.960000,1.060000,1.200000,2.000000,3.000000,5.000000,10.000000,60.000000,200.000000]
    dbObj.CalculateParams()
    return dbObj
