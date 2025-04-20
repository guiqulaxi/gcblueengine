import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Isuzu DDE'
    dbObj.natoClass='Isuzu DDE'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1700000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1961.491943
    dbObj.finalYear=1993.875000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=94.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['BLR-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','OPS-1','OPS-16','OQS-14 Active','SPG-34']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=26.000000
    dbObj.mfAccel_ktsps=0.078793
    dbObj.mfTurnRate_degps=2.636992
    dbObj.mfFuelCapacity_kg=238000.000000
    dbObj.mfFuelRate_kgps=0.127324
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Isuzu DDE durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['3/50 Mark 27 Twin','3/50 Mark 27 Twin','533mm torpedo x4 tubes Japan','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','375mm Bofors ASRL','DC Rack 12']
    dbObj.maMagazineClass=['76mm mk33 Store','Japanese ASW Magazine','Japanese Ship Torpedo Racks']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,320.000000,270.000000,30.000000,30.000000,300.000000,10.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,90.000000,270.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=38.001999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=21.886999
    airDetectionDBObject.irSignature_dB=17.094999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.500000
    dbObj.beam_m=10.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=16000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
