# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 12347 Nakat'
    dbObj.natoClass='Nanuchka IV'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=639000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1987.750000
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FSG'
    dbObj.imageList='nanuchka4.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='Only one ship commissioned'
    dbObj.length_m=59.299999
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['34K1 Monolit','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Half Hat','MR-123 Vympel FC','Peel Pair AS/SS','Pop Group FC']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=35.000000
    dbObj.mfAccel_ktsps=0.250903
    dbObj.mfTurnRate_degps=4.756897
    dbObj.mfFuelCapacity_kg=89460.000000
    dbObj.mfFuelRate_kgps=0.085199
    dbObj.mfToughness=50.000000
    dbObj.damageEffect='Pr 12347 Nakat durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['SS-N-26 x6 Launcher','SS-N-26 x6 Launcher','SA-N-4 x2(16) Launcher','76 mm/59 (3in) AK-176','30 mm/54 (1.2in) AK-630M']
    dbObj.maMagazineClass=['76mm AK-176 Magazine 152 Rounds','9K33 OSA Store']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,300.000000,320.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,40.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[20.000000,20.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','Pop Group FC','MR-123 Vympel FC','MR-123 Vympel FC']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=31.628000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=20.301001
    airDetectionDBObject.irSignature_dB=17.608000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=3.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.080000
    dbObj.beam_m=11.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=30000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
