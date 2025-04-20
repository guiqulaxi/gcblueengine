import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Ocean LPH'
    dbObj.natoClass='Ocean LPH'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=210600000.000000
    dbObj.weight_kg=21500278.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1998.000000
    dbObj.finalYear=3000.000000
    dbObj.country='UK'
    dbObj.designation='LPH'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes='[phoenixegmh]'
    dbObj.length_m=203.399994
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Centaur ESM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Sampson','Type 1007']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=18.000000
    dbObj.mfAccel_ktsps=0.015525
    dbObj.mfTurnRate_degps=0.776463
    dbObj.mfFuelCapacity_kg=4594920.000000
    dbObj.mfFuelRate_kgps=1.033765
    dbObj.mfToughness=632.000000
    dbObj.damageEffect='Ocean LPH durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['30 mm Bushmaster II Mark 46 Mod 1','30 mm Bushmaster II Mark 46 Mod 1','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B']
    dbObj.maMagazineClass=['Wasp Fuel Supply','Ocean LPH Ammo Mag','Ocean Airwing Magazine']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['Port','Stbd','','','']
    dbObj.launcherFOV_deg=[140.000000,140.000000,270.000000,270.000000,270.000000]
    dbObj.launcherAz_deg=[270.000000,90.000000,0.000000,120.000000,240.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.532001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=30.049000
    airDetectionDBObject.irSignature_dB=17.618999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=32.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.500000
    dbObj.beam_m=35.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=18360.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Ocean Flightdeck'
    dbObj.CalculateParams()
    return dbObj
