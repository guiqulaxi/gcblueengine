# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Yamagumo DDK'
    dbObj.natoClass='Yamagumo DDK'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2700000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1966.078003
    dbObj.finalYear=2005.000000
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
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','NOLR-1B','OPS-11','OPS-17','OQS-3 Active','OQS-3 Passive','SQS-35(J) VDS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.075323
    dbObj.mfTurnRate_degps=2.191887
    dbObj.mfFuelCapacity_kg=378000.000000
    dbObj.mfFuelRate_kgps=0.207691
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Yamagumo DDK durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['3/50 Mark 27 Twin','3/50 Mark 27 Twin','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-112 ASROC','375mm Bofors ASRL']
    dbObj.maMagazineClass=['76mm mk33 Store','Japanese ASW Magazine','Japanese Ship Torpedo Racks']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[330.000000,330.000000,30.000000,30.000000,300.000000,300.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,90.000000,270.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.015999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.344999
    airDetectionDBObject.irSignature_dB=18.701000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.950000
    dbObj.beam_m=11.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=26000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
