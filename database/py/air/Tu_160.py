# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Tu-160'
    dbObj.natoClass='Tu-160'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=200000000.000000
    dbObj.weight_kg=110000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1987.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='Bomber'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoTU160.jpg'
    dbObj.mz3DModelFileName='tu-22.xml'
    dbObj.notes='Contributed by greengills'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Baikal ECM','Baikal ESM','Laser-30km','Obzor K']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1200.000000
    dbObj.mfAccel_ktsps=20.000000
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=117000.000000
    dbObj.mfFuelRate_kgps=9.500000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='Tu-160 durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['MKU-6-5U Rotary Launcher','MKU-6-5U Rotary Launcher','APP-15 CMD (Left Bank)','APP-15 CMD (Right Bank)']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Obzor K','Obzor K','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.710000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_HP_4_M0.85'
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
    dbObj.maxTakeoffWeight_kg=275000.000000
    dbObj.maxAltitude_m=16000.000000
    dbObj.climbRate_mps=70.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=40.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=548000.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=980000.000000
    dbObj.abThrustSpeedSlope=0.001000
    dbObj.mfAfterburnFuelRate_kgps=13.210000
    dbObj.mfCdpsub=4.000000
    dbObj.mfCdptran=8.000000
    dbObj.mfCdpsup=7.000000
    dbObj.mfMcm=1.150000
    dbObj.mfMsupm=1.250000
    dbObj.cruiseSpeed_mps=125.000000
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.900000,0.900000,0.800000,0.750000,0.550000,0.100000,0.050000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,0.950000,0.950000,1.000000,1.050000,1.200000,1.900000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
