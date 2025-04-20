import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSimpleAirDBObject()
    dbObj.mzClass='Nimrod MR.2'
    dbObj.natoClass='Nimrod MR.2'
    dbObj.mnModelType=4
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=39009.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1979.000000
    dbObj.finalYear=2999.000000
    dbObj.country='UK'
    dbObj.designation='ASuW'
    dbObj.imageList='a330.jpg'
    dbObj.iconFileName='air/AdvicoNimrodR1.JPG'
    dbObj.mz3DModelFileName='civilairliner.xml'
    dbObj.notes='Alec Walker'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ALQ-210 ESM','AN/AAR-57 MAWS','ASQ-81 MAD','Eyeball 20/10','Eyeball 20/10b','Eyeball 20/10c','Search Water']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=498.000000
    dbObj.mfAccel_ktsps=5.000000
    dbObj.mfTurnRate_degps=4.000000
    dbObj.mfFuelCapacity_kg=37272.000000
    dbObj.mfFuelRate_kgps=0.941000
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Nimrod MR.2 durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['Nimrod Bay','Nimrod Flare','MCP10 CM','MCP10 CM','115 Buoy Launcher','115 Buoy Launcher','61 Buoy Launcher','Nimrod Wing','Nimrod Wing']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=15.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.510000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_L_H_HP_4_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-999.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTakeoffWeight_kg=87090.000000
    dbObj.maxAltitude_m=13411.000000
    dbObj.climbRate_mps=10.000000
    dbObj.gmax=2.000000
    dbObj.minimumRunway_m=2200.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=16.600000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=3600.000000
    dbObj.CalculateParams()
    return dbObj
