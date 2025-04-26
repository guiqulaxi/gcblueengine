# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='La Fayette'
    dbObj.natoClass='La Fayette'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=500000000.000000
    dbObj.weight_kg=3600000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1996.229980
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBR 21','DRBV 15C','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','VAMPIR IIRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.063242
    dbObj.mfTurnRate_degps=1.875118
    dbObj.mfFuelCapacity_kg=504000.000000
    dbObj.mfFuelRate_kgps=0.299997
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='La Fayette durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Crotale Naval','Exocet Quad Launcher','Exocet Quad Launcher','100mm/55 (3.9in) model 1968 CADAM','20 mm F2 Cannon','20 mm F2 Cannon']
    dbObj.maMagazineClass=['AS 565 1.1 Support','100mm/55 Model 1968 600 rounds','Crotale Naval 26','French Combat Stores']
    dbObj.magazineId=[1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[340.000000,30.000000,30.000000,300.000000,120.000000,120.000000]
    dbObj.launcherAz_deg=[180.000000,90.000000,270.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,12.000000,12.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=29.879999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.816999
    airDetectionDBObject.irSignature_dB=18.292000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.800000
    dbObj.beam_m=15.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=21000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
