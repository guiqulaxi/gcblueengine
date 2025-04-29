# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Hamburg DDG 1975'
    dbObj.natoClass='Hamburg DDG 1975'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4680000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1976.089966
    dbObj.finalYear=1994.959961
    dbObj.country='Germany'
    dbObj.designation='DDG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=133.699997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DA-02','Decca 1226','Elac 1Bv Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','LW-02','M45 FCS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=35.000000
    dbObj.mfAccel_ktsps=0.053314
    dbObj.mfTurnRate_degps=1.998970
    dbObj.mfFuelCapacity_kg=655200.000000
    dbObj.mfFuelRate_kgps=0.963521
    dbObj.mfToughness=25.000000
    dbObj.damageEffect='Hamburg DDG 1975 durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['MM-38 Exocet Twin Launcher','MM-38 Exocet Twin Launcher','100mm/55 (3.9in) model 1964','100mm/55 (3.9in) model 1964','100mm/55 (3.9in) model 1964','40 mm 2xL70 Bofors','40 mm 2xL70 Bofors','Mk-32 2 Torpedo Mount','Mk-32 2 Torpedo Mount','40 mm 2xL70 Bofors','40 mm 2xL70 Bofors']
    dbObj.maMagazineClass=['100mm/55 model 1964 2400 Rounds','40mm/L70 Bofors Twin x4 Magazine','Hamburg Torpedo Racks']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,300.000000,300.000000,170.000000,170.000000,30.000000,30.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,0.000000,180.000000,90.000000,90.000000,90.000000,270.000000,270.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.598999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.989000
    airDetectionDBObject.irSignature_dB=21.691000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.200000
    dbObj.beam_m=13.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=72000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
