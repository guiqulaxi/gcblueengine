import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Sea Harrier FA.Mk.2'
    dbObj.natoClass='Sea Harrier FA.Mk.2'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=5900.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='Strike Fighter'
    dbObj.imageList='harrier-gr3.jpg'
    dbObj.iconFileName='air/AdvicoHarrierFA2.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Blue Vixen','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Sky Guardian RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=529.190002
    dbObj.mfAccel_ktsps=20.150000
    dbObj.mfTurnRate_degps=33.610001
    dbObj.mfFuelCapacity_kg=3467.500000
    dbObj.mfFuelRate_kgps=1.600000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Sea Harrier FA.Mk.2 durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['Harrier FRS.2 1-5','Harrier FRS.2 2-4','Harrier FRS.1 3','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Blue Vixen','Blue Vixen','Blue Vixen','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.190000
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
    dbObj.maxTakeoffWeight_kg=11600.000000
    dbObj.maxAltitude_m=15000.000000
    dbObj.climbRate_mps=341.260010
    dbObj.gmax=8.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=75662.476562
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=97119.000000
    dbObj.abThrustSpeedSlope=0.000000
    dbObj.mfAfterburnFuelRate_kgps=2.190000
    dbObj.mfCdpsub=0.750000
    dbObj.mfCdptran=1.500000
    dbObj.mfCdpsup=2.500000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.000000
    dbObj.cruiseSpeed_mps=140.000000
    dbObj.stallSpeed_mps=60.000000
    dbObj.thrustTable=[0.950000,0.900000,0.880000,0.850000,0.800000,0.750000,0.700000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,0.900000,0.950000,1.100000,1.500000,2.000000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
