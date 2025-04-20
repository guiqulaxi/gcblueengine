import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Fridtjof Nansen FFGHM'
    dbObj.natoClass='Fridtjof Nansen FFGHM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2006.260010
    dbObj.finalYear=2999.000000
    dbObj.country='Norway'
    dbObj.designation='FFG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes=''
    dbObj.length_m=134.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['CS-3701 ESM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MRS 2000 Active','MRS 2000 Passive','Mk-2 ATAS','SPG-62 8','SPY-1F','VAMPIR NG IIRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.145656
    dbObj.mfTurnRate_degps=1.873990
    dbObj.mfFuelCapacity_kg=630000.000000
    dbObj.mfFuelRate_kgps=0.622217
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Fridtjof Nansen FFGHM durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Mk-41 Mod10 VLS','NSM Launcher x4','NSM Launcher x4','76 mm/62 Mark 75 Compact','Eurotorp TLS launcher','Eurotorp TLS launcher']
    dbObj.maMagazineClass=['NH-90 1.1 Support','76mm/62 mk75 240 rounds','Mk-41 VLS Mod10 8 Cell']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,360.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-62 8','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=31.334000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.681999
    airDetectionDBObject.irSignature_dB=15.415000
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
    dbObj.draft_m=6.100000
    dbObj.beam_m=16.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=30000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
