# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='S-2T Taiwan'
    dbObj.natoClass='S-2T Taiwan'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=8125000.000000
    dbObj.weight_kg=8310.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Taiwan'
    dbObj.designation='ASW'
    dbObj.imageList='s2g.jpg'
    dbObj.iconFileName='air/AdvicoS2T.JPG'
    dbObj.mz3DModelFileName='s-2g.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['AAS-36 FLIR','ALR-47 ESM','APS-504(V)5','ASQ-81 MAD','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=265.000000
    dbObj.mfAccel_ktsps=10.000000
    dbObj.mfTurnRate_degps=10.000000
    dbObj.mfFuelCapacity_kg=1400.000000
    dbObj.mfFuelRate_kgps=0.100000
    dbObj.mfToughness=4.000000
    dbObj.damageEffect='S-2T Taiwan durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['5 DICASS Launcher','5 LOFAR Launcher','14 DIFAR Launcher','S-2T Taiwan Torpedo Launcher']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['Buoy','Buoy','Buoy','Torp']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.140000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=11.970000
    airDetectionDBObject.irSignature_dB=30.000000
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
    dbObj.maxTakeoffWeight_kg=50000.000000
    dbObj.maxAltitude_m=6500.000000
    dbObj.climbRate_mps=15.000000
    dbObj.gmax=5.000000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=0.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.CalculateParams()
    return dbObj
