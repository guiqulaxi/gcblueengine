# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CVN-69 (Nimitz) USS Dwight D. Eisenhower(RCOH)'
    dbObj.natoClass='CVN-69 (Nimitz) USS Dwight D. Eisenhower(RCOH)'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=91487000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2004.250000
    dbObj.finalYear=2999.989990
    dbObj.country='USA'
    dbObj.designation='CVN'
    dbObj.imageList='nimitz.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='nimitz.xml'
    dbObj.notes=''
    dbObj.length_m=317.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)4 ECM','SLQ-32(v)4 ESM B.1','SLQ-32(v)4 ESM B.2','SLQ-32(v)4 ESM B.3','SPS-48(E) AS','SPS-49(v)5','SPS-67(V)3 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.045625
    dbObj.mfTurnRate_degps=0.580666
    dbObj.mfFuelCapacity_kg=12808180.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=1000.000000
    dbObj.damageEffect='CVN-69 (Nimitz) USS Dwight D. Eisenhower durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','SeaSparrow x8 Launcher','RIM-116A RAM x21','RIM-116A RAM x21']
    dbObj.maMagazineClass=['Nimitz Fuel','Nimitz Magazine']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[180.000000,180.000000,300.000000,300.000000]
    dbObj.launcherAz_deg=[80.000000,260.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,40.000000]
    dbObj.launcherFireControl=['SPS-48(E) AS','SPS-48(E) AS','SPS-48(E) AS','SPS-48(E) AS']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=63.966000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=32.967999
    airDetectionDBObject.irSignature_dB=15.501000
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
    dbObj.draft_m=11.300000
    dbObj.beam_m=40.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=260000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Nimitz Flight Deck'
    dbObj.CalculateParams()
    return dbObj
