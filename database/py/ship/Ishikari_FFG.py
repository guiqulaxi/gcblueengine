# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Ishikari FFG'
    dbObj.natoClass='Ishikari FFG'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1450000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.237061
    dbObj.finalYear=2007.792969
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=85.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','FCS-2-21 1','OPS-28','SQS-36 Active','SQS-36 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.244791
    dbObj.mfTurnRate_degps=2.796059
    dbObj.mfFuelCapacity_kg=203000.000000
    dbObj.mfFuelRate_kgps=0.171695
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Ishikari FFG durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','76 mm/62 Mark 75','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','375mm Bofors ASRL']
    dbObj.maMagazineClass=['Japanese ASW Magazine','76mm/62 mk75 240 rounds','Japanese Ship Torpedo Racks']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,320.000000,30.000000,30.000000,300.000000]
    dbObj.launcherAz_deg=[30.000000,330.000000,0.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=36.966000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=21.683001
    airDetectionDBObject.irSignature_dB=19.804001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.600000
    dbObj.beam_m=10.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=24700.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
