# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1171 Tapir'
    dbObj.natoClass='Alligator'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4700000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1966.630005
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='LS'
    dbObj.imageList='tapir.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=113.099998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','ESM-1.5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=16.500000
    dbObj.mfAccel_ktsps=0.029359
    dbObj.mfTurnRate_degps=1.429105
    dbObj.mfFuelCapacity_kg=517000.000000
    dbObj.mfFuelRate_kgps=0.205157
    dbObj.mfToughness=69.000000
    dbObj.damageEffect='Pr 1171 Tapir durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['76 mm/59 (3in) AK-176','SA-N-5 x2 launcher x3']
    dbObj.maMagazineClass=['Strela2 x12 Mag']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[240.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.626999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.368000
    airDetectionDBObject.irSignature_dB=18.184000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=14.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S002.Merchant Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.500000
    dbObj.beam_m=15.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=9000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
