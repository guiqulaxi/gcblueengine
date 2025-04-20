import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Allen M Sumner(Colombia)'
    dbObj.natoClass='Allen M Sumner(Colombia)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3315000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.829956
    dbObj.finalYear=1986.000000
    dbObj.country='Colombia'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes='initially installed with SC-2, and SG radars.  Early 50\'s gains it the SPS-6, 1953 SG is replaced with SPS-10.  During FRAM II SPS-6 was replaced with SPS-40.  Initial Sonar was the QGA(3kyds-5kyds detection), FRAM II gained her SQS-4(up to 15kyds).  Winter 1962 added the VDS SQA-8, 600ft cable.  Late 1944 saw introduction of SPR-1 ESM, WLR-1 in 1960\'s.  makes her one of the earliest US ships found in GCB, with ESM of some sort.'
    dbObj.length_m=112.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPR-1 ESM','SPS-10','SPS-6','SQA-8 VDS','SQS-4 Active']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=34.900002
    dbObj.mfAccel_ktsps=0.061473
    dbObj.mfTurnRate_degps=2.340637
    dbObj.mfFuelCapacity_kg=497250.000000
    dbObj.mfFuelRate_kgps=0.345310
    dbObj.mfToughness=126.099998
    dbObj.damageEffect='Allen M Sumner durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Sumner Primary Magazine','DASH Support Stores']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=42.353001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.864000
    airDetectionDBObject.irSignature_dB=24.597000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.800000
    dbObj.beam_m=12.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
