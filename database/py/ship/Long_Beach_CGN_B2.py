import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Long Beach CGN B2'
    dbObj.natoClass='Long Beach CGN B2'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=15540000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.229980
    dbObj.finalYear=1995.329956
    dbObj.country='USA'
    dbObj.designation='CGN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='TicoMk26.xml'
    dbObj.notes=''
    dbObj.length_m=219.839996
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Phalanx FC','SPG-55 4','SPS-10B','SPS-48C AS','SPS-49 AS','SQS-23 Active','SQS-23 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.075240
    dbObj.mfTurnRate_degps=1.095479
    dbObj.mfFuelCapacity_kg=2175600.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Long Beach CGN durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['Mk-10 GMLS','Mk-10 GMLS','20mm/76 M-61A1 Gatling Mark 15 Block 0','20mm/76 M-61A1 Gatling Mark 15 Block 0','5/38 Mark 12','5/38 Mark 12','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','Mk-112 ASROC','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Long beach Deck Gun Magazine','Phalanx 0 x2 Store','Mk-10 Store 120','Long Beach Torpedo Racks','Long Beach ASROC Reloads']
    dbObj.magazineId=[3,2,1,4,5]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','','','','']
    dbObj.launcherFOV_deg=[340.000000,310.000000,220.000000,340.000000,130.000000,130.000000,0.000000,0.000000,270.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,90.000000,270.000000,90.000000,270.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['SPG-55 4','SPG-55 4','Phalanx FC','Phalanx FC','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=52.417000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.146999
    airDetectionDBObject.irSignature_dB=13.823000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=13.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=30.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.320000
    dbObj.beam_m=21.790001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=80000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
