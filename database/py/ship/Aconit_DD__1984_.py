# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Aconit DD (1984)'
    dbObj.natoClass='Aconit DD (1984)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=1996.000000
    dbObj.country='France'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=127.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DRBC 32B','DRBV 15C','DRBV 22','DUBV-23 Active','DUBV-43 VDS Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.120987
    dbObj.mfTurnRate_degps=1.889861
    dbObj.mfFuelCapacity_kg=546000.000000
    dbObj.mfFuelRate_kgps=0.454996
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Aconit DD durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['100mm/55 (3.9in) model 1968','100mm/55 (3.9in) model 1968','MM-38 Exocet Twin Launcher','MM-38 Exocet Twin Launcher','533mm French L Torp Tubes x5','533mm French L Torp Tubes x5']
    dbObj.maMagazineClass=['100mm/55 Model 1968 1200 Rounds','L Torpedo Racks 20 Rounds']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[320.000000,300.000000,0.000000,0.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,20.000000,20.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['DRBC 31D','DRBC 31D','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.411999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.677000
    airDetectionDBObject.irSignature_dB=21.641001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.800000
    dbObj.beam_m=13.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=28650.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
