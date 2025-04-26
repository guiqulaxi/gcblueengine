# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Tourville'
    dbObj.natoClass='Tourville'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=20000000.000000
    dbObj.weight_kg=6100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1974.469971
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBR 16','DRBV 26','DRBV 51D','DSBV 61C','DUBV-23 Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPG-51D 16']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.039719
    dbObj.mfTurnRate_degps=1.692479
    dbObj.mfFuelCapacity_kg=854000.000000
    dbObj.mfFuelRate_kgps=0.948881
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Tourville durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['Crotale Naval','Exocet Tri Launcher','Exocet Tri Launcher','100mm/55 (3.9in) model 1968 CADAM','100mm/55 (3.9in) model 1968 CADAM','20 mm F2 Cannon','20 mm F2 Cannon','KD59E Torp Launcher','KD59E Torp Launcher']
    dbObj.maMagazineClass=['Lynx 2.2 Support','Crotale Naval 16','100mm/55 Model 1968 1200 Rounds','French Combat Stores']
    dbObj.magazineId=[1,0,2,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[330.000000,30.000000,30.000000,300.000000,300.000000,200.000000,200.000000,180.000000,180.000000]
    dbObj.launcherAz_deg=[180.000000,45.000000,315.000000,0.000000,0.000000,270.000000,90.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,12.000000,12.000000,0.000000,0.000000,30.000000,30.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=46.326000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.142000
    airDetectionDBObject.irSignature_dB=24.764000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.600000
    dbObj.beam_m=15.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=58000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
