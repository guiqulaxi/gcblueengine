# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 206 (Germany, East)'
    dbObj.natoClass='Pr 206 (Germany, East)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=161000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1968.800049
    dbObj.finalYear=1990.199951
    dbObj.country='Germany, East'
    dbObj.designation='PTB'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Reya']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=46.000000
    dbObj.mfAccel_ktsps=0.381481
    dbObj.mfTurnRate_degps=9.912308
    dbObj.mfFuelCapacity_kg=22540.000000
    dbObj.mfFuelRate_kgps=0.234800
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Pr 206 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['30 mm/63 (1.2in) AK-230','30 mm/63 (1.2in) AK-230','533mm OTA-53-206 Torpedo Tube','533mm OTA-53-206 Torpedo Tube','533mm OTA-53-206 Torpedo Tube','533mm OTA-53-206 Torpedo Tube']
    dbObj.maMagazineClass=['AK-230 x2 Store']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['0','0','0','0','0','0']
    dbObj.launcherFOV_deg=[270.000000,270.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=22.648001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.462000
    airDetectionDBObject.irSignature_dB=16.409000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.513000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.720000
    dbObj.beam_m=6.770000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=15000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
