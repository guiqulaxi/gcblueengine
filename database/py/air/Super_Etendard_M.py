# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Super Etendard M'
    dbObj.natoClass='Super Etendard M'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=10000000.000000
    dbObj.weight_kg=6500.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='Bomber'
    dbObj.imageList='superentendard.jpg'
    dbObj.iconFileName='air/AdvicoSuperEtendardM.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes='one centerline, and 4 wing pylons, but just 2100kg in payload.  this means that payoads will be quite limited.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Agave','Damocles LASER','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','RWR SuE']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1050.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=16.000000
    dbObj.mfFuelCapacity_kg=2612.000000
    dbObj.mfFuelRate_kgps=1.800000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Super Etendard M durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['Super Etendard Outer Pylon','Super Etendard inner Pylon','Super Etendard inner Pylon','Super Etendard Centerline','DEFA 30mm','Alkan 5081','Alkan 5081']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','Gun','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,20.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Damocles LASER','Damocles LASER','Damocles LASER','Damocles LASER','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=6.600000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.790000
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
    dbObj.maxTakeoffWeight_kg=12000.000000
    dbObj.maxAltitude_m=13700.000000
    dbObj.climbRate_mps=50.000000
    dbObj.gmax=6.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=49000.000000
    dbObj.militaryThrustSpeedSlope=0.002250
    dbObj.mfAfterburnThrust_N=49000.000000
    dbObj.abThrustSpeedSlope=0.002250
    dbObj.mfAfterburnFuelRate_kgps=1.800000
    dbObj.mfCdpsub=0.500000
    dbObj.mfCdptran=0.650000
    dbObj.mfCdpsup=0.800000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=125.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.960000,0.830000,0.680000,0.540000,0.350000,-0.105000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[0.900000,0.800000,0.775000,0.850000,1.020000,1.400000,3.000000,4.000000,0.000000,0.000000]
    dbObj.CalculateParams()
    return dbObj
