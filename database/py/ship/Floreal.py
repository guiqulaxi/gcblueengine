# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Floreal'
    dbObj.natoClass='Floreal'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=500000000.000000
    dbObj.weight_kg=2950000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1992.400024
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBR 17','DRBV 21A','DUBA-25A Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=0.059652
    dbObj.mfTurnRate_degps=1.927193
    dbObj.mfFuelCapacity_kg=413000.000000
    dbObj.mfFuelRate_kgps=0.127468
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Floreal durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['Mistral Simbad','Mistral Simbad','20 mm F2 Cannon','20 mm F2 Cannon','Exocet Single Launcher','Exocet Single Launcher','100mm/55 (3.9in) model 1968 CADAM']
    dbObj.maMagazineClass=['AS 565 1.2 Support','100mm/55 Model 1968 600 rounds','Mistral Simbad Mag x2','French Combat Stores']
    dbObj.magazineId=[1,2,3,4]
    dbObj.launcherId=[1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[220.000000,220.000000,120.000000,120.000000,30.000000,30.000000,300.000000]
    dbObj.launcherAz_deg=[130.000000,230.000000,90.000000,90.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,30.000000,30.000000,12.000000,12.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.592999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.152000
    airDetectionDBObject.irSignature_dB=18.042000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.300000
    dbObj.beam_m=14.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=17640.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
