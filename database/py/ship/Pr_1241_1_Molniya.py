import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1241.1 Molniya'
    dbObj.natoClass='Tarantul II'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=436000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.239990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FSG'
    dbObj.imageList='tarantul2.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='[kbluck]'
    dbObj.length_m=56.099998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['34K1 Monolit','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Half Hat','MR-123 Vympel FC','Spin Trough SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=41.000000
    dbObj.mfAccel_ktsps=0.566650
    dbObj.mfTurnRate_degps=5.929837
    dbObj.mfFuelCapacity_kg=61040.000000
    dbObj.mfFuelRate_kgps=0.148360
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Pr 1241.1 Molniya durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['SS-N-2C x2 Launcher','SS-N-2C x2 Launcher','76 mm/59 (3in) AK-176','SA-N-5 x4 launcher','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M']
    dbObj.maMagazineClass=['76mm AK-176 Magazine 152 Rounds','Strela2 x8 Mag']
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
    airDetectionDBObject.RCS_dBsm=29.138000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=19.350000
    airDetectionDBObject.irSignature_dB=23.077000
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
    dbObj.draft_m=2.500000
    dbObj.beam_m=10.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=32000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
