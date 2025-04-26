# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV-67 (JFK) USS John F Kennedy'
    dbObj.natoClass='CV-67 (JFK) USS John F Kennedy'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=81430000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1968.680054
    dbObj.finalYear=2007.579956
    dbObj.country='USA'
    dbObj.designation='CVN'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)4 ECM','SLQ-32(v)4 ESM B.1','SLQ-32(v)4 ESM B.2','SLQ-32(v)4 ESM B.3','SPS-48(E) AS','SPS-49 AS','SPS-67(V)3 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.018522
    dbObj.mfTurnRate_degps=0.602680
    dbObj.mfFuelCapacity_kg=11400200.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=1480.000000
    dbObj.damageEffect='CV-67 (JFK) USS John F Kennedy durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','RIM-116A RAM x21','RIM-116A RAM x21','SeaSparrow x8 Launcher','SeaSparrow x8 Launcher']
    dbObj.maMagazineClass=['Carrier Fuel Supply','Carrier Magazine']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,180.000000,180.000000,270.000000,270.000000]
    dbObj.launcherAz_deg=[135.000000,225.000000,80.000000,280.000000,135.000000,225.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,40.000000,40.000000,40.000000,40.000000]
    dbObj.launcherFireControl=['','','','','SPS-48(E) AS','SPS-48(E) AS']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=63.207001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=32.658001
    airDetectionDBObject.irSignature_dB=16.693001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=30.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S12.Carrier Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=11.200000
    dbObj.beam_m=40.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=280000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='John F Kennedy Flight Deck'
    dbObj.CalculateParams()
    return dbObj
