# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV R12 Hermes'
    dbObj.natoClass='CV R12 Hermes'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=20000000.000000
    dbObj.weight_kg=28700000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1959.900024
    dbObj.finalYear=1964.150024
    dbObj.country='UK'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=236.139999
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 974','Type 982','Type 984']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.015232
    dbObj.mfTurnRate_degps=0.847318
    dbObj.mfFuelCapacity_kg=3157000.000000
    dbObj.mfFuelRate_kgps=2.254981
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='CV R12 Hermes durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['40mm/56.3 QF Mk5 x2','40mm/56.3 QF Mk5 x2','40mm/56.3 QF Mk5 x2','40mm/56.3 QF Mk5 x2','40mm/56.3 QF Mk5 x2']
    dbObj.maMagazineClass=['Carrier Fuel Supply','Hermes Carrier Magazine','40mm Bofors x2 Magazine x5']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[260.000000,260.000000,260.000000,170.000000,260.000000]
    dbObj.launcherAz_deg=[315.000000,225.000000,45.000000,90.000000,135.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=56.414001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=31.822001
    airDetectionDBObject.irSignature_dB=22.208000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=17.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=25.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S10.Carrier Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.500000
    dbObj.beam_m=45.099998
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=76000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='HermesFlightDeck'
    dbObj.CalculateParams()
    return dbObj
