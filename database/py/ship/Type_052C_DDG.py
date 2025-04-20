import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 052C DDG'
    dbObj.natoClass='Luyang II'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=7000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2004.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='DDG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42_temp.xml'
    dbObj.notes=''
    dbObj.length_m=155.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['30N6E','Decca 1226','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SJD-8 Active','SJD-9 Passive','Type 344','Type 347','Type 364','Type 382','Type 517h-1','Type 826','Type 984-1/2']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.143607
    dbObj.mfTurnRate_degps=1.533335
    dbObj.mfFuelCapacity_kg=980000.000000
    dbObj.mfFuelRate_kgps=0.846906
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 052C DDG durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['YJ-83 x8','YJ-83 x8','100mm/56 Type-79A Twin-mount','HQ-9 x48 VLS','30 mm/92(1/2in) Type 730 CIWS','30 mm/92(1/2in) Type 730 CIWS','324mm Torpedo Tube x3 (China)','324mm Torpedo Tube x3 (China)']
    dbObj.maMagazineClass=['Z-9C 2.2 Support','Type 730 Ciws x2 Magazine','100mm/56 Type 79A Magazine 300 Rounds']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[240.000000,240.000000,320.000000,320.000000,170.000000,170.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,90.000000,270.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,40.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','30N6E','Type 347','Type 347','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=47.222000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.313000
    airDetectionDBObject.irSignature_dB=21.740999
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
    dbObj.draft_m=6.000000
    dbObj.beam_m=17.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=57440.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
