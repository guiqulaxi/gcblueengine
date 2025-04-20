import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='San Antonio LPDM'
    dbObj.natoClass='San Antonio LPDM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=25300000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2006.040039
    dbObj.finalYear=3000.000000
    dbObj.country='USA'
    dbObj.designation='LPD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=208.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SLQ-32(v)2 ESM B.1','SLQ-32(v)2 ESM B.2','SLQ-32(v)2 ESM B.3','SPS-48(E) AS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=22.000000
    dbObj.mfAccel_ktsps=0.021985
    dbObj.mfTurnRate_degps=0.808554
    dbObj.mfFuelCapacity_kg=2783000.000000
    dbObj.mfFuelRate_kgps=1.193479
    dbObj.mfToughness=1000.000000
    dbObj.damageEffect='San Antonio LPDM durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','0.50in/72 (12.7 mm) M3M FN Herstal MG (GAU-21)','30 mm Bushmaster II Mark 46 Mod 1','30 mm Bushmaster II Mark 46 Mod 1','Mk-41 Mod4 VLS','RIM-116A RAM x11(mk31?)']
    dbObj.maMagazineClass=['San Antonio Ammo Mag','Mk-41 VLS Mod4 16 Cell']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[170.000000,170.000000,170.000000,170.000000,240.000000,240.000000,0.000000,300.000000]
    dbObj.launcherAz_deg=[90.000000,90.000000,270.000000,270.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,90.000000,40.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,False,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=54.042999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.879000
    airDetectionDBObject.irSignature_dB=17.500999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.000000
    dbObj.beam_m=32.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=41600.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
