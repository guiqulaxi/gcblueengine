# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='LST Class Capana'
    dbObj.natoClass='LST Class Capana'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4070000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.560059
    dbObj.finalYear=3000.000000
    dbObj.country='Venezuela'
    dbObj.designation='LST'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes='Marcos'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Raytheon']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=14.000000
    dbObj.mfAccel_ktsps=0.032014
    dbObj.mfTurnRate_degps=1.407654
    dbObj.mfFuelCapacity_kg=1343100.000000
    dbObj.mfFuelRate_kgps=0.139905
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='LST Class Capana durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['Launcher 40/70L-1']
    dbObj.maMagazineClass=['Capana fuel helo']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[360.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.689999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.624001
    airDetectionDBObject.irSignature_dB=21.650999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=14.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.000000
    dbObj.beam_m=15.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=12800.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='FFG-7 Helo Deck'
    dbObj.CalculateParams()
    return dbObj
