# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Baleares FFG (1991)'
    dbObj.natoClass='Baleares FFG (1991)'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4177000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.000000
    dbObj.finalYear=2009.500000
    dbObj.country='Spain'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes=''
    dbObj.length_m=134.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPG-51D 1','SPS-10F','SPS-52C AS','SQS-35 VDS Active','SQS-56 Active','SQS-56 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.036687
    dbObj.mfTurnRate_degps=1.855959
    dbObj.mfFuelCapacity_kg=584780.000000
    dbObj.mfFuelRate_kgps=0.561512
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Baleares FFG durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['127mm/54 (5in) Mk42','Mk-22 GMLS','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','20mm Meroka CIWS','20mm Meroka CIWS','Mk-32 2 Torpedo Mount','Mk-32 2 Torpedo Mount']
    dbObj.maMagazineClass=['Meroka x2 Store','Mk-22 GMLS Rotary Store','127mm Mk-42 500 Rounds','Mk-32 Torpedo Racks','Mk-37 Torpedo Racks']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[1,0,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,300.000000,0.000000,0.000000,170.000000,170.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,90.000000,270.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,40.000000,20.000000,20.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','SPG-51D 1','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.859001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.480000
    airDetectionDBObject.irSignature_dB=21.662001
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
    dbObj.draft_m=7.540000
    dbObj.beam_m=14.250000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=35000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
