# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='RA-5C'
    dbObj.natoClass='RA-5C'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=17009.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Recon'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoRA5C.jpg'
    dbObj.mz3DModelFileName='f-15.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APD-7','APD-7','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','KA-51 6in Vigi Photo-1','Ka-50A 1.75in Vigi Photo-2','Ka-50A 12in Vigi Photo-2','Ka-50A 3in Vigi Photo-2','Ka-50A 6in Vigi Photo-2','Ka-53A 1.75in Vigi Photo-4','Ka-53A 1.75in Vigi Photo-4','Ka-53A 12in Vigi Photo-4','Ka-53A 12in Vigi Photo-4','Ka-53A 3in Vigi Photo-4','Ka-53A 3in Vigi Photo-4','Ka-53A 6in Vigi Photo-4','Ka-53A 6in Vigi Photo-4','Ka-58A 18in Pan Vigi Photo-3','Ka-58A 18in Pan Vigi Photo-3','Ka-58A 3in Pan Vigi Photo-3','Ka-58A 3in Pan Vigi Photo-3']
    sensorPlatformDBObject.sensorAz=[270.000000,90.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,270.000000,90.000000,270.000000,90.000000,270.000000,90.000000,270.000000,90.000000,0.000000,180.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1200.000000
    dbObj.mfAccel_ktsps=24.870001
    dbObj.mfTurnRate_degps=17.000000
    dbObj.mfFuelCapacity_kg=10194.200195
    dbObj.mfFuelRate_kgps=2.320000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='RA-5C durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[]
    dbObj.launcherName=[]
    dbObj.launcherFOV_deg=[]
    dbObj.launcherAz_deg=[]
    dbObj.launcherEl_deg=[]
    dbObj.launcherFireControl=[]
    dbObj.launcherFireControl2=[]
    dbObj.launcherIsReloadable=[]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=20.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.300000
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
    dbObj.maxTakeoffWeight_kg=36100.000000
    dbObj.maxAltitude_m=15900.000000
    dbObj.climbRate_mps=40.599998
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=96000.000000
    dbObj.militaryThrustSpeedSlope=0.001000
    dbObj.mfAfterburnThrust_N=152000.000000
    dbObj.abThrustSpeedSlope=0.003000
    dbObj.mfAfterburnFuelRate_kgps=8.444000
    dbObj.mfCdpsub=1.400000
    dbObj.mfCdptran=2.200000
    dbObj.mfCdpsup=1.800000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=120.000000
    dbObj.stallSpeed_mps=40.000000
    dbObj.thrustTable=[0.870000,0.830000,0.760000,0.700000,0.620000,0.480000,0.150000,0.050000,0.005000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.980000,0.960000,0.940000,0.920000,0.900000,1.250000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
