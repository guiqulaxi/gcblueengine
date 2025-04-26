# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV-62 (Forrestal) USS Independence(68)'
    dbObj.natoClass='CV-62 (Forrestal) USS Independence(68)'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=20000000.000000
    dbObj.weight_kg=75900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1968.328003
    dbObj.finalYear=1985.134033
    dbObj.country='USA'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPS-8A','SPS-10E','SPS-30','SPS-37']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.018004
    dbObj.mfTurnRate_degps=0.626541
    dbObj.mfFuelCapacity_kg=8570000.000000
    dbObj.mfFuelRate_kgps=3.967558
    dbObj.mfToughness=300.000000
    dbObj.damageEffect='CV-62 (Forrestal) USS Independence durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['127mm/54 (5in) Mk42','127mm/54 (5in) Mk42','127mm/54 (5in) Mk42','127mm/54 (5in) Mk42']
    dbObj.maMagazineClass=['Forrestal Fuel','Forrestal Magazine']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[160.000000,160.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[105.000000,255.000000,102.000000,258.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
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
