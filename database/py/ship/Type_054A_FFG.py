# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 054A FFG'
    dbObj.natoClass='Type 054A FFG'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=4053000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2008.072021
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='FFG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='cn_type-054a_jiangkai-ii.xml'
    dbObj.notes=''
    dbObj.length_m=134.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-335 Platina Active','MG-335 Platina Passive','MR-755 Fregat MAE-5','TR47C','Type 344','Type 345 4','Type 362','Type 826','Type 985-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.064503
    dbObj.mfTurnRate_degps=1.940495
    dbObj.mfFuelCapacity_kg=602000.000000
    dbObj.mfFuelRate_kgps=0.394038
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Type 054A FFG durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['YJ-83 Quad Launcher','YJ-83 Quad Launcher','HQ-16 VLS x36','30 mm/92(1/2in) Type 730 CIWS','30 mm/92(1/2in) Type 730 CIWS','76 mm/59 (3in) AK-176','324mm Torpedo Tube x3 (China)','324mm Torpedo Tube x3 (China)']
    dbObj.maMagazineClass=['Z-9C 1.2 Support','Type 730 Ciws x2 Magazine','76mm AK-176 Magazine 152 Rounds']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[2,1,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,170.000000,170.000000,320.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,90.000000,270.000000,0.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,90.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type 344','Type 344','Type 345 4','TR47C','TR47C','Type 344','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=33.661999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.070999
    airDetectionDBObject.irSignature_dB=18.423000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.000000
    dbObj.beam_m=15.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=28200.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
