# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1134 Berkut'
    dbObj.natoClass='Kresta I'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=5340000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.770020
    dbObj.finalYear=1994.510010
    dbObj.country='Russia'
    dbObj.designation='CG'
    dbObj.imageList='kresta1.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['4R90 Yatagan 2','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Gurzef ESM','Gurzef-1 ESM','MG-312 Titan Active','MR-310U Angara M(Head Net C)','MR-500 Kliver','MRP-25 SS','Vychegda TA Active','Vychegda TA Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.051805
    dbObj.mfTurnRate_degps=1.759387
    dbObj.mfFuelCapacity_kg=747600.000000
    dbObj.mfFuelRate_kgps=0.747594
    dbObj.mfToughness=747.000000
    dbObj.damageEffect='Pr 1134 Berkut durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['S-125M Twin Launcher','S-125M Twin Launcher','SS-N-3 x2 Launcher x2','57 mm/75 (2.24in) AK-725 (ZIF-72) twin barrel','57 mm/75 (2.24in) AK-725 (ZIF-72) twin barrel','533mm torpedo x5 tubes','533mm torpedo x5 tubes']
    dbObj.maMagazineClass=['KA-25 2.2 Support','AK-725 x2 Store','Kresta I Sam Store','Kresta Torpedo Racks']
    dbObj.magazineId=[1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,320.000000,0.000000,170.000000,170.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,20.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['4R90 Yatagan 2','4R90 Yatagan 2','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=45.459000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.224001
    airDetectionDBObject.irSignature_dB=23.761999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.600000
    dbObj.beam_m=16.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=92000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
