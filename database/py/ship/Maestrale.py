import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Maestrale'
    dbObj.natoClass='Maestrale'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=3100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.180054
    dbObj.finalYear=2999.000000
    dbObj.country='Italy'
    dbObj.designation='FF'
    dbObj.imageList='maestrale.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes=''
    dbObj.length_m=122.699997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DE-1164 Active','DE-1164 Passive','ESM-2','RAN-10S','RTN-10XPx2','RTN-20X-2']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.235036
    dbObj.mfTurnRate_degps=2.274987
    dbObj.mfFuelCapacity_kg=434000.000000
    dbObj.mfFuelRate_kgps=0.301386
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Maestrale durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['127 mm/54 (5in) Compact','Albatross Launcher','Otomat Launcher x4','40 mm 2xL70 Bofors','40 mm 2xL70 Bofors','ILAS-3 Triple Torpedo Tube','ILAS-3 Triple Torpedo Tube','533 mm Torpedo Tube Maestrale','533 mm Torpedo Tube Maestrale','SCLAR Rocket Launcher','SCLAR Rocket Launcher']
    dbObj.maMagazineClass=['Fuel depot','Ship stores','Ship stores']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','CIWS','CIWS','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,320.000000,160.000000,160.000000,40.000000,40.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,270.000000,90.000000,90.000000,270.000000,315.000000,45.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[30.000000,30.000000,0.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,30.000000,30.000000]
    dbObj.launcherFireControl=['','RTN-10XPx2','','RTN-20X-2','RTN-20X-2','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.916000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.999001
    airDetectionDBObject.irSignature_dB=23.612000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.200000
    dbObj.beam_m=12.900000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=61000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
