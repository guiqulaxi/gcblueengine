import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Gepard Type 143 (1993)'
    dbObj.natoClass='Gepard Type 143 (1993)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=398000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1993.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation='PGG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=57.599998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','WM-27']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=40.000000
    dbObj.mfAccel_ktsps=0.272491
    dbObj.mfTurnRate_degps=5.998146
    dbObj.mfFuelCapacity_kg=55720.000000
    dbObj.mfFuelRate_kgps=0.095247
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Gepard Type 143 durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['76 mm/62 Mark 75','RIM-116A RAM x21','Exocet Twin Launcher','Exocet Twin Launcher']
    dbObj.maMagazineClass=['76mm/62 mk75 240 rounds','RIM-116 21 x1 Store']
    dbObj.magazineId=[1,2]
    dbObj.launcherId=[0,1,3,4]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[330.000000,340.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,20.000000,20.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=28.544001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.589001
    airDetectionDBObject.irSignature_dB=17.468000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.600000
    dbObj.beam_m=7.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=17748.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
