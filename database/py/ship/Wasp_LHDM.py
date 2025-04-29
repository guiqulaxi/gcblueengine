# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Wasp LHDM'
    dbObj.natoClass='Wasp LHDM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=41772000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1989.569946
    dbObj.finalYear=3000.000000
    dbObj.country='USA'
    dbObj.designation='LHD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=257.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPS-48(E) AS','SPS-49 AS','SPS-67 SS','SPS-73(V) SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=22.000000
    dbObj.mfAccel_ktsps=0.010520
    dbObj.mfTurnRate_degps=0.648863
    dbObj.mfFuelCapacity_kg=4594920.000000
    dbObj.mfFuelRate_kgps=1.094730
    dbObj.mfToughness=632.000000
    dbObj.damageEffect='Wasp LHDM durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','SeaSparrow x8 Launcher','RIM-116A RAM x21','RIM-116A RAM x21','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','25 mm MGS','25 mm MGS']
    dbObj.maMagazineClass=['Wasp Fuel Supply','Phalanx 1 x2 Store','Wasp LHDM Missile Store','Wasp LHDM Ammo Mag','Wasp Airwing Magazine']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[3,1,2,0,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,300.000000,300.000000,240.000000,240.000000,270.000000,270.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,0.000000,180.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPS-48(E) AS','SPS-48(E) AS','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=58.859001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=30.908001
    airDetectionDBObject.irSignature_dB=25.298000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=32.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.100000
    dbObj.beam_m=32.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=70000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Wasp Flightdeck'
    dbObj.CalculateParams()
    return dbObj
