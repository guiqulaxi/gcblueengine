import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='AH-1W Super Cobra'
    dbObj.natoClass='AH-1W Super Cobra'
    dbObj.mnModelType=6
    dbObj.mnType=34
    dbObj.cost=16000000.000000
    dbObj.weight_kg=4953.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Attack'
    dbObj.imageList='sh3h.jpg'
    dbObj.iconFileName='air/AdvicoAH1W.jpg'
    dbObj.mz3DModelFileName='s-70.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APR-44 RWR','Eyeball 20/10.n','Eyeball 20/10b.n','Eyeball 20/10c.n','NTS FLIR','TOW Operator.n']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=152.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=23.000000
    dbObj.mfFuelCapacity_kg=946.000000
    dbObj.mfFuelRate_kgps=0.178567
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='AH-1W Super Cobra durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['20mm M197 Chain Gun Cobra','AH-1 Outboard Pylon','AH-1 Inboard Pylon','AH-1 Inboard Pylon','AH-1 Outboard Pylon','ALE-39 CMD','ALE-39 CMD']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[220.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[-14.000000,5.000000,5.000000,5.000000,5.000000,-45.000000,-45.000000]
    dbObj.launcherFireControl=['','TOW Operator.n','TOW Operator.n','TOW Operator.n','TOW Operator.n','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=13.810000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=10.960000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_Rot_S_2V'
    airDetectionDBObject.IR_ModelB='IR_Rot_S_2V'
    airDetectionDBObject.IR_ModelC='IR_Rot_S_2V'
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
    dbObj.maxTakeoffWeight_kg=6690.000000
    dbObj.maxAltitude_m=4270.000000
    dbObj.climbRate_mps=44.000000
    dbObj.gmax=2.500000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
