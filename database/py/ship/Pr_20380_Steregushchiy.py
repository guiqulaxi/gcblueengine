# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 20380 Steregushchiy'
    dbObj.natoClass='Steregushchiy'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2007.869995
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=111.599998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','ME-02 Zarya Active','ME-02 Zarya Passive','Top Plate AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.090881
    dbObj.mfTurnRate_degps=2.480666
    dbObj.mfFuelCapacity_kg=266000.000000
    dbObj.mfFuelRate_kgps=0.258609
    dbObj.mfToughness=148.000000
    dbObj.damageEffect='Pr 20380 Steregushchiy durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['100 mm/70 (3.9in) AK-100','12.7 mm (0.5in) Degtjarev DShK M38 Heavy Machine Gun','12.7 mm (0.5in) Degtjarev DShK M38 Heavy Machine Gun','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','SS-N-25 x4 Launcher x2']
    dbObj.maMagazineClass=['Pr20380 Ammo Mag','AK-630 x2 Store','Kashtan x2 Store']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,170.000000,170.000000,300.000000,300.000000,300.000000,300.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,0.000000,180.000000,0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,40.000000,40.000000,20.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=31.737000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.738001
    airDetectionDBObject.irSignature_dB=12.674000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.700000
    dbObj.beam_m=14.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=23320.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
