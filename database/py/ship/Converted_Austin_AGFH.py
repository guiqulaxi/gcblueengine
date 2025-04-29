# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Converted Austin AGFH'
    dbObj.natoClass='Converted Austin AGFH'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=16912000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.750000
    dbObj.finalYear=2006.750000
    dbObj.country='USA'
    dbObj.designation='AGF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=173.800003
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)2 ESM B.3','SLQ-32(v)2 ESM B.3','SLQ-32(v)2 ESM B.3','SPS-10F']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=21.000000
    dbObj.mfAccel_ktsps=0.011298
    dbObj.mfTurnRate_degps=0.944973
    dbObj.mfFuelCapacity_kg=1860320.000000
    dbObj.mfFuelRate_kgps=0.494499
    dbObj.mfToughness=738.000000
    dbObj.damageEffect='Converted Austin AGFH durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B']
    dbObj.maMagazineClass=['Converted Austin Ammo Mag','Phalanx 1 x2 Store']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[170.000000,170.000000,270.000000,270.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=52.969002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=28.950001
    airDetectionDBObject.irSignature_dB=27.080000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.000000
    dbObj.beam_m=30.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=24000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
