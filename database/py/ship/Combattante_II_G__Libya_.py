import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Combattante II G (Libya)'
    dbObj.natoClass='Combattante II G (Libya)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=311000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.099976
    dbObj.finalYear=3000.000000
    dbObj.country='Libya'
    dbObj.designation='PGG'
    dbObj.imageList='boat.jpg'
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='pg-84.xml'
    dbObj.notes=''
    dbObj.length_m=47.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','TRS 3030 Triton']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=39.000000
    dbObj.mfAccel_ktsps=0.233816
    dbObj.mfTurnRate_degps=6.765627
    dbObj.mfFuelCapacity_kg=27499.000000
    dbObj.mfFuelRate_kgps=0.071611
    dbObj.mfToughness=25.000000
    dbObj.damageEffect='Tiger Type 148 FACM durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['Otomat Launcher x2','Otomat Launcher x2','76 mm/62 Mark 75','40 mm 2xL70 Bofors']
    dbObj.maMagazineClass=['Combattante IIG Ammo Mag']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[330.000000,240.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[180.000000,0.000000,60.000000,300.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,20.000000,20.000000]
    dbObj.launcherFireControl=['TRS 3030 Triton','TRS 3030 Triton','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=26.937000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=17.073999
    airDetectionDBObject.irSignature_dB=17.395000
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
    dbObj.draft_m=2.000000
    dbObj.beam_m=7.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=12000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
