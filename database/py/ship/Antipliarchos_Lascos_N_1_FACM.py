# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Antipliarchos Lascos N.1 FACM'
    dbObj.natoClass='Antipliarchos Lascos N.1 FACM'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=447000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.538940
    dbObj.finalYear=3000.000000
    dbObj.country='Greece'
    dbObj.designation='PGG'
    dbObj.imageList='boat.jpg'
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='pg-84.xml'
    dbObj.notes=''
    dbObj.length_m=56.650002
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','TRS 3030 Triton','Decca 1226','TRS 3220 Pollux','Panda IIR','Panda Optical','DR2000S']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=39.000000
    dbObj.mfAccel_ktsps=0.255317
    dbObj.mfTurnRate_degps=5.721591
    dbObj.mfFuelCapacity_kg=43540.000000
    dbObj.mfFuelRate_kgps=0.100786
    dbObj.mfToughness=25.000000
    dbObj.damageEffect='Antipliarchos Lascos N.1 FACM durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['Exocet Twin Launcher','Exocet Twin Launcher','76 mm/62 Mark 75 Compact','76 mm/62 Mark 75 Compact','30mm/75 Emerlec 30 KCB','30mm/75 Emerlec 30 KCB','533mm SST-4 Tube x1','533mm SST-4 Tube x1','Mk-34 RBOC x4 CM Launcher','Mk-34 RBOC x2 CM Launcher','Mk-34 RBOC x4 CM Launcher','Mk-34 RBOC x2 CM Launcher']
    dbObj.maMagazineClass=['30mm Emerlec x2 Store','76mm/62 mk75 x2 480 rounds','RBOC CM Mag 180']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,240.000000,240.000000,185.000000,185.000000,30.000000,30.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[30.000000,330.000000,0.000000,180.000000,90.000000,270.000000,90.000000,270.000000,90.000000,90.000000,270.000000,270.000000]
    dbObj.launcherEl_deg=[20.000000,20.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=26.937000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.646999
    airDetectionDBObject.irSignature_dB=17.395000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.700000
    dbObj.beam_m=8.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=18000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
