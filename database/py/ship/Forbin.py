# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Forbin'
    dbObj.natoClass='Forbin'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=20000000.000000
    dbObj.weight_kg=6970000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2008.920044
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes='EW systems using ESM-3 and ARBB-33 ECM as stand-ins, missing data'
    dbObj.length_m=152.869995
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBB-33 ECM','EMPAR','ESM-3','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','S1850M','UMS 4110 Active','UMS 4110 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.187774
    dbObj.mfTurnRate_degps=1.540853
    dbObj.mfFuelCapacity_kg=975800.000000
    dbObj.mfFuelRate_kgps=0.696994
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Forbin durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['Sylver A50 VLS','Sylver A50 VLS','Exocet Quad Launcher','Exocet Quad Launcher','20 mm F2 Cannon','20 mm F2 Cannon','Mistral Sadral','Mistral Sadral','76 mm/62 Mark 75','76 mm/62 Mark 75','Eurotorp TLS launcher','Eurotorp TLS launcher']
    dbObj.maMagazineClass=['NH-90 1.2 Support','Sylver A50 VLS 48 Cell','Mistral Sadral Mag x2','76mm/62 mk75 240 rounds','French Combat Stores']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[1,0,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,30.000000,30.000000,200.000000,200.000000,300.000000,300.000000,270.000000,270.000000,180.000000,180.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,90.000000,270.000000,270.000000,90.000000,135.000000,225.000000,45.000000,315.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,90.000000,12.000000,12.000000,30.000000,30.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['EMPAR','EMPAR','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=37.194000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.122999
    airDetectionDBObject.irSignature_dB=16.694000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.600000
    dbObj.beam_m=20.299999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=74310.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
