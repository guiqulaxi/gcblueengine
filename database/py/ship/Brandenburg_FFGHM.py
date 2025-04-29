# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Brandenburg FFGHM'
    dbObj.natoClass='Brandenburg FFGHM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1994.790039
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=138.850006
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DSQS-21BZ Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','LW-08','SMART-S','STIR 180']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.204064
    dbObj.mfTurnRate_degps=1.775078
    dbObj.mfFuelCapacity_kg=686000.000000
    dbObj.mfFuelRate_kgps=0.857493
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Brandenburg FFGHM durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['Mk-41 Mod4 VLS','RIM-116A RAM x21','RIM-116A RAM x21','Exocet Twin Launcher','Exocet Twin Launcher','76 mm/62 Mark 75','20mm Rh 202','20mm Rh 202','Mk-32 2 Torpedo Mount','Mk-32 2 Torpedo Mount']
    dbObj.maMagazineClass=['Lynx 2.2 Support','76mm/62 mk75 240 rounds','RIM-116 21 x2 Store','20mm Rh202 x2 Store','Mk-41 VLS Mod4 16 Cell']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[0,1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[330.000000,340.000000,340.000000,30.000000,30.000000,300.000000,170.000000,170.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,180.000000,90.000000,270.000000,0.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,20.000000,20.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['STIR 180','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.898998
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.853001
    airDetectionDBObject.irSignature_dB=26.743000
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
    dbObj.draft_m=6.300000
    dbObj.beam_m=16.700001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=61875.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
