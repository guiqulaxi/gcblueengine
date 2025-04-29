# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1241.RE Molniya-E'
    dbObj.natoClass='Tarantul I'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=415000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.239990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FSG'
    dbObj.imageList='tarantul1.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=56.099998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Half Hat','MR-123 Vympel FC','Plank Shave AS/SS','Spin Trough SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=43.000000
    dbObj.mfAccel_ktsps=0.568618
    dbObj.mfTurnRate_degps=6.173496
    dbObj.mfFuelCapacity_kg=58100.000000
    dbObj.mfFuelRate_kgps=0.102701
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Pr 1241.RE Molniya-E durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['SS-N-2D x2 Launcher','SS-N-2D x2 Launcher','76 mm/59 (3in) AK-176','SA-N-5 x4 launcher','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M']
    dbObj.maMagazineClass=['76mm AK-176 Magazine 152 Rounds','Strela2 x16 Mag']
    dbObj.mnNumMagazines=2
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,240.000000,360.000000,270.000000,270.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[20.000000,20.000000,85.000000,40.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=28.816000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=19.231001
    airDetectionDBObject.irSignature_dB=23.063000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.200000
    dbObj.beam_m=10.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=34000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
