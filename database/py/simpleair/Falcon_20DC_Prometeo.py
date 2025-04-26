# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Falcon-20DC Prometeo'
    dbObj.natoClass='Falcon-20DC Prometeo'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=7530.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Venezuela'
    dbObj.designation='EW'
    dbObj.imageList='falcon20d.jpg'
    dbObj.iconFileName='air/AdvicoFalcon20DC.jpg'
    dbObj.mz3DModelFileName='tu-16.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ELINT Prometeo','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=465.000000
    dbObj.mfAccel_ktsps=6.000000
    dbObj.mfTurnRate_degps=9.000000
    dbObj.mfFuelCapacity_kg=3646.000000
    dbObj.mfFuelRate_kgps=0.240000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Falcon-20DC Prometeo durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['AN/ALE-40 C','AN/ALE-40 F']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=7.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=8.130000
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
    dbObj.maxTakeoffWeight_kg=13000.000000
    dbObj.maxAltitude_m=12800.000000
    dbObj.climbRate_mps=9.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=25200.000000
    dbObj.maintenanceMax_s=25200.000000
    dbObj.CalculateParams()
    return dbObj
