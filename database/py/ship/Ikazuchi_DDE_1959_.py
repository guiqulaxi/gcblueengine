# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Ikazuchi DDE(1959)'
    dbObj.natoClass='Ikazuchi DDE(1959)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1080000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1959.000000
    dbObj.finalYear=1976.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=88.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','OPS-2','OPS-3','OQS-3 Active','OQS-3 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.090653
    dbObj.mfTurnRate_degps=3.057936
    dbObj.mfFuelCapacity_kg=151200.000000
    dbObj.mfFuelRate_kgps=0.077777
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Ikazuchi DDE durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['3/50 Mark 34','3/50 Mark 34','40mm Bofors Mk12','Hedgehog','Kgun x2','Kgun x2']
    dbObj.maMagazineClass=['76mm mk33 Store','40mm Bofors x2 Magazine','Japanese ASW Magazine']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,310.000000,10.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,180.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=35.047001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=20.937000
    airDetectionDBObject.irSignature_dB=16.959000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.080000
    dbObj.beam_m=8.700000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=12000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
