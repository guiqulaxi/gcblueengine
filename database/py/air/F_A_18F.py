# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F/A-18F'
    dbObj.natoClass='F/A-18F'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=40000000.000000
    dbObj.weight_kg=11800.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1998.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='Fighter Multi'
    dbObj.imageList='fa18f.jpg'
    dbObj.iconFileName='air/AdvicoFA18F.jpg'
    dbObj.mz3DModelFileName='f-18E.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-214 ECM','ALR-67 RWR','AN/AAR-57 MAWS','APG-73','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Litening LDP']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1050.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=16.000000
    dbObj.mfFuelCapacity_kg=6145.000000
    dbObj.mfFuelRate_kgps=2.800000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F/A-18F durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['F/A-18 Centerline','F/A-18 Nacelle','F/A-18 Inboard','F/A-18 Central','F/A-18 Outboard','F/A-18 Wingtip','M61A Cannon','AN/ALE-47 CMD','AN/ALE-47 CMD']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APG-73','APG-73','APG-73','APG-73','APG-73','APG-73','APG-73','','']
    dbObj.launcherFireControl2=['Litening LDP','Litening LDP','Litening LDP','Litening LDP','Litening LDP','Litening LDP','Litening LDP','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=3.800000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.260000
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
    dbObj.maxTakeoffWeight_kg=29000.000000
    dbObj.maxAltitude_m=17000.000000
    dbObj.climbRate_mps=230.000000
    dbObj.gmax=9.000000
    dbObj.minimumRunway_m=1800.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=124600.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=195800.000000
    dbObj.abThrustSpeedSlope=0.001500
    dbObj.mfAfterburnFuelRate_kgps=5.000000
    dbObj.mfCdpsub=1.300000
    dbObj.mfCdptran=2.700000
    dbObj.mfCdpsup=2.250000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.cruiseSpeed_mps=100.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.800000,0.750000,0.730000,0.600000,0.200000,0.050000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.900000,0.850000,0.900000,1.050000,2.000000,3.000000,3.000000,3.000000]
    dbObj.CalculateParams()
    return dbObj
