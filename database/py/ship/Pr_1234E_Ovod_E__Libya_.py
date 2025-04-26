# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1234E Ovod-E (Libya)'
    dbObj.natoClass='Nanuchka II (Libya)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=569000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.750000
    dbObj.finalYear=3000.000000
    dbObj.country='Libya'
    dbObj.designation='FSG'
    dbObj.imageList='nanuchka2.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Half Hat','MR-103 Bars','MR-331 Rangout','Pop Group FC']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=34.000000
    dbObj.mfAccel_ktsps=0.238494
    dbObj.mfTurnRate_degps=4.873325
    dbObj.mfFuelCapacity_kg=63900.000000
    dbObj.mfFuelRate_kgps=0.085199
    dbObj.mfToughness=50.000000
    dbObj.damageEffect='Pr 1234E Ovod-E (Libya) durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['SS-N-2C x2 Launcher','SS-N-2C x2 Launcher','SA-N-4 x2 Launcher','57 mm/75 (2.24in) AK-725 (ZIF-72) twin barrel']
    dbObj.maMagazineClass=['9K33 OSA Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[20.000000,20.000000,40.000000,0.000000]
    dbObj.launcherFireControl=['','','Pop Group FC','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=30.872000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=20.186001
    airDetectionDBObject.irSignature_dB=17.577000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=3.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.740000
    dbObj.beam_m=11.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=25800.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
