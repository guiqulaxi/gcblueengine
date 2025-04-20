import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Agosta(Pakistan)'
    dbObj.natoClass='Agosta(Pakistan)'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=1740000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1979.103027
    dbObj.finalYear=2999.000000
    dbObj.country='Pakistan'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DRUA 33','DSUV 22 Active','DSUV 22 Bow Passive','DSUV 62C TA','ESM-1','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=17.500000
    dbObj.mfAccel_ktsps=1.300000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=243600.000000
    dbObj.mfFuelRate_kgps=0.181439
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Agosta(Pakistan) durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['533mm French Torpedo Tube','533mm French Torpedo Tube','533mm French Torpedo Tube','533mm French Torpedo Tube']
    dbObj.maMagazineClass=['Sub 20']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=9.000000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.000000
    airDetectionDBObject.irSignature_dB=7.000000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=6.360000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='FK175'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.500000
    dbObj.surfaceSpeed_kts=12.000000
    dbObj.mfMaxDepth_m=300.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.678680
    dbObj.CalculateParams()
    return dbObj
