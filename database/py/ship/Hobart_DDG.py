import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Hobart DDG'
    dbObj.natoClass='Hobart DDG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=6250000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2013.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Australia'
    dbObj.designation='DD'
    dbObj.imageList='hobart.jpg;hobart2.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-45.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=133.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ES-3701 ESM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Kariwarra Towed Array Sonar','SPG-62 (Aft)','SPG-62 (Fore)','SPY-1D','Spherion B Mod 5','VAMPIR IIRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.143838
    dbObj.mfTurnRate_degps=1.625100
    dbObj.mfFuelCapacity_kg=980000.000000
    dbObj.mfFuelRate_kgps=0.890901
    dbObj.mfToughness=685.000000
    dbObj.damageEffect='Hobart DDG durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['5/62 Mark 45 Mod 4','Hobart Mk-41 VLS Cells 1-12','Hobart Mk-41 VLS Cells 13-24','Hobart Mk-41 VLS Cells 25-36','Hobart Mk-41 VLS Cells 37-48','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-160 EDL x 4','Mk-137 SRBOC Launcher','Mk-137 SRBOC Launcher']
    dbObj.maMagazineClass=['Hobart Helo Fuel Bunker','Hobart Torpedo Magazine','Hobart Gun/CM Magazine','Ship Helo Stores']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,0.000000,0.000000,0.000000,0.000000,270.000000,45.000000,45.000000,360.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,270.000000,90.000000,0.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[0.000000,90.000000,90.000000,90.000000,90.000000,0.000000,0.000000,0.000000,0.000000,60.000000,60.000000]
    dbObj.launcherFireControl=['SPG-62 (Fore)','SPG-62 (Fore)','SPG-62 (Fore)','SPG-62 (Aft)','SPG-62 (Aft)','','','','','','']
    dbObj.launcherFireControl2=['VAMPIR IIRST','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.222000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.750000
    airDetectionDBObject.irSignature_dB=23.836000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.900000
    dbObj.beam_m=18.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=59568.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
