# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 051G DDG(2001)'
    dbObj.natoClass='Luda III'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3730000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2001.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='DDG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42_temp.xml'
    dbObj.notes=''
    dbObj.length_m=132.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Decca 1229','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJD-8 Active','SJD-9 Passive','Type 343G','Type 345','Type 347','Type 363','Type 517h-1','Type 826','Type 981 ECM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.055106
    dbObj.mfTurnRate_degps=2.068151
    dbObj.mfFuelCapacity_kg=513800.000000
    dbObj.mfFuelRate_kgps=0.864976
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 051G DDG durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['YJ-82 x8','YJ-82 x8','100mm/56 Type-79A Twin-mount','100mm/56 Type-79A Twin-mount','HQ-7 Octuple Launcher','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','25mm/60(1in) Type 61','25mm/60(1in) Type 61','324mm Torpedo Tube x3 (China)','324mm Torpedo Tube x3 (China)']
    dbObj.maMagazineClass=['37mm/63 Type 76 Magazine x4','100mm/56 Type 79A Magazine x2 800 Rounds','25mm Type 61 Store x2 8000 Rounds','Chinese Torpedo Racks(18)','HQ-7 Magazine']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[1,0,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,320.000000,320.000000,320.000000,300.000000,170.000000,170.000000,170.000000,170.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,180.000000,0.000000,90.000000,270.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','Type 343G','Type 343G','Type 345','Type 347','Type 347','Type 347','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.120998
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.417000
    airDetectionDBObject.irSignature_dB=20.552000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.700000
    dbObj.beam_m=12.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=72000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
