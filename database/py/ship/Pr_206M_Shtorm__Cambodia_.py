# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 206M Shtorm (Cambodia)'
    dbObj.natoClass='Turya'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=250000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=1998.000000
    dbObj.country='Cambodia'
    dbObj.designation='PTB'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=39.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Reya','MG-329 Shelon VDS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=44.000000
    dbObj.mfAccel_ktsps=0.261514
    dbObj.mfTurnRate_degps=8.072054
    dbObj.mfFuelCapacity_kg=35000.000000
    dbObj.mfFuelRate_kgps=0.293105
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Pr 206m durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['57 mm/75 (2.24in) AK-725 (ZIF-72) twin barrel','25mm 2M-3M Twin','533mm OTA-53-206 Torpedo Tube','533mm OTA-53-206 Torpedo Tube','533mm OTA-53-206 Torpedo Tube','533mm OTA-53-206 Torpedo Tube','BB1 DCx10']
    dbObj.maMagazineClass=['AK-725 0.3x Store','2M3 Magazine']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,0.000000,0.000000,0.000000,0.000000,30.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=25.514999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=16.438000
    airDetectionDBObject.irSignature_dB=16.533001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.070000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.640000
    dbObj.beam_m=7.600000
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
