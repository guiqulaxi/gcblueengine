# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 062B PBG(Vietnam, North)'
    dbObj.natoClass='Shanghai II'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=155000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1961.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Vietnam, North'
    dbObj.designation='PG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='pg-84.xml'
    dbObj.notes=''
    dbObj.length_m=38.779999
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Active Sonar Chinese PB','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Reya']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=34.000000
    dbObj.mfAccel_ktsps=0.125131
    dbObj.mfTurnRate_degps=8.359827
    dbObj.mfFuelCapacity_kg=17500.000000
    dbObj.mfFuelRate_kgps=0.103298
    dbObj.mfToughness=25.000000
    dbObj.damageEffect='Type 062B PBG durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['37mm/63(1.5in) Type 676','37mm/63(1.5in) Type 676','25mm/60(1in) Type 61','25mm/60(1in) Type 61','DC Rack 8 Chn']
    dbObj.maMagazineClass=['Type 062B Ammo Mag']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[300.000000,320.000000,270.000000,270.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,125.000000,235.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=22.400999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=15.115000
    airDetectionDBObject.irSignature_dB=16.398001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=5.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.550000
    dbObj.beam_m=5.410000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=2400.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
