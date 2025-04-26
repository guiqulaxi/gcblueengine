# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Typhoon'
    dbObj.natoClass='Typhoon'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=50000000.000000
    dbObj.weight_kg=11000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2003.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='typhoon.jpg'
    dbObj.iconFileName='air/AdvicoTyphoon.jpg'
    dbObj.mz3DModelFileName='f-16.xml'
    dbObj.notes='the engines have an SFC of 23g/Kn.s dry and 49g/kN.s wet, so they consume as a pair 2.76kg/s dry and 8.82kg/s wet, its not everyday I have raw consumption rates to work with, lol.  Generally thought to be a sub 1mÃƒâ€šÃ‚Â² RCS, assuming this to be 0.8mÃƒâ€šÃ‚Â².  Best reference i found was a 300nm combat radius, assume 80% fuel used, thus 300nm is 555.6km, is 1111.2 round trip, plus 20% reserve is 1333.44lkm.  Assigned the fighter this range.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DASS-ECM','DASS-ESM','ECR-90','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Litening-3 LDP','PIRATE IRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1350.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=27.000000
    dbObj.mfFuelCapacity_kg=5000.000000
    dbObj.mfFuelRate_kgps=2.760000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Typhoon durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Typhoon-W1','Typhoon-W2','Typhoon-W3','Typhoon-F1','Typhoon-F2','27mm BK27-Cannon(180)','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['ECR-90','ECR-90','ECR-90','ECR-90','ECR-90','ECR-90','','']
    dbObj.launcherFireControl2=['PIRATE IRST','PIRATE IRST','PIRATE IRST','PIRATE IRST','PIRATE IRST','PIRATE IRST','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-0.961000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.890000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=23500.000000
    dbObj.maxAltitude_m=19810.000000
    dbObj.climbRate_mps=315.000000
    dbObj.gmax=9.500000
    dbObj.minimumRunway_m=700.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=120000.000000
    dbObj.militaryThrustSpeedSlope=0.000100
    dbObj.mfAfterburnThrust_N=180000.000000
    dbObj.abThrustSpeedSlope=0.000900
    dbObj.mfAfterburnFuelRate_kgps=8.820000
    dbObj.mfCdpsub=1.125000
    dbObj.mfCdptran=1.358000
    dbObj.mfCdpsup=1.125000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,0.800000,0.635000,0.450000,0.235000,0.140000,0.025000,0.001250]
    dbObj.fuelEfficiencyTable=[1.090000,1.190000,1.300000,1.420000,1.551000,1.950000,3.300000,10.000000,20.000000,20.000000]
    dbObj.CalculateParams()
    return dbObj
