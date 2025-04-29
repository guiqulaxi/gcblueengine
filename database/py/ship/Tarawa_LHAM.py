# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Tarawa LHAM'
    dbObj.natoClass='Tarawa LHAM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=39967000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1976.410034
    dbObj.finalYear=3000.000000
    dbObj.country='USA'
    dbObj.designation='LHA'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=254.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)3 ECM','SLQ-32(v)3 ESM B.1','SLQ-32(v)3 ESM B.2','SLQ-32(v)3 ESM B.3','SPS-40E','SPS-48(E) AS','SPS-67 SS','SPS-73(V) SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=24.000000
    dbObj.mfAccel_ktsps=0.010753
    dbObj.mfTurnRate_degps=0.689790
    dbObj.mfFuelCapacity_kg=4396370.000000
    dbObj.mfFuelRate_kgps=1.221203
    dbObj.mfToughness=595.000000
    dbObj.damageEffect='Tarawa LHAM durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['RIM-116A RAM x21','RIM-116A RAM x21','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','25 mm MGS','25 mm MGS','25 mm MGS','25 mm MGS','25 mm MGS','25 mm MGS']
    dbObj.maMagazineClass=['Tarawa Ammo Mag','Phalanx 1 x2 Store','RIM-116 21 x2 Store']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,270.000000,270.000000,240.000000,240.000000,240.000000,240.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,45.000000,135.000000,225.000000,315.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=58.570999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=31.650999
    airDetectionDBObject.irSignature_dB=25.285000
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
    dbObj.draft_m=7.900000
    dbObj.beam_m=40.200001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=70000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Tarawa Flightdeck'
    dbObj.CalculateParams()
    return dbObj
