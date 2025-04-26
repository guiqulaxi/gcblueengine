# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Gun Test Boat'
    dbObj.natoClass='Gun Test Boat'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=20000000.000000
    dbObj.weight_kg=500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.099976
    dbObj.finalYear=3000.000000
    dbObj.country='TEST'
    dbObj.designation='TEST'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='pg-84.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Generic radar','Test ECM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=50.000000
    dbObj.mfAccel_ktsps=0.459586
    dbObj.mfTurnRate_degps=5.256105
    dbObj.mfFuelCapacity_kg=70000.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=25.000000
    dbObj.damageEffect='Ship1'
    dbObj.mnNumLaunchers=16
    dbObj.maLauncherClass=['ASROC-TEST Launcher','SAM Launcher','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun','Test Gun II']
    dbObj.maMagazineClass=['Magazine Slow','Magazine Fast']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    dbObj.launcherName=['','','','','','','','','','','11th launcher','12th launcher','13th launcher','14th launcher','15th launcher','16th launcher']
    dbObj.launcherFOV_deg=[0.000000,360.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,45.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Generic radar','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=30.030001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.118999
    airDetectionDBObject.irSignature_dB=12.252000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.000000
    dbObj.beam_m=18.900000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=48400.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
