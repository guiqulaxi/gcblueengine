# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 12321 Dzheyran'
    dbObj.natoClass='Aist'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=298000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1974.530029
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='LCJ'
    dbObj.imageList='aist.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Kivach SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=49.000000
    dbObj.mfAccel_ktsps=0.726299
    dbObj.mfTurnRate_degps=7.754910
    dbObj.mfFuelCapacity_kg=41720.000000
    dbObj.mfFuelRate_kgps=1.577363
    dbObj.mfToughness=9.000000
    dbObj.damageEffect='Pr 12321 Dzheyran durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M Twin Barrel','30 mm/54 (1.2in) AK-630M Twin Barrel']
    dbObj.maMagazineClass=['AK-630 Twin x2 Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[270.000000,270.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=26.659000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=20.174999
    airDetectionDBObject.irSignature_dB=25.982000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S13.HoverCraft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.600000
    dbObj.beam_m=17.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=32000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
