import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Sachsen FFGHM'
    dbObj.natoClass='Sachsen FFGHM'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=5600000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2004.750000
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=143.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APAR','DSQS-21BZ Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SMART-L']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.162156
    dbObj.mfTurnRate_degps=1.685347
    dbObj.mfFuelCapacity_kg=784000.000000
    dbObj.mfFuelRate_kgps=0.979992
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Sachsen FFGHM durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['Mk-41 Mod10 VLS','Mk-41 Mod10 VLS','RIM-116A RAM x21','RIM-116A RAM x21','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','76 mm/62 Mark 75','27mm MLG 27','27mm MLG 27','Eurotorp TLS Launcher x3','Eurotorp TLS Launcher x3']
    dbObj.maMagazineClass=['Lynx 2.2 Support','Mk-41 VLS Mod10 32 Cell','RIM-116 21 x2 Store','76mm/62 mk75 240 rounds','27mm MLG 27 x2 Store']
    dbObj.magazineId=[0,1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,330.000000,330.000000,30.000000,30.000000,300.000000,170.000000,170.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,160.000000,200.000000,90.000000,270.000000,0.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,90.000000,40.000000,40.000000,20.000000,20.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['APAR','APAR','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=35.768002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.056000
    airDetectionDBObject.irSignature_dB=16.621000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.000000
    dbObj.beam_m=17.440001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=51642.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
