# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 053K FFG'
    dbObj.natoClass='Jiangdong'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1925000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='FFG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42_temp.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJD-5','Type 341','Type 343G','Type 352','Type 354','Type 921-A ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=26.000000
    dbObj.mfAccel_ktsps=0.063172
    dbObj.mfTurnRate_degps=2.471592
    dbObj.mfFuelCapacity_kg=269500.000000
    dbObj.mfFuelRate_kgps=0.389274
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 053K FFG durability'
    dbObj.mnNumLaunchers=13
    dbObj.maLauncherClass=['HQ-61 Twin Launcher','HQ-61 Twin Launcher','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','100mm/56 Type-79A Twin-mount','100mm/56 Type-79A Twin-mount','EDS-25A Mortar','EDS-25A Mortar','DC Rack 8 Chn']
    dbObj.maMagazineClass=['37mm/63 Type 76 Magazine x6','100mm/56 Type 79A Magazine x2 600 Rounds','EDS-25A x2 12 rounds','HQ-61 Twin x2 32 Rounds']
    dbObj.magazineId=[1,0,2,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    dbObj.launcherName=['','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,320.000000,170.000000,170.000000,300.000000,300.000000,300.000000,300.000000,320.000000,320.000000,10.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,90.000000,270.000000,45.000000,135.000000,315.000000,225.000000,0.000000,180.000000,0.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type 341','Type 341','Type 341','Type 341','Type 341','Type 341','Type 341','Type 341','Type 343G','Type 343G','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=38.812000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.337000
    airDetectionDBObject.irSignature_dB=17.134001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.100000
    dbObj.beam_m=10.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=14400.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
