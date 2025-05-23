# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F-8E(FN)'
    dbObj.natoClass='F-8E(FN)'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=21000000.000000
    dbObj.weight_kg=8090.399902
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1964.786011
    dbObj.finalYear=2000.000000
    dbObj.country='France'
    dbObj.designation='Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoF8E.jpg'
    dbObj.mz3DModelFileName='f-5.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-51','APQ-104','APR-30 RWR','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1070.000000
    dbObj.mfAccel_ktsps=20.389999
    dbObj.mfTurnRate_degps=18.000000
    dbObj.mfFuelCapacity_kg=4096.600098
    dbObj.mfFuelRate_kgps=1.060000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F-8E durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['20mm Colt Mk-12 Cannon (125) x2','20mm Colt Mk-12 Cannon (125) x2','F8U FN chin','F8U FN chin','F8U FN wings','CM Ejector','CM Ejector']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.030000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.800000
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
    dbObj.maxTakeoffWeight_kg=15468.000000
    dbObj.maxAltitude_m=16000.000000
    dbObj.climbRate_mps=138.800003
    dbObj.gmax=8.000000
    dbObj.minimumRunway_m=1615.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=15.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=47600.000000
    dbObj.militaryThrustSpeedSlope=0.001000
    dbObj.mfAfterburnThrust_N=80100.000000
    dbObj.abThrustSpeedSlope=0.002175
    dbObj.mfAfterburnFuelRate_kgps=6.353300
    dbObj.mfCdpsub=0.800000
    dbObj.mfCdptran=1.200000
    dbObj.mfCdpsup=0.960000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.600000
    dbObj.cruiseSpeed_mps=127.070000
    dbObj.stallSpeed_mps=61.900002
    dbObj.thrustTable=[0.854000,0.728600,0.706000,0.690000,0.593500,0.435700,0.168800,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,0.906500,0.869500,0.935950,2.400000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
