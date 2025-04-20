import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr M123bis Komsomolets (Romania)'
    dbObj.natoClass='Pr M123bis Komsomolets (Romania)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=20500.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1952.900024
    dbObj.finalYear=1964.000000
    dbObj.country='Romania'
    dbObj.designation='PTB'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=18.660000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=50.000000
    dbObj.mfAccel_ktsps=0.390735
    dbObj.mfTurnRate_degps=23.890551
    dbObj.mfFuelCapacity_kg=236600.000000
    dbObj.mfFuelRate_kgps=0.298735
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Pr 123K durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['450mm TTKA-45 Torpedo Tube','450mm TTKA-45 Torpedo Tube','12.7 mm (0.5in) 2-UKT Twin','12.7 mm (0.5in) 2-UKT Twin','BM1 DCx6']
    dbObj.maMagazineClass=['2UKT x2 Magazine']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,300.000000,330.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,45.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=37.964001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.743000
    airDetectionDBObject.irSignature_dB=19.848000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=0.760000
    dbObj.beam_m=3.430000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=2000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
