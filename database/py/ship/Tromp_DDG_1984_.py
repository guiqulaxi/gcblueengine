import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Tromp DDG(1984)'
    dbObj.natoClass='Tromp DDG(1984)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4308000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1984.000000
    dbObj.finalYear=1989.000000
    dbObj.country='Netherlands'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=133.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['CWE 610 Active','CWE 610 Passive','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','RAMSES ECM','RAMSES ESM','SPG-51D 1','SPS-01 AS','WM-25']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.198323
    dbObj.mfTurnRate_degps=1.839705
    dbObj.mfFuelCapacity_kg=603120.000000
    dbObj.mfFuelRate_kgps=0.603115
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Tromp DDG durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['Mk-13 Mod4 GMLS','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','SeaSparrow x8 Launcher','12cm/50(4.7in) Model 1950','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Lynx 1.3 Support','Mk-13 Mod4 Rotary Store 40','Sea Sparrow Reloads','12cm/50(4.7in) Model 1950 Magazine']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,0.000000,0.000000,300.000000,320.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,180.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,45.000000,45.000000,40.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-51D 1','','','WM-25','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.060001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.365000
    airDetectionDBObject.irSignature_dB=23.702000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.600000
    dbObj.beam_m=14.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=52200.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
