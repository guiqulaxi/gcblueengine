# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 775  Ropucha'
    dbObj.natoClass='Ropucha'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4400000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1974.500000
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='LST'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','ESM-6','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MGK-355TA Polinom TA','Strut Curve AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=17.590000
    dbObj.mfAccel_ktsps=0.045110
    dbObj.mfTurnRate_degps=1.510362
    dbObj.mfFuelCapacity_kg=484000.000000
    dbObj.mfFuelRate_kgps=0.247252
    dbObj.mfToughness=63.000000
    dbObj.damageEffect='Pr 775  Ropucha durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','57 mm/75 (2.24in) AK-725 (ZIF-72) twin barrel','57 mm/75 (2.24in) AK-725 (ZIF-72) twin barrel','76 mm/59 (3in) AK-176','SA-N-5 x4 launcher x4']
    dbObj.maMagazineClass=['Pr775 Ammo Mag','AK-630 x2 Store','Strela2 x32 Mag']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,270.000000,240.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.196999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.156000
    airDetectionDBObject.irSignature_dB=18.163000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=14.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S002.Merchant Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.260000
    dbObj.beam_m=15.010000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=19200.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
