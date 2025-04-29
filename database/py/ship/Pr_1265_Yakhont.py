# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1265 Yakhont'
    dbObj.natoClass='Sonya'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=450000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='MS'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=49.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','ESM-1.5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Generic Mine Hunting Sonar']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=14.000000
    dbObj.mfAccel_ktsps=0.054189
    dbObj.mfTurnRate_degps=3.546755
    dbObj.mfFuelCapacity_kg=63000.000000
    dbObj.mfFuelRate_kgps=0.116666
    dbObj.mfToughness=34.000000
    dbObj.damageEffect='Pr 1265 Yakhont durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','SA-N-5 x4 launcher x2']
    dbObj.maMagazineClass=['AK-630 x2 Store','Strela2 x16 Mag']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=29.344000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.250000
    airDetectionDBObject.irSignature_dB=17.499001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S001.Merchant Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.450000
    dbObj.beam_m=8.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=2200.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
