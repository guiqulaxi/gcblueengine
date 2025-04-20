import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 12322 Zubr'
    dbObj.natoClass='Pomornik'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=550000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1988.770020
    dbObj.finalYear=2011.000000
    dbObj.country='Russia'
    dbObj.designation='LCJ'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=57.299999
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Curl Stone SS','ESM-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=63.000000
    dbObj.mfAccel_ktsps=0.357851
    dbObj.mfTurnRate_degps=6.767025
    dbObj.mfFuelCapacity_kg=77000.000000
    dbObj.mfFuelRate_kgps=1.752053
    dbObj.mfToughness=17.000000
    dbObj.damageEffect='Pr 12322 Zubr durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','SA-N-5 x4 launcher x2']
    dbObj.maMagazineClass=['AK-630 x2 Store','Strela2 x16 Mag']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=30.650999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.709000
    airDetectionDBObject.irSignature_dB=26.149000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=3.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S13.HoverCraft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.600000
    dbObj.beam_m=25.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=30000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
