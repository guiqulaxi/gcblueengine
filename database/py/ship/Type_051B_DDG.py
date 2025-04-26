# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 051B DDG'
    dbObj.natoClass='Luhai'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=6100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1998.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='DDG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42_temp.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Decca 1226','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJD-8 Active','SJD-9 Passive','Type 344','Type 345','Type 347','Type 363','Type 381','Type 517h-1','Type 826','Type 984-1/2']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.500000
    dbObj.mfAccel_ktsps=0.160321
    dbObj.mfTurnRate_degps=1.648973
    dbObj.mfFuelCapacity_kg=854000.000000
    dbObj.mfFuelRate_kgps=0.790734
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 051B DDG durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['YJ-83 x8','YJ-83 x8','100mm/56 Type-79A Twin-mount','HQ-7 Octuple Launcher','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','324mm Torpedo Tube x3 (China)','324mm Torpedo Tube x3 (China)']
    dbObj.maMagazineClass=['Z-9C 2.2 Support','37mm/63 Type 76 Magazine x4','100mm/56 Type 79A Magazine 300 Rounds','HQ-7 Magazine']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,320.000000,320.000000,300.000000,170.000000,170.000000,300.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,0.000000,90.000000,270.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','Type 343G','Type 345','Type 347','Type 347','Type 347','Type 347','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=46.326000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.090000
    airDetectionDBObject.irSignature_dB=21.704000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.000000
    dbObj.beam_m=16.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=57440.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
