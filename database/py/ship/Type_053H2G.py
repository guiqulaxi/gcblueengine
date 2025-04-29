# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 053H2G'
    dbObj.natoClass='Jiangwie I'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2250000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1992.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='FFG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='cn_type-053h2g_jianwei.xml'
    dbObj.notes=''
    dbObj.length_m=111.699997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Decca 1229','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJC-1B Passive','SJD-7 Active','Type 341','Type 343G','Type 360','Type 517h-1','Type 921-A ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.092685
    dbObj.mfTurnRate_degps=2.387217
    dbObj.mfFuelCapacity_kg=315000.000000
    dbObj.mfFuelRate_kgps=0.279998
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 053H2G durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['HQ-61 6pk Launcher','YJ-82 x3','YJ-82 x3','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','100mm/56 Type-79A Twin-mount','EDS-25A Mortar','EDS-25A Mortar']
    dbObj.maMagazineClass=['Z-9C 1.2 Support','HQ-61 6pk 24 rounds','100mm/56 Type 79A Magazine 300 Rounds','37mm/63 Type 76 Magazine x4','EDS-25A x2 12 rounds']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[0,1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,240.000000,240.000000,300.000000,300.000000,300.000000,300.000000,320.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,45.000000,135.000000,315.000000,225.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type 341','','','Type 341','Type 341','Type 341','Type 341','Type 343G','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=39.827999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.638000
    airDetectionDBObject.irSignature_dB=17.191999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
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
    dbObj.beam_m=12.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=24000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
