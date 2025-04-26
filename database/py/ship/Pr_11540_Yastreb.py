# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 11540 Yastreb'
    dbObj.natoClass='Neustrashimy'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4250000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1990.989990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Cross Dome AS/SS','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Half Hat','MGK-365 Zvezda M-1 Active','MGK-365 Zvezda M-1 Passive','MGK-365 Zvezda M-1 TA','Palm Frond SS','Top Plate AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.177187
    dbObj.mfTurnRate_degps=1.892944
    dbObj.mfFuelCapacity_kg=595000.000000
    dbObj.mfFuelRate_kgps=0.991658
    dbObj.mfToughness=327.000000
    dbObj.damageEffect='Pr 11540 Yastreb durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['100 mm/70 (3.9in) AK-100','533mm torpedo x3 tubes','533mm torpedo x3 tubes','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','SA-N-9 x8 VLS Launcher x4']
    dbObj.maMagazineClass=['KA-25 1.1 Support','Kashtan x2 Store','AK-630 x2 Store','Pr11540 Ammo Mag']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,40.000000,40.000000,220.000000,220.000000,220.000000,220.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,135.000000,225.000000,135.000000,225.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,40.000000,40.000000,90.000000]
    dbObj.launcherFireControl=['','','','','','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=40.960999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.020000
    airDetectionDBObject.irSignature_dB=21.108999
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
    dbObj.draft_m=4.800000
    dbObj.beam_m=15.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=57000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
