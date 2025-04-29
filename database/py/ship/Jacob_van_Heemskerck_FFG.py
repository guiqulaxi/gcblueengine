# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Jacob van Heemskerck FFG'
    dbObj.natoClass='Jacob van Heemskerck FFG'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3048140.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.040039
    dbObj.finalYear=2006.959961
    dbObj.country='Netherlands'
    dbObj.designation='FFG'
    dbObj.imageList='heemskerck.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes='Two ships were built by Royal Schelde dockyard. The ships were named after Admirals as is usual practice in the Royal Netherlands Navy.Both ships were sold to Chile in 2005.'
    dbObj.length_m=130.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DA-08','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','LW-08','SQS-505 Active','SQS-505 Passive','STIR 180','WM-25','ZW-06']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.270650
    dbObj.mfTurnRate_degps=2.150058
    dbObj.mfFuelCapacity_kg=426739.593750
    dbObj.mfFuelRate_kgps=0.403533
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Jacob van Heemskerck FFG durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','Mk-13 Mod4 GMLS','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','30mm/77 GAU-8/A Goalkeeper','Mk-32 2 Torpedo Mount','Mk-32 2 Torpedo Mount']
    dbObj.maMagazineClass=['Goalkeeper x1 Store','Mk-13 Mod4 Rotary Store 40','Sea Sparrow Reloads','Mk-32 Torpedo Racks']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,330.000000,0.000000,0.000000,330.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,90.000000,270.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,20.000000,20.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['STIR 180','STIR 180','','','','','']
    dbObj.launcherFireControl2=['WM-25','WM-25','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.806000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.066000
    airDetectionDBObject.irSignature_dB=23.608000
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
    dbObj.draft_m=6.000000
    dbObj.beam_m=14.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=61200.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
