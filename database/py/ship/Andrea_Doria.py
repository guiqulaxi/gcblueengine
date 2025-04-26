# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Andrea Doria'
    dbObj.natoClass='Andrea Doria'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=7050000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2007.969971
    dbObj.finalYear=2999.000000
    dbObj.country='Italy'
    dbObj.designation='DD'
    dbObj.imageList='horizon.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-45.xml'
    dbObj.notes='EW systems using ESM-3 and ARBB-33 ECM as stand-ins, missing data'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBB-33 ECM','EMPAR','ESM-3','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','S1850M','UMS 4110 Active','UMS 4110 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.175415
    dbObj.mfTurnRate_degps=1.534927
    dbObj.mfFuelCapacity_kg=987000.000000
    dbObj.mfFuelRate_kgps=0.704994
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Andrea Doria durability'
    dbObj.mnNumLaunchers=14
    dbObj.maLauncherClass=['Otomat Launcher x8','Sylver A50 VLS','Sylver A50 VLS','Sylver A50 VLS','Otobreda 76/62 Super Rapid','Otobreda 76/62 Super Rapid','Otobreda 76/62 Super Rapid','20 mm F2 Cannon','20 mm F2 Cannon','324 mm Horizon Tube x 2','324 mm Horizon Tube x 2','SLAT CM','SCLAR Rocket Launcher','SCLAR Rocket Launcher']
    dbObj.maMagazineClass=['Fuel depot','Ship stores','Ship stores','Sylver A50 VLS 48 Cell']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    dbObj.launcherName=['','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,0.000000,0.000000,0.000000,240.000000,240.000000,180.000000,200.000000,200.000000,40.000000,40.000000,0.000000,180.000000,180.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,270.000000,90.000000,90.000000,270.000000,45.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[30.000000,60.000000,60.000000,60.000000,30.000000,30.000000,30.000000,30.000000,30.000000,0.000000,0.000000,0.000000,30.000000,30.000000]
    dbObj.launcherFireControl=['','EMPAR','EMPAR','EMPAR','EMPAR','EMPAR','EMPAR','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,False,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=37.268002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.124001
    airDetectionDBObject.irSignature_dB=16.697001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.600000
    dbObj.beam_m=20.299999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=66570.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
