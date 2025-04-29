# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='PC Class Jose Ma Palas'
    dbObj.natoClass='PC Class Jose Ma Palas'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=99000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1989.750000
    dbObj.finalYear=3000.000000
    dbObj.country='Columbia'
    dbObj.designation='PBC'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='pg-84.xml'
    dbObj.notes='Marcos Amram-is a swiftships 110 foot patrol boat.  http://www.swiftships.com/subcommon.php?eC&MnK&ecB'
    dbObj.length_m=109.900002
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Kelvin Hughes']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.255027
    dbObj.mfTurnRate_degps=6.415481
    dbObj.mfFuelCapacity_kg=29997.000000
    dbObj.mfFuelRate_kgps=0.058327
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='PC Class Jose Ma Palas durability'
    dbObj.mnNumLaunchers=1
    dbObj.maLauncherClass=['Launcher 40/70L-simple']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0]
    dbObj.launcherName=['']
    dbObj.launcherFOV_deg=[360.000000]
    dbObj.launcherAz_deg=[0.000000]
    dbObj.launcherEl_deg=[0.000000]
    dbObj.launcherFireControl=['']
    dbObj.launcherFireControl2=['']
    dbObj.launcherIsReloadable=[False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=19.480000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.426001
    airDetectionDBObject.irSignature_dB=17.082001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.130000
    dbObj.beam_m=24.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=2400.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
