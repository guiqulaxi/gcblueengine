# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Braunschweig'
    dbObj.natoClass='Braunschweig'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1662000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2008.290039
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=89.120003
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','TRS 3D/16 AS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=26.000000
    dbObj.mfAccel_ktsps=0.113877
    dbObj.mfTurnRate_degps=2.692586
    dbObj.mfFuelCapacity_kg=232680.000000
    dbObj.mfFuelRate_kgps=0.242373
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Braunschweig durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['76 mm/62 Mark 75','RIM-116A RAM x21','RIM-116A RAM x21','RBS-15 Twin Launcher','RBS-15 Twin Launcher','27mm MLG 27','27mm MLG 27']
    dbObj.maMagazineClass=['27mm MLG 27 x2 Store','76mm/62 mk75 240 rounds','RIM-116 21 x2 Store']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[3,2,1]
    dbObj.launcherId=[0,2,3,4,5,7,8]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,320.000000,340.000000,60.000000,60.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,40.000000,40.000000,20.000000,20.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=37.855000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.910000
    airDetectionDBObject.irSignature_dB=17.884001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
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
    dbObj.beam_m=13.280000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=19850.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
