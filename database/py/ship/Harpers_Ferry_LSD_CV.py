# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Harpers Ferry LSD-CV'
    dbObj.natoClass='Harpers Ferry LSD-CV'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=16740000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1995.020020
    dbObj.finalYear=2999.989990
    dbObj.country='USA'
    dbObj.designation='LSD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)1 ESM B.3','SPS-49 AS','SPS-64 SS','SPS-67 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=22.000000
    dbObj.mfAccel_ktsps=0.025754
    dbObj.mfTurnRate_degps=0.949128
    dbObj.mfFuelCapacity_kg=1841400.000000
    dbObj.mfFuelRate_kgps=0.602834
    dbObj.mfToughness=255.000000
    dbObj.damageEffect='Harpers Ferry LSD-CV durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['RIM-116A RAM x21','RIM-116A RAM x21','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','25 mm MGS','25 mm MGS']
    dbObj.maMagazineClass=['Harpers Ammo Mag','Harpers Missile Mag','Phalanx 1 x2 Store']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,240.000000,240.000000,240.000000,240.000000,270.000000,270.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,45.000000,135.000000,225.000000,315.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=52.902000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=28.677999
    airDetectionDBObject.irSignature_dB=18.617001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S002.Merchant Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.400000
    dbObj.beam_m=26.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=33000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
