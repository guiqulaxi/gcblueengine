# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 266M Akvamarin-M'
    dbObj.natoClass='Natya'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=804000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.829956
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='MS'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=61.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','ESM-1.5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Generic Mine Hunting Sonar']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=16.500000
    dbObj.mfAccel_ktsps=0.027217
    dbObj.mfTurnRate_degps=3.004078
    dbObj.mfFuelCapacity_kg=112560.000000
    dbObj.mfFuelRate_kgps=0.166754
    dbObj.mfToughness=12.000000
    dbObj.damageEffect='Pr 266M Akvamarin-M durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['25 mm MGS','25 mm MGS','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/63 (1.2in) AK-230','30 mm/63 (1.2in) AK-230','SA-N-5 x4 launcher x2']
    dbObj.maMagazineClass=['Pr266M Ammo Mag','AK-630 x2 Store','Strela2 x16 Mag']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[170.000000,170.000000,270.000000,270.000000,270.000000,270.000000,360.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,180.000000,0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=33.124001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=19.879000
    airDetectionDBObject.irSignature_dB=17.665001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S001.Merchant Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.970000
    dbObj.beam_m=10.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=500.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.670000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
