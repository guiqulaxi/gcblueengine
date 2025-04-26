# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 45 DDG'
    dbObj.natoClass='Type 45 DDG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=6460000256.000000
    dbObj.weight_kg=8000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2009.560059
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-82.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['EOSS 2500 IIRST','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','S1850M','Sabre ECM','Sabre ESM B.1','Sabre ESM B.2','Sampson','Type 2091 Active','Type 2091 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=0.211451
    dbObj.mfTurnRate_degps=1.522737
    dbObj.mfFuelCapacity_kg=1120000.000000
    dbObj.mfFuelRate_kgps=0.799993
    dbObj.mfToughness=250.000000
    dbObj.damageEffect='Type 45 DDG durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['Sylver A50 VLS','Sylver A50 VLS','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','114mm/55(4.5in) Mark 8 Mod 1']
    dbObj.maMagazineClass=['Lynx 2.2 Support','114mm/55(4.5in) mk8 800 rounds','Phalanx 1 x2 Store','Sylver A50 VLS 48 Cell']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,170.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,90.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Sampson','Sampson','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=35.082001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.216999
    airDetectionDBObject.irSignature_dB=15.601000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.400000
    dbObj.beam_m=21.200001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=117000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
