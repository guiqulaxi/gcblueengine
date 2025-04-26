# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='BAL Class Ciudad Bolivar'
    dbObj.natoClass='BAL Class Ciudad Bolivar'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=9750000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1901.729980
    dbObj.finalYear=3000.000000
    dbObj.country='Venezuela'
    dbObj.designation='BAL'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes='Marcos. Need photo'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARPA-S','ARPA-X','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=18.600000
    dbObj.mfAccel_ktsps=0.023784
    dbObj.mfTurnRate_degps=1.132596
    dbObj.mfFuelCapacity_kg=1365000.000000
    dbObj.mfFuelRate_kgps=47.016262
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='BAL Class Ciudad Bolivar durability'
    dbObj.mnNumLaunchers=0
    dbObj.maLauncherClass=[]
    dbObj.maMagazineClass=['T-81 helo fuel']
    dbObj.magazineId=[0]
    dbObj.launcherId=[]
    dbObj.launcherName=[]
    dbObj.launcherFOV_deg=[]
    dbObj.launcherAz_deg=[]
    dbObj.launcherEl_deg=[]
    dbObj.launcherFireControl=[]
    dbObj.launcherFireControl2=[]
    dbObj.launcherIsReloadable=[]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=49.381001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.099001
    airDetectionDBObject.irSignature_dB=18.400999
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
    dbObj.draft_m=6.500000
    dbObj.beam_m=18.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=12500.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='FFG-7 Helo Deck'
    dbObj.CalculateParams()
    return dbObj
