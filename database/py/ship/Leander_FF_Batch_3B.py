# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Leander FF Batch 3B'
    dbObj.natoClass='Leander FF Batch 3B'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=3300000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1969.790039
    dbObj.finalYear=2006.819946
    dbObj.country='UK'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='lea.xml'
    dbObj.notes='I do not know the upgrade path for the ships int he leander batch 3 line, their name entries are thus empty.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 1006','Type 2016 Active','Type 2016 Passive','Type 967/968']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.500000
    dbObj.mfAccel_ktsps=0.031734
    dbObj.mfTurnRate_degps=2.074414
    dbObj.mfFuelCapacity_kg=462000.000000
    dbObj.mfFuelRate_kgps=0.481246
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Leander FF Batch 3 durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['114mm/43(4.5in) Mark 6','Sea Wolf 6pack','Exocet Quad Launcher','20 mm Mark 16','20 mm Mark 16','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Lynx 1.2 Support','Sea Wolf Store 20','Leander Ammo Mag']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,300.000000,60.000000,300.000000,300.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,270.000000,30.000000,330.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,40.000000,12.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Type 967/968','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=42.323002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.797001
    airDetectionDBObject.irSignature_dB=24.596001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.500000
    dbObj.beam_m=13.100000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=22370.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
