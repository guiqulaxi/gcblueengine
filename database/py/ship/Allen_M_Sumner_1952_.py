import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Allen M Sumner(1952)'
    dbObj.natoClass='Allen M Sumner(1952)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3315000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1952.000000
    dbObj.finalYear=1953.000000
    dbObj.country='USA'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes='initially installed with SC-2, and SG radars.  Early 50\'s gains it the SPS-6, 1953 SG is replaced with SPS-10.  During FRAM II SPS-6 was replaced with SPS-40.  Initial Sonar was the QGA(3kyds-5kyds detection), FRAM II gained her SQS-4(up to 15kyds).  Winter 1962 added the VDS SQA-8, 600ft cable.  Late 1944 saw introduction of SPR-1 ESM, WLR-1 in 1960\'s.  makes her one of the earliest US ships found in GCB, with ESM of some sort.'
    dbObj.length_m=112.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','QHBa Active','SG','SPR-1 ESM','SPS-6']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=34.900002
    dbObj.mfAccel_ktsps=0.061473
    dbObj.mfTurnRate_degps=2.340637
    dbObj.mfFuelCapacity_kg=497250.000000
    dbObj.mfFuelRate_kgps=0.345310
    dbObj.mfToughness=126.099998
    dbObj.damageEffect='Allen M Sumner durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','Mk-14/15 Torpedo Mount','3/50 Mark 33','3/50 Mark 33','3/50 Mark 33','DC Rack 12','Kgun','Kgun']
    dbObj.maMagazineClass=['Sumner Secondary Magazine','Sumner Primary Magazine','Sumner Torpedo Racks']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','Rack','K-gun','K-gun']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,360.000000,200.000000,200.000000,200.000000,1.000000,1.000000,1.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,90.000000,40.000000,320.000000,180.000000,180.000000,150.000000,210.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True]
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
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
