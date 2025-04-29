# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='A-20A'
    dbObj.natoClass='A-20A'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=6827.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1939.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoA20A.jpg'
    dbObj.mz3DModelFileName='c-130.xml'
    dbObj.notes='thrust estimated by HP * 1/3 * prop_area_m2.  propstall modelled with negative speed slope.  Assuming 36m2 when unknown.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=320.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=12.000000
    dbObj.mfFuelCapacity_kg=4479.500000
    dbObj.mfFuelRate_kgps=0.800000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='A-20A durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['0.30in(7.7m) Browning M1(900)(x2)','0.30in(7.7m) Browning M1(900)(x2)','A-20A Bay']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[0.000000,20.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=4.770000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=7.430000
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
    dbObj.maxTakeoffWeight_kg=12338.000000
    dbObj.maxAltitude_m=7225.000000
    dbObj.climbRate_mps=10.200000
    dbObj.gmax=4.500000
    dbObj.minimumRunway_m=741.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=15.000000
    dbObj.maintenanceMin_s=5400.000000
    dbObj.maintenanceMax_s=5400.000000
    dbObj.militaryThrust_N=38400.000000
    dbObj.militaryThrustSpeedSlope=-0.002100
    dbObj.mfAfterburnThrust_N=38400.000000
    dbObj.abThrustSpeedSlope=-0.002100
    dbObj.mfAfterburnFuelRate_kgps=0.800000
    dbObj.mfCdpsub=1.065000
    dbObj.mfCdptran=1.800000
    dbObj.mfCdpsup=1.600000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=76.000000
    dbObj.stallSpeed_mps=43.200001
    dbObj.thrustTable=[0.900000,0.820000,0.600000,0.200000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,1.100000,1.400000,3.000000,5.000000,5.000000,5.000000,5.000000,5.000000]
    dbObj.CalculateParams()
    return dbObj
