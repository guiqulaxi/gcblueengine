# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV-59 (Forrestal) USS Forrestal(SLEP)'
    dbObj.natoClass='CV-59 (Forrestal) USS Forrestal(SLEP)'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=20000000.000000
    dbObj.weight_kg=75900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.416016
    dbObj.finalYear=1993.692993
    dbObj.country='USA'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=300.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPS-10F','SPS-48C AS','SPS-49 AS','Mk-91 FCS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.018004
    dbObj.mfTurnRate_degps=0.626541
    dbObj.mfFuelCapacity_kg=8570000.000000
    dbObj.mfFuelRate_kgps=3.967558
    dbObj.mfToughness=300.000000
    dbObj.damageEffect='CV-59 (Forrestal) USS Forrestal durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','SeaSparrow x8 Launcher','SeaSparrow x8 Launcher','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0']
    dbObj.maMagazineClass=['Forrestal Fuel','Forrestal Magazine']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[160.000000,180.000000,180.000000,160.000000,210.000000,190.000000]
    dbObj.launcherAz_deg=[80.000000,100.000000,260.000000,280.000000,90.000000,255.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Mk-91 FCS','Mk-91 FCS','Mk-91 FCS','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=62.749001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=32.522999
    airDetectionDBObject.irSignature_dB=22.909000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=30.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=25.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=10.300000
    dbObj.beam_m=39.419998
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=260000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='ForrestalFlightDeck'
    dbObj.CalculateParams()
    return dbObj
