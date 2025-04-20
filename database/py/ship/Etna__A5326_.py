import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Etna (A5326)'
    dbObj.natoClass='Etna (A5326)'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=13400000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1998.569946
    dbObj.finalYear=2999.000000
    dbObj.country='Italy'
    dbObj.designation='AOR'
    dbObj.imageList='etna.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='tanker.xml'
    dbObj.notes='7600 nmi range at 18 kts. May need an air search radar and ESM system'
    dbObj.length_m=146.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPN-748']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=21.000000
    dbObj.mfAccel_ktsps=0.027026
    dbObj.mfTurnRate_degps=1.065784
    dbObj.mfFuelCapacity_kg=1474000.000000
    dbObj.mfFuelRate_kgps=0.458574
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Etna (A5326) durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['76 mm/62 Mark 75 Compact','20mm/70 Oerlikon Mk1/2/3/4']
    dbObj.maMagazineClass=['Cargo 39000']
    dbObj.magazineId=[1]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['Gun','CIWS']
    dbObj.launcherFOV_deg=[240.000000,270.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000]
    dbObj.launcherEl_deg=[30.000000,30.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=51.452000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.020000
    airDetectionDBObject.irSignature_dB=18.504000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S004.Merchant Very Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.400000
    dbObj.beam_m=21.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=22400.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
