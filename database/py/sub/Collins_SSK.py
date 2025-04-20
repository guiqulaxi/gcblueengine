import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Collins SSK'
    dbObj.natoClass='Collins SSK'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=3051000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1996.567383
    dbObj.finalYear=2999.997314
    dbObj.country='Australia'
    dbObj.designation='SSK'
    dbObj.imageList='collins.jpg;collins2.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='zwaardvis.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ES-3701 ESM','Kariwarra Towed Array Sonar','Scylla Active','Scylla Bow Passive','Scylla Port Flank Passive','Scylla Stbd Flank Passive','Type 1007(s)','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,270.000000,90.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=600000.000000
    dbObj.mfFuelRate_kgps=0.500000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Collins SSK durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['533mm Collins Torpedo Tube','533mm Collins Torpedo Tube','533mm Collins Torpedo Tube','533mm Collins Torpedo Tube','533mm Collins Torpedo Tube','533mm Collins Torpedo Tube','Collins CM Launcher','Collins CM Launcher']
    dbObj.maMagazineClass=['Collins Torpedo Racks','Collins Missile Racks']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','Tube 5','Tube 6','CM1','CM2']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.800000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.800000
    airDetectionDBObject.irSignature_dB=7.800000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=5.849000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='BK195'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.000000
    dbObj.surfaceSpeed_kts=10.500000
    dbObj.mfMaxDepth_m=275.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=2.000000
    dbObj.CalculateParams()
    return dbObj
