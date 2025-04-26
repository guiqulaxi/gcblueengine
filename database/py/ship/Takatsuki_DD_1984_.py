# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Takatsuki DD(1984)'
    dbObj.natoClass='Takatsuki DD(1984)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.201050
    dbObj.finalYear=2003.848022
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
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','FCS-2-21 1','NOLR-6','OLT-3','OPS-11','OPS-17','OQR-1 TA','SQS-23 Active','SQS-23 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.041514
    dbObj.mfTurnRate_degps=1.928293
    dbObj.mfFuelCapacity_kg=630000.000000
    dbObj.mfFuelRate_kgps=0.499996
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Takatsuki DD durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','SeaSparrow x8 Launcher','5/54 Mark 16']
    dbObj.maMagazineClass=['127mm mk12/16 300 round','Sea Sparrow Reloads']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,330.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,0.000000]
    dbObj.launcherFireControl=['','','FCS-2-21 1','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.344002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.614000
    airDetectionDBObject.irSignature_dB=20.604000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.400000
    dbObj.beam_m=13.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
