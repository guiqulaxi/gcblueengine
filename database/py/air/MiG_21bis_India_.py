# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='MiG-21bis(India)'
    dbObj.natoClass='Fishbed-N'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=1800000.000000
    dbObj.weight_kg=5895.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.000000
    dbObj.finalYear=2999.000000
    dbObj.country='India'
    dbObj.designation='Bomber'
    dbObj.imageList='mig21.jpg'
    dbObj.iconFileName='air/AdvicoMiG21bis.jpg'
    dbObj.mz3DModelFileName='mig21.xml'
    dbObj.notes='cross sections not configured yet.  Service ceilings may be slightly off.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','RP-22M Sapfir','Sirena-3M RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1350.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=19.000000
    dbObj.mfFuelCapacity_kg=2312.100098
    dbObj.mfFuelRate_kgps=1.350000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='MiG-21bis durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['MiG-21bis OuterPylon','MiG-21SM InnerPylon','23mm GSh-23L','MiG-21S Fuselage','MiG-21SM InnerPylon','MiG-21bis OuterPylon']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,20.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['RP-22M Sapfir','RP-22M Sapfir','','','RP-22M Sapfir','RP-22M Sapfir']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.620000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.260000
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
    dbObj.maxTakeoffWeight_kg=10100.000000
    dbObj.maxAltitude_m=17800.000000
    dbObj.climbRate_mps=240.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=40200.000000
    dbObj.militaryThrustSpeedSlope=-0.000800
    dbObj.mfAfterburnThrust_N=69600.000000
    dbObj.abThrustSpeedSlope=0.000790
    dbObj.mfAfterburnFuelRate_kgps=3.200000
    dbObj.mfCdpsub=0.400000
    dbObj.mfCdptran=0.800000
    dbObj.mfCdpsup=0.600000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,1.000000,1.000000,1.000000,0.925000,0.800000,0.400000,0.100000,0.050000,0.000000]
    dbObj.fuelEfficiencyTable=[0.950000,0.925000,0.900000,0.875000,0.830000,0.960000,1.800000,2.200000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
