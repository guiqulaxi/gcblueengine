# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Famous Cutter WMEC'
    dbObj.natoClass='Famous Cutter WMEC'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1820000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.089966
    dbObj.finalYear=2999.989990
    dbObj.country='USA'
    dbObj.designation='wPG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=82.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1.5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPS-73(V) SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=19.500000
    dbObj.mfAccel_ktsps=0.061339
    dbObj.mfTurnRate_degps=2.309903
    dbObj.mfFuelCapacity_kg=254800.000000
    dbObj.mfFuelRate_kgps=0.051749
    dbObj.mfToughness=139.000000
    dbObj.damageEffect='Famous Cutter WMEC durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','76 mm/62 Mark 75','Bofors 40 mm/70 Mark 3','Bofors 40 mm/70 Mark 3','Bofors 40 mm/70 Mark 3','Bofors 40 mm/70 Mark 3']
    dbObj.maMagazineClass=['USCGS Helo Support','Famous Ammo Mag']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,240.000000,170.000000,170.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,90.000000,90.000000,270.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=38.446999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=28.115000
    airDetectionDBObject.irSignature_dB=17.899000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.300000
    dbObj.beam_m=12.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=8000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=1.000000
    dbObj.FlashyPaintScheme=1.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
