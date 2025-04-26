# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 054 FFG'
    dbObj.natoClass='Type 054 FFG'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4300000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2005.133057
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='FFG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='cn_type-054a_jiangkai-ii.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-335 Platina Active','MG-335 Platina Passive','Type 344','Type 345','Type 347','Type 362','Type 363','Type 826','Type 985-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.061521
    dbObj.mfTurnRate_degps=1.811768
    dbObj.mfFuelCapacity_kg=602000.000000
    dbObj.mfFuelRate_kgps=0.376247
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 054 FFG durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['YJ-83 Quad Launcher','YJ-83 Quad Launcher','HQ-7 Octuple Launcher','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','100mm/56 Type-79A Twin-mount']
    dbObj.maMagazineClass=['Z-9C 1.2 Support','AK-630 x4 Store','100mm AK-100 Magazine 350 rounds','Crotale Naval 16']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,170.000000,170.000000,170.000000,170.000000,320.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,85.000000,95.000000,265.000000,275.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type 344','Type 344','Type 345','Type 347','Type 347','Type 347','Type 347','Type 344']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=34.048000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.007000
    airDetectionDBObject.irSignature_dB=18.438999
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
    dbObj.draft_m=5.000000
    dbObj.beam_m=15.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=28200.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
