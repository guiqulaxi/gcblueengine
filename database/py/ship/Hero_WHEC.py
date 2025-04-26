# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Hero WHEC'
    dbObj.natoClass='Hero WHEC'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=3300000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=2999.000000
    dbObj.country='USA'
    dbObj.designation='wPG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPS-40B','SPS-73(V) SS','WLR-1C']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.182311
    dbObj.mfTurnRate_degps=2.122789
    dbObj.mfFuelCapacity_kg=462000.000000
    dbObj.mfFuelRate_kgps=0.253991
    dbObj.mfToughness=247.000000
    dbObj.damageEffect='Hero WHEC durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','25 mm MGS','25 mm MGS','76 mm/62 Mark 75 Compact']
    dbObj.maMagazineClass=['USCGS Helo Support','Hero Ammo Mag','Phalanx 1 x1 Store']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[270.000000,170.000000,170.000000,240.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=42.323002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.955000
    airDetectionDBObject.irSignature_dB=26.635000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.600000
    dbObj.beam_m=13.310000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=43000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=1.000000
    dbObj.FlashyPaintScheme=1.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
