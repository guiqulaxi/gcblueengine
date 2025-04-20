import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Akizuki DD'
    dbObj.natoClass='Akizuki DD'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2890000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1960.119019
    dbObj.finalYear=1976.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=134.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','OPS-1','OPS-15','SQS-23 Active','SQS-23 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.212413
    dbObj.mfTurnRate_degps=2.242460
    dbObj.mfFuelCapacity_kg=404600.000000
    dbObj.mfFuelRate_kgps=0.399601
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Akizuki DD durability'
    dbObj.mnNumLaunchers=12
    dbObj.maLauncherClass=['5/54 Mark 16','5/54 Mark 16','5/54 Mark 16','3/50 Mark 27 Twin','3/50 Mark 27 Twin','533mm torpedo tube Japan','533mm torpedo tube Japan','Weapon Alfa','Hedgehog','Hedgehog','Ygun','Ygun']
    dbObj.maMagazineClass=['127mm mk12/16 900 round','76mm mk33 Store','Japanese ASW Magazine','Japanese Ship Torpedo Racks','Weapon Alfa Reloads']
    dbObj.magazineId=[0,1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11]
    dbObj.launcherName=['','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,320.000000,320.000000,340.000000,0.000000,0.000000,270.000000,10.000000,10.000000,10.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,180.000000,0.000000,180.000000,20.000000,340.000000,0.000000,0.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.459000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.018000
    airDetectionDBObject.irSignature_dB=20.480000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.150000
    dbObj.beam_m=11.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=52000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
