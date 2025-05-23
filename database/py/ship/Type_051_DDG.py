# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 051 DDG'
    dbObj.natoClass='Luda'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3670000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1971.000000
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
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJC-IV Passive','SJD-2','Type 343G','Type 354','Type 515','Type 707','Type 921-A ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.055185
    dbObj.mfTurnRate_degps=2.079361
    dbObj.mfFuelCapacity_kg=513800.000000
    dbObj.mfFuelRate_kgps=0.864976
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 051 DDG durability'
    dbObj.mnNumLaunchers=14
    dbObj.maLauncherClass=['3 HY-1','3 HY-1','130 mm/58 (5.1in) Type 76','130 mm/58 (5.1in) Type 76','57mm /70 (2.24in) Type 59 Twin Barrel','57mm /70 (2.24in) Type 59 Twin Barrel','57mm /70 (2.24in) Type 59 Twin Barrel','57mm /70 (2.24in) Type 59 Twin Barrel','25mm/60(1in) Type 61','25mm/60(1in) Type 61','EDS-25B Mortar','EDS-25B Mortar','DC Rack 8 Chn','DC Rack 8 Chn']
    dbObj.maMagazineClass=['25mm Type 61 Store x2 8000 Rounds','57mm Type 59 Store x4 2000 Rounds','130 mm/58 (5.1in) Type 76 x2 800 Rounds','EDS-25B x2 36 Rounds']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    dbObj.launcherName=['','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,320.000000,320.000000,300.000000,170.000000,300.000000,170.000000,170.000000,170.000000,10.000000,10.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,0.000000,90.000000,180.000000,270.000000,90.000000,270.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','Type 343G','Type 343G','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.015999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.391001
    airDetectionDBObject.irSignature_dB=20.548000
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
    dbObj.draft_m=4.600000
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
