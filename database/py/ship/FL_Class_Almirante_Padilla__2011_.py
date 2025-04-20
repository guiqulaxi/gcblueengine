import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='FL Class Almirante Padilla (2011)'
    dbObj.natoClass='FL Class Almirante Padilla (2011)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2011.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Columbia'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes='Marcos'
    dbObj.length_m=99.099998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ASO-84-5-ACT','ASO-84-5-PAS','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Furuno','Mirador-EOD','SMART-S Mk2','STING-EO Mk2','Scanter 2001','Vigile-300']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.081576
    dbObj.mfTurnRate_degps=2.471596
    dbObj.mfFuelCapacity_kg=294000.000000
    dbObj.mfFuelRate_kgps=0.228665
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='FL Class Almirante Padilla durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Mistral Simbad','exocet3-padilla','76 mm/62 Mark 75 Compact','76 mm/62 Mark 75 Compact','Launcher 40/70L-1','chaff padilla']
    dbObj.maMagazineClass=['Padilla Fuel Helo','76/62 Compact santabarbara','Padilla Chaff']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,270.000000,270.000000,180.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','STRALES','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,False,True,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=39.379002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.448000
    airDetectionDBObject.irSignature_dB=17.941999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.500000
    dbObj.beam_m=11.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=23400.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='FFG-7 Helo Deck'
    dbObj.CalculateParams()
    return dbObj
