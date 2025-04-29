# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='FF Class Mariscal Sucre (2001)'
    dbObj.natoClass='FF Class Mariscal Sucre (2001)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2520000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2001.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Venezuela'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes='Marcos'
    dbObj.length_m=113.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['21HS7-ACT','21HS7-PAS','ARPA M-25','DEO','EL/M 2238','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','INTRA','NS9003A-V2','NS9005AV-2','PRT-401','RAN-10S','RTN-10XPx2','RTN-20X-2']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=35.000000
    dbObj.mfAccel_ktsps=0.240615
    dbObj.mfTurnRate_degps=2.561490
    dbObj.mfFuelCapacity_kg=352800.000000
    dbObj.mfFuelRate_kgps=0.285088
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='FF Class Mariscal Sucre durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Otomat-Lupo','Albatros-Lupo','ILAS-3 Lupo','127 mm/54 (5in) Compact','Launcher 40/70L','Mk-137 Mod.1']
    dbObj.maMagazineClass=['Lupo helo fuel','127/54 Compact polvorin Lupo','LUPO CHAFF','Lupo torpedos']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,0.000000,360.000000,360.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','RTN-10XPx2','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=40.567001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.118000
    airDetectionDBObject.irSignature_dB=23.555000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.840000
    dbObj.beam_m=11.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=57800.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='FFG-7 Helo Deck'
    dbObj.CalculateParams()
    return dbObj
