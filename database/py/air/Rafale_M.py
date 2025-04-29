# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Rafale M'
    dbObj.natoClass='Rafale M'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=138000000.000000
    dbObj.weight_kg=10460.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2006.000000
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='rafale.jpg'
    dbObj.iconFileName='air/AdvicoRafaleM.jpg'
    dbObj.mz3DModelFileName='F-22-Raptor.xml'
    dbObj.notes='SPECTRA active cancellation ECM being emulated by flat -10dB reduction in RCS. Going to assume RCS of roughly 1mÃƒâ€šÃ‚Â², will work with 1.1, yielding a dB of 0.414, tack on the -10dB reduction from Spectra and its -9.586dB, or 0.11mÃƒâ€šÃ‚Â² effective.  Given this RCS it can get within 108km of an E-2C 2000 NP undetected.  It can also get within 53km of an F/A-18E/F while detecting the super hornet at 104.8km.  Primarily armed with Magic missiles, while not overly capable, they are sufficient in most cases given its discreet nature.  Couple this with some support for AIM-120\'s, and you have the makings of a very mean, reasonably priced naval dominance fighter.http://rafalenews.blogspot.com/p/rafale-weapon-load-out.html'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Damocles LASER','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','OSF IRST','RBE2-AA','SPECTRA ECM','SPECTRA ELINT','SPECTRA RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1287.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=18.000000
    dbObj.mfFuelCapacity_kg=4577.000000
    dbObj.mfFuelRate_kgps=4.328000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Rafale M durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Rafale Pylon Wing tips','Rafale Pylon Wing tips','Rafale Pylon Mid Wing','Rafale Pylon Inner Wing','Rafale Pylon Fwd Nacelle','Rafale Pylon Aft Nacelle','Rafale Pylon Centerline','GIAT30-719B','SPECTRA CM','SPECTRA CM']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['RBE2-AA','RBE2-AA','RBE2-AA','RBE2-AA','RBE2-AA','RBE2-AA','RBE2-AA','','','']
    dbObj.launcherFireControl2=['Damocles LASER','Damocles LASER','Damocles LASER','Damocles LASER','Damocles LASER','Damocles LASER','Damocles LASER','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-9.586100
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.210000
    airDetectionDBObject.irSignature_dB=-5.000000
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
    dbObj.maxTakeoffWeight_kg=24500.000000
    dbObj.maxAltitude_m=16800.000000
    dbObj.climbRate_mps=255.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=450.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=30.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=100080.000000
    dbObj.militaryThrustSpeedSlope=0.000100
    dbObj.mfAfterburnThrust_N=151240.000000
    dbObj.abThrustSpeedSlope=0.000670
    dbObj.mfAfterburnFuelRate_kgps=13.770000
    dbObj.mfCdpsub=0.847000
    dbObj.mfCdptran=1.078000
    dbObj.mfCdpsup=0.900000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,0.800000,0.635000,0.450000,0.150000,0.020000,0.005000,0.001250]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,0.986100,1.060000,1.232600,1.848800,2.465100,4.930200,4.930200]
    dbObj.CalculateParams()
    return dbObj
