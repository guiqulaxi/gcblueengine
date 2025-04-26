# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Converted Raleigh AGFH'
    dbObj.natoClass='Converted Raleigh AGFH'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=14650000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1972.500000
    dbObj.finalYear=2005.400024
    dbObj.country='USA'
    dbObj.designation='AGF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)2 ESM B.3','SLQ-32(v)2 ESM B.3','SLQ-32(v)2 ESM B.3','SPS-10F','SPS-40']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=0.012079
    dbObj.mfTurnRate_degps=0.989643
    dbObj.mfFuelCapacity_kg=1611500.000000
    dbObj.mfFuelRate_kgps=0.414477
    dbObj.mfToughness=637.000000
    dbObj.damageEffect='Converted Raleigh AGFH durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','25 mm MGS','25 mm MGS']
    dbObj.maMagazineClass=['Converted Raleigh Ammo Mag','Phalanx 1 x2 Store']
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,270.000000,270.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=52.033001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.865000
    airDetectionDBObject.irSignature_dB=25.004000
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
    dbObj.draft_m=6.400000
    dbObj.beam_m=25.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=24000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
