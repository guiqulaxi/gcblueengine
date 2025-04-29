# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='SSN 637 Sturgeon'
    dbObj.natoClass='SSN 637 Sturgeon'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=4246000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1966.928833
    dbObj.finalYear=2004.797363
    dbObj.country='USA'
    dbObj.designation='SSN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['BPS-14 SS','BQQ-2 Active','BQQ-2 Bow Passive','BQQ-2 Port Flank Passive','BQQ-2 Stbd Flank Passive','Periscope-1','TB-16 TA','WLR-4 ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,270.000000,90.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=26.000000
    dbObj.mfAccel_ktsps=1.250000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='SSN 637 Sturgeon durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm 688 Tube','533mm 688 Tube','533mm 688 Tube','533mm 688 Tube','CSA Mk1','CSA Mk1']
    dbObj.maMagazineClass=['688 magazine']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','CM','CM']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.300000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.300000
    airDetectionDBObject.irSignature_dB=8.300000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=13.260000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='AN165'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.800000
    dbObj.surfaceSpeed_kts=14.000000
    dbObj.mfMaxDepth_m=375.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=16.000000
    dbObj.CalculateParams()
    return dbObj
