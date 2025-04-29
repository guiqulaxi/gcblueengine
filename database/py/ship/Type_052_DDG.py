# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 052 DDG'
    dbObj.natoClass='Luhu'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4800000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1994.000000
    dbObj.finalYear=2003.000000
    dbObj.country='China'
    dbObj.designation='DDG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42_temp.xml'
    dbObj.notes=''
    dbObj.length_m=144.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DRBV 15C','ESS-1 VDS','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJD-8 Active','SJD-9 Passive','Type 344','Type 345','Type 347','Type 360','Type 362','Type 518','Type 928-1','Type 984-1/2']
    sensorPlatformDBObject.sensorAz=[0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=0.188374
    dbObj.mfTurnRate_degps=1.831176
    dbObj.mfFuelCapacity_kg=513800.000000
    dbObj.mfFuelRate_kgps=0.864976
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 052 DDG durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['YJ-82 x4','YJ-82 x4','100mm/56 Type-79A Twin-mount','HQ-7 Octuple Launcher','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','324mm Torpedo Tube x3 (China)','324mm Torpedo Tube x3 (China)','EDS-25B Mortar','EDS-25B Mortar']
    dbObj.maMagazineClass=['Z-9C 2.2 Support','37mm/63 Type 76 Magazine x4','EDS-25B x2 36 Rounds','100mm/56 Type 79A Magazine 300 Rounds','HQ-7 Magazine']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[3,1,2,0,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,320.000000,320.000000,300.000000,170.000000,170.000000,300.000000,30.000000,30.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,0.000000,90.000000,270.000000,180.000000,90.000000,270.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','Type 345','Type 347','Type 347','Type 347','Type 347','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.764000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.611000
    airDetectionDBObject.irSignature_dB=21.636999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.100000
    dbObj.beam_m=16.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=63840.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
