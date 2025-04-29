# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Buccaneer S2'
    dbObj.natoClass='Buccaneer S2'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=13608.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1965.619995
    dbObj.finalYear=1994.000000
    dbObj.country='UK'
    dbObj.designation='Bomber'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoBUCS2.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Airpass 3','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Sky Guardian RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=600.000000
    dbObj.mfAccel_ktsps=22.389999
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=5695.000000
    dbObj.mfFuelRate_kgps=2.254100
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Buccaneer S2 durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['Buccaneer S1 Bay','Buccaneer S2 1-4','Buccaneer S1 1.5-3.5','Buccaneer S2 2-3']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.300000
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
    dbObj.maxTakeoffWeight_kg=28123.000000
    dbObj.maxAltitude_m=12200.000000
    dbObj.climbRate_mps=46.000000
    dbObj.gmax=3.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=101200.000000
    dbObj.militaryThrustSpeedSlope=0.001000
    dbObj.mfAfterburnThrust_N=101200.000000
    dbObj.abThrustSpeedSlope=0.001000
    dbObj.mfAfterburnFuelRate_kgps=2.254100
    dbObj.mfCdpsub=1.350000
    dbObj.mfCdptran=2.700000
    dbObj.mfCdpsup=4.050000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=90.000000
    dbObj.stallSpeed_mps=45.000000
    dbObj.thrustTable=[0.850000,0.900000,0.850000,0.760000,0.650000,0.500000,0.220000,0.040000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[0.980000,0.950000,0.900000,0.950000,1.100000,1.500000,2.500000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
