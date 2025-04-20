import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Commandant Riviere FF'
    dbObj.natoClass='Commandant Riviere FF'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2250000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.496948
    dbObj.finalYear=1998.000000
    dbObj.country='France'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=103.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DRBC 31D','DRBV 22','DRBV 50','DUBV-23 Active','DUBV-43 VDS Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.140761
    dbObj.mfTurnRate_degps=2.301902
    dbObj.mfFuelCapacity_kg=315000.000000
    dbObj.mfFuelRate_kgps=0.186665
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Commandant Riviere FF durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['100mm/53 (3.9in) model 1953','100mm/53 (3.9in) model 1953','100mm/53 (3.9in) model 1953','40mm L70 Sea Trinity','40mm L70 Sea Trinity','533mm French L Torp Tubes x3','533mm French L Torp Tubes x3']
    dbObj.maMagazineClass=['100mm/55 Model 1953 1800 Rounds','40mm L70 Trinity x2 Magazine','L Torpedo Racks 12 rounds']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,300.000000,280.000000,165.000000,165.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,180.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['DRBC 31D','DRBC 31D','DRBC 31D','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=39.827999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.415001
    airDetectionDBObject.irSignature_dB=17.965000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=15.700000
    dbObj.beam_m=11.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=16000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
