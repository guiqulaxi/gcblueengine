# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='P-8 MPA'
    dbObj.natoClass='Poseidon'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=300000000.000000
    dbObj.weight_kg=46606.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2010.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='ASuW'
    dbObj.imageList='p8.jpg'
    dbObj.iconFileName='air/AdvicoP8A.JPG'
    dbObj.mz3DModelFileName='tu-95.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-218 ESM','AN/AAR-54 MAWS','APY-10']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=490.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=3.000000
    dbObj.mfFuelCapacity_kg=33087.000000
    dbObj.mfFuelRate_kgps=1.070000
    dbObj.mfToughness=10.000000
    dbObj.damageEffect='P-8 MPA durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Poseidon Internal Bay','Poseidon Wings','17 DICASS Launcher','17 LOFAR Launcher','50 DIFAR Launcher','AN/AAQ-24 Nemesis DIRCM','AN/ALE-47 CMD','AN/ALE-47 CMD']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APY-10','APY-10','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=30.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.270000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_H_LP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_H_LP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=85370.000000
    dbObj.maxAltitude_m=25000.000000
    dbObj.climbRate_mps=9.000000
    dbObj.gmax=4.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=31.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
