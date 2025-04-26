# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Hayabusa PGM'
    dbObj.natoClass='Hayabusa PGM'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=240000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2002.229004
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','FCS-2-21 1','OPS-18']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=46.000000
    dbObj.mfAccel_ktsps=1.237969
    dbObj.mfTurnRate_degps=7.883809
    dbObj.mfFuelCapacity_kg=33600.000000
    dbObj.mfFuelRate_kgps=0.337994
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Hayabusa PGM durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['SSM-1B Twin','SSM-1B Twin','76 mm/62 Mark 75 Compact']
    dbObj.maMagazineClass=['76mm/62 mk75 240 rounds']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000]
    dbObj.launcherAz_deg=[20.000000,340.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=25.249001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.908001
    airDetectionDBObject.irSignature_dB=19.309999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.200000
    dbObj.beam_m=8.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=16200.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.670000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
