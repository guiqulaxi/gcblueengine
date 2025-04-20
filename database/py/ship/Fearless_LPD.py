import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Fearless LPD'
    dbObj.natoClass='Fearless LPD'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=12120000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1965.900024
    dbObj.finalYear=2002.209961
    dbObj.country='UK'
    dbObj.designation='LPD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes=''
    dbObj.length_m=158.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Sea Cat Operator','Type 978','Type 993']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=21.000000
    dbObj.mfAccel_ktsps=0.013304
    dbObj.mfTurnRate_degps=1.080576
    dbObj.mfFuelCapacity_kg=1333200.000000
    dbObj.mfFuelRate_kgps=0.575750
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Fearless LPD durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['Sea Cat Quad launcher','Sea Cat Quad launcher','Sea Cat Quad launcher','Sea Cat Quad launcher']
    dbObj.maMagazineClass=['Sea Cat Store 48']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[290.000000,290.000000,290.000000,290.000000]
    dbObj.launcherAz_deg=[45.000000,135.000000,215.000000,305.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Phalanx FC','Phalanx FC','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=50.798000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.676001
    airDetectionDBObject.irSignature_dB=21.990000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S003.Merchant Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.300000
    dbObj.beam_m=24.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=22000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Quintuple Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
