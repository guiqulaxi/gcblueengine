# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV-551 Giuseppe Garibaldi'
    dbObj.natoClass='CV-551 Giuseppe Garibaldi'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=13850000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1985.746948
    dbObj.finalYear=2003.000000
    dbObj.country='Italy'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DE-1160B Active','DE-1160B Passive','ELT 211 ESM','ELT 318 ECM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','RAN-10S','RAN-3L','RTN-20X x3','SPS-52C AS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.111505
    dbObj.mfTurnRate_degps=1.196352
    dbObj.mfFuelCapacity_kg=1523500.000000
    dbObj.mfFuelRate_kgps=1.209117
    dbObj.mfToughness=1000.000000
    dbObj.damageEffect='CV-551 Giuseppe Garibaldi durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['Albatross Launcher','Albatross Launcher','40mm Twin Fast Forty','40mm Twin Fast Forty','40mm Twin Fast Forty','Otomat Launcher x2','Otomat Launcher x2','533mm B-515 Torpedo Launcher x3','533mm B-515 Torpedo Launcher x3']
    dbObj.maMagazineClass=['Guiseppe Garibaldi Magazine','Guiseppe Garibaldi Fuel Supply']
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,170.000000,170.000000,260.000000,360.000000,360.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,85.000000,275.000000,180.000000,30.000000,330.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,15.000000,15.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['RTN-20X x3','RTN-20X x3','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=51.667000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.573999
    airDetectionDBObject.irSignature_dB=24.028000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=12.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.200000
    dbObj.beam_m=33.400002
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=82000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Garibaldi Flightdeck'
    dbObj.CalculateParams()
    return dbObj
