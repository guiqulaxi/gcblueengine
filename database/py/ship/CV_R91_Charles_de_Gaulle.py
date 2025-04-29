# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV R91 Charles de Gaulle'
    dbObj.natoClass='CV R91 Charles de Gaulle'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=1000000000.000000
    dbObj.weight_kg=42000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2001.380005
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=261.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBB-33 ECM','ARBR 21','Arabel FC','DIBC 2A','DRBJ 11B AS','DRBV 15C','DRBV 26D','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','VAMPIR MB IIRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.034283
    dbObj.mfTurnRate_degps=0.714416
    dbObj.mfFuelCapacity_kg=5880000.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=1000.000000
    dbObj.damageEffect='CV R91 Charles de Gaulle durability'
    dbObj.mnNumLaunchers=16
    dbObj.maLauncherClass=['Sylver A43 VLS','Mistral Sadral','Mistral Sadral','20 mm F2 Cannon','20 mm F2 Cannon','20 mm F2 Cannon','20 mm F2 Cannon','20 mm F2 Cannon','20 mm F2 Cannon','20 mm F2 Cannon','20 mm F2 Cannon','Sagaie CM','Sagaie CM','Sagaie CM','Sagaie CM','SLAT CM']
    dbObj.maMagazineClass=['Charles de Gaulle CVN Fuel','Charles de Gaulle CVN Magazine','Mistral Sadral Mag x2','Sylver A43 VLS 32 Cell']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[0,1,2,3]
    dbObj.launcherId=[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    dbObj.launcherName=['','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,300.000000,300.000000,90.000000,90.000000,90.000000,90.000000,90.000000,90.000000,90.000000,90.000000,0.000000,0.000000,0.000000,0.000000,360.000000]
    dbObj.launcherAz_deg=[90.000000,90.000000,270.000000,0.000000,45.000000,90.000000,135.000000,180.000000,225.000000,270.000000,315.000000,90.000000,270.000000,0.000000,180.000000,90.000000]
    dbObj.launcherEl_deg=[90.000000,40.000000,40.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,45.000000,45.000000,45.000000,45.000000,0.000000]
    dbObj.launcherFireControl=['Arabel FC','','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=58.894001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=33.659000
    airDetectionDBObject.irSignature_dB=14.691000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.430000
    dbObj.beam_m=64.360001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=80460.000000
    dbObj.ExhaustStacks=0.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='De Gaulle Flight Deck'
    dbObj.CalculateParams()
    return dbObj
