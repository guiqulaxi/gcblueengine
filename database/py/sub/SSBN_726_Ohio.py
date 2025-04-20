import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='SSBN 726 Ohio'
    dbObj.natoClass='SSBN 726 Ohio'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=1000000000.000000
    dbObj.weight_kg=16600000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.860352
    dbObj.finalYear=2999.997314
    dbObj.country='USA'
    dbObj.designation='SSBN'
    dbObj.imageList='ohio-1.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='ohio.xml'
    dbObj.notes='Renamed from Ohio SSBN to just Ohio. Going to name SSGN conversion as Ohio SSGN (2008)'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['BPS-15F','BQQ-6 Bow Passive','BQQ-6 Port Flank Passive','BQQ-6 Stbd Flank Passive','BQS-13 Active','Periscope-1','TB-23 TA','WLR-8 ESM']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,270.000000,90.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=1.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=150.000000
    dbObj.damageEffect='SSBN 726 Ohio durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['533mm Ohio Tube','533mm Ohio Tube','533mm Ohio Tube','533mm Ohio Tube','CSA Mk1','CSA Mk1','Ohio SLBM Tubes']
    dbObj.maMagazineClass=['Ohio Torpedo Room']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','CM','CM','SLBM']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,45.000000,315.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,90.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=15.300000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=9.300000
    airDetectionDBObject.irSignature_dB=13.300000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.755000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='AN180'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=11.500000
    dbObj.surfaceSpeed_kts=21.000000
    dbObj.mfMaxDepth_m=290.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=0.000000
    dbObj.batteryCharge_kW=0.000000
    dbObj.CalculateParams()
    return dbObj
