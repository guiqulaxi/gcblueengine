# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 10750 Sapfir'
    dbObj.natoClass='Lida'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=135000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1989.949951
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='MH'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Generic Mine Hunting Sonar','Pechora SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=12.000000
    dbObj.mfAccel_ktsps=0.091308
    dbObj.mfTurnRate_degps=5.478001
    dbObj.mfFuelCapacity_kg=18900.000000
    dbObj.mfFuelRate_kgps=0.065624
    dbObj.mfToughness=10.400000
    dbObj.damageEffect='Pr 10750 Sapfir durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M']
    dbObj.maMagazineClass=['AK-630 x1 Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[270.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=21.500999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=14.867000
    airDetectionDBObject.irSignature_dB=17.162001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S001.Merchant Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.530000
    dbObj.beam_m=6.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=900.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
