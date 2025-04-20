import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Cassard(88)'
    dbObj.natoClass='Cassard(88)'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=500000000.000000
    dbObj.weight_kg=4500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1988.569946
    dbObj.finalYear=1992.000000
    dbObj.country='France'
    dbObj.designation='DD'
    dbObj.imageList='cassard.jpg'
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=139.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBR 17','DIBC 1A','DRBJ 15','DRBV 26C','DUBA-25A Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPG-51D 1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.084534
    dbObj.mfTurnRate_degps=1.825695
    dbObj.mfFuelCapacity_kg=630000.000000
    dbObj.mfFuelRate_kgps=0.371872
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Cassard(88) durability'
    dbObj.mnNumLaunchers=15
    dbObj.maLauncherClass=['Mk-13 Mod4 GMLS','Mistral Sadral','Mistral Sadral','20 mm F2 Cannon','20 mm F2 Cannon','Exocet Quad Launcher','Exocet Quad Launcher','100mm/55 (3.9in) model 1968 CADAM','KD59E Torp Launcher','KD59E Torp Launcher','12.7 mm Machine Gun Generic','Sagaie CM','Sagaie CM','Sagaie CM','Sagaie CM']
    dbObj.maMagazineClass=['AS 565 1.2 Support','Mk-13 Mod4 Rotary Store 40','100mm/55 Model 1968 600 rounds','Mistral Sadral Mag x2','French Combat Stores']
    dbObj.magazineId=[1,0,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    dbObj.launcherName=['','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,220.000000,220.000000,120.000000,120.000000,30.000000,30.000000,300.000000,180.000000,180.000000,360.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[180.000000,130.000000,230.000000,90.000000,90.000000,90.000000,270.000000,0.000000,90.000000,270.000000,0.000000,90.000000,270.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,30.000000,30.000000,12.000000,12.000000,0.000000,0.000000,0.000000,10.000000,45.000000,45.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['SPG-51D 16','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False,False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.344002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.354000
    airDetectionDBObject.irSignature_dB=21.131001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.500000
    dbObj.beam_m=14.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=42000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
