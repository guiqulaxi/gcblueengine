# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Georges Leygues DDGHM(D640)(96)'
    dbObj.natoClass='Georges Leygues DDGHM(D640)(96)'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.449951
    dbObj.finalYear=2003.890015
    dbObj.country='France'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBR 17','DRBV 26','DRBV 51D','DUBV-23 Active','DUBV-43 VDS Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','VAMPIR MB IIRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.194825
    dbObj.mfTurnRate_degps=1.856905
    dbObj.mfFuelCapacity_kg=630000.000000
    dbObj.mfFuelRate_kgps=0.313155
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Georges Leygues DDGHM(D640)(79) durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Exocet Quad Launcher','Exocet Quad Launcher','Crotale Naval','Mistral Sadral','Mistral Sadral','100mm/55 (3.9in) model 1968 CADAM','20 mm F2 Cannon','20 mm F2 Cannon','KD59E Torp Launcher','KD59E Torp Launcher']
    dbObj.maMagazineClass=['Lynx 2.2 Support','Crotale Naval 26','100mm/55 Model 1968 600 rounds','Mistral Sadral Mag x2','French Combat Stores']
    dbObj.magazineId=[1,0,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[30.000000,30.000000,340.000000,180.000000,180.000000,330.000000,200.000000,200.000000,180.000000,180.000000]
    dbObj.launcherAz_deg=[45.000000,315.000000,180.000000,0.000000,270.000000,0.000000,270.000000,90.000000,180.000000,90.000000]
    dbObj.launcherEl_deg=[12.000000,12.000000,40.000000,40.000000,40.000000,0.000000,30.000000,30.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.344002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.169001
    airDetectionDBObject.irSignature_dB=23.714001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.700000
    dbObj.beam_m=14.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=62400.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
