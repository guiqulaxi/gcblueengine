import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Halifax FFH'
    dbObj.natoClass='Halifax FFH'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=1000000000.000000
    dbObj.weight_kg=5032000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1992.489990
    dbObj.finalYear=2999.000000
    dbObj.country='Canada'
    dbObj.designation='FF'
    dbObj.imageList='halifax.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=134.100006
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SLQ-501 ESM','SPG-503','SPS-49(V)8','SQS-510 Active','SQS-510 Passive','Type 1007']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.165978
    dbObj.mfTurnRate_degps=1.864338
    dbObj.mfFuelCapacity_kg=704480.000000
    dbObj.mfFuelRate_kgps=0.489218
    dbObj.mfToughness=715.000000
    dbObj.damageEffect='Halifax FFH durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['ESSM 2x4 Launcher','ESSM 2x4 Launcher','20mm/99 M-61A1 Gatling OGB Mark 15 Block 1B','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','57 mm/70 (2.25in) Marks 2 - 3','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Shield Mark 2','Shield Mark 2']
    dbObj.maMagazineClass=['Ship stores','Phalanx 1 x2 Store','Main gun reloads']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,270.000000,0.000000,0.000000,320.000000,40.000000,40.000000,45.000000,45.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,180.000000,90.000000,270.000000,0.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,30.000000,30.000000]
    dbObj.launcherFireControl=['SPG-503','SPG-503','Phalanx FC','','','SPG-503','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=45.071999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.348000
    airDetectionDBObject.irSignature_dB=23.745001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.900000
    dbObj.beam_m=16.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=56300.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Burke Helo Deck'
    dbObj.CalculateParams()
    return dbObj
