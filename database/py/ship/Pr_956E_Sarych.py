import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 956E Sarych'
    dbObj.natoClass='Sovremenny E'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=1000000000.000000
    dbObj.weight_kg=6200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1999.989990
    dbObj.finalYear=2999.989990
    dbObj.country='China'
    dbObj.designation='DDG'
    dbObj.imageList='sovremenny-1.jpg;sovremenny-4.jpg;sovremenny-5.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=156.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Foot Ball ESM','MG-335 Platina Active','MG-335 Platina Passive','MP-407E ECM','MR-105 (Port)','MR-105 (Stbd)','MR-184','MR-212 Nvada','MR-700A Fregat AS/SS','MR-90 Oriech FC (Port Array)','MR-90 Oriech FC (Stbd Array)']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,270.000000,90.000000,0.000000,0.000000,0.000000,270.000000,90.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.051931
    dbObj.mfTurnRate_degps=1.700457
    dbObj.mfFuelCapacity_kg=868000.000000
    dbObj.mfFuelRate_kgps=1.107133
    dbObj.mfToughness=300.000000
    dbObj.damageEffect='Pr 956E Sarych durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['130 mm/70 (5.1in) AK-130 Twin Barrel','130 mm/70 (5.1in) AK-130 Twin Barrel','SS-N-22 x4 Launcher x2','SA-N-12 Fore Rail','SA-N-12 Aft Rail','30 mm/54 (1.2in) AK-630M x2','30 mm/54 (1.2in) AK-630M x2','533mm torpedo x2 tubes','533mm torpedo x2 tubes','PK-10 Chaff Launcher x 5 (Port)','PK-10 Chaff Launcher x 5 (Stbd)']
    dbObj.maMagazineClass=['Sovremenny Helo Fuel Bunker','Sovremenny Torpedo Magazine','Sovremenny Gun/CM Magazine','Ship Helo Stores']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['Fore 130mm Guns','Aft 130mm Guns','','SA-N-12 Fore Rail','SA-N-12 Aft Rail','Port 30mm CIWS Mounts','Stbd 30mm CIWS Mounts','Port Torpedo Tubes','Stbd Torpedo Tubes','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,0.000000,360.000000,360.000000,180.000000,180.000000,40.000000,40.000000,90.000000,90.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,0.000000,180.000000,270.000000,90.000000,270.000000,90.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,30.000000,45.000000,45.000000,0.000000,0.000000,0.000000,0.000000,60.000000,60.000000]
    dbObj.launcherFireControl=['MR-184','MR-184','MR-184','MR-90 Oriech FC (Stbd Array)','MR-90 Oriech FC (Port Array)','MR-105 (Port)','MR-105 (Port)','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=46.431999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.496000
    airDetectionDBObject.irSignature_dB=23.802999
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
    dbObj.draft_m=6.500000
    dbObj.beam_m=17.299999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=99500.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Sovremenny Hangar'
    dbObj.CalculateParams()
    return dbObj
