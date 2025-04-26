# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Joao Coutinho FSH'
    dbObj.natoClass='Joao Coutinho FSH'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1380000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.178955
    dbObj.finalYear=1989.000000
    dbObj.country='Portugal'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Decca TM 626','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MLA-1','QCU-2','SPG-34']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=24.400000
    dbObj.mfAccel_ktsps=0.075644
    dbObj.mfTurnRate_degps=2.842285
    dbObj.mfFuelCapacity_kg=193200.000000
    dbObj.mfFuelRate_kgps=0.114797
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Joao Coutinho FSH durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['3/50 Mark 33','40 mm 2xL70 Bofors','DC Rack 12','Kgun','Kgun']
    dbObj.maMagazineClass=['40mm/70 x2 Magazine','76mm mk33 Store','Coutinho DC Racks']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[320.000000,300.000000,10.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,180.000000,135.000000,225.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,11.250000,45.000000,45.000000]
    dbObj.launcherFireControl=['SPG-34','SPG-34','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=36.644001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=21.325001
    airDetectionDBObject.irSignature_dB=17.820999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.600000
    dbObj.beam_m=10.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=10560.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
