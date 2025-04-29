# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Kawasaki C-1'
    dbObj.natoClass='Kawasaki C-1'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=4704065.000000
    dbObj.weight_kg=23320.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1974.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation='Cargo'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoC1.jpg'
    dbObj.mz3DModelFileName='c-130.xml'
    dbObj.notes='[phoenixegmh]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALR-2002 RWR','AN/AAR-54 MAWS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=436.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=15.000000
    dbObj.mfFuelCapacity_kg=15000.000000
    dbObj.mfFuelRate_kgps=0.100000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Kawasaki C-1 durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['AN/ALE-47 CMD','AN/ALE-47 CMD','AN/AAQ-24 Nemesis DIRCM']
    dbObj.maMagazineClass=['Kawasaki C-1 Cargo Bay']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['CM1','CM2','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=15.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.100000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_TP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_TP_4_M0.85'
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
    dbObj.maxTakeoffWeight_kg=38700.000000
    dbObj.maxAltitude_m=11600.000000
    dbObj.climbRate_mps=17.799999
    dbObj.gmax=2.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=30.000000
    dbObj.maintenanceMin_s=10000.000000
    dbObj.maintenanceMax_s=10000.000000
    dbObj.CalculateParams()
    return dbObj
