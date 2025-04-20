import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CVN R98 Clemenceau/R99 Foch'
    dbObj.natoClass='CVN R98 Clemenceau/R99 Foch'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=32780000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1961.890015
    dbObj.finalYear=1987.079956
    dbObj.country='France'
    dbObj.designation='CVN'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes='This version with 100 mm turrets before major refit in 80s. 60 days endurance. About 1800 m3 of aviation fuel = 1.4M kg. Refit for SAMs for CVN R98 Clemenceau/R99 Foch was 1 Sep 1985 - 31 Aug 1989. Foch was Feb 87 to early 88 according to globalsecurity.org. NEED TO FINISH ADDING AIRCRAFT'
    dbObj.length_m=264.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DRBI-10','DRBV 23B','DRBV 50']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.018071
    dbObj.mfTurnRate_degps=0.842736
    dbObj.mfFuelCapacity_kg=3605800.000000
    dbObj.mfFuelRate_kgps=2.403846
    dbObj.mfToughness=1086.000000
    dbObj.damageEffect='CVN R98 Clemenceau/R99 Foch durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['100mm/55 x2','100mm/55 x2','100mm/55 x2','100mm/55 x2']
    dbObj.maMagazineClass=['Generic Stores','Carrier Magazine','Carrier Fuel Supply']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[90.000000,90.000000,90.000000,90.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,180.000000,270.000000]
    dbObj.launcherEl_deg=[30.000000,30.000000,30.000000,30.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=57.279999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=32.771999
    airDetectionDBObject.irSignature_dB=22.257000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=17.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=25.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S12.Carrier Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.600000
    dbObj.beam_m=51.200001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=126000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Clem Flightdeck'
    dbObj.CalculateParams()
    return dbObj
