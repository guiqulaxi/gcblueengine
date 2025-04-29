# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Hauk PTGM 1994'
    dbObj.natoClass='Hauk PTGM 1994'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=160000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1994.140015
    dbObj.finalYear=2001.000000
    dbObj.country='Norway'
    dbObj.designation='PTGM'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=36.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Decca 1226','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.209805
    dbObj.mfTurnRate_degps=8.147333
    dbObj.mfFuelCapacity_kg=33600.000000
    dbObj.mfFuelRate_kgps=0.213691
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Hauk PTGM durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['Penguin SSM Launcher x6','533mm Hauk tube','533mm Hauk tube','40mm L70 Sea Trinity','Mistral Simbad']
    dbObj.maMagazineClass=['40mm L70 Trinity magazine','Mistral Simbad Mag x1']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,300.000000,330.000000]
    dbObj.launcherAz_deg=[0.000000,20.000000,340.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[20.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=22.607000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.299000
    airDetectionDBObject.irSignature_dB=17.209999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.500000
    dbObj.beam_m=6.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=6820.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
