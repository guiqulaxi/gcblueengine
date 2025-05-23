# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Oyashio'
    dbObj.natoClass='Oyashio'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=3500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1998.203979
    dbObj.finalYear=2999.997314
    dbObj.country='Japan'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes='Jane\'s Fighting Ships 2004-2005, Wikipedia, Conways fighting ships 45-90, Materiels of IJN(JMSDF)(http://homepage2.nifty.com/nishidah/e/d_index.htm), http://www.hazegray.org/worldnav/, http://www.navypedia.org/naval_balance/japan.htm'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Periscope-1','ZLA-7 ESM','ZPS-6 AS/SS','ZQQ-6 Active','ZQQ-6 Bow Passive','ZQQ-6 Port Flank Passive','ZQQ-6 Stbd Flank Passive','ZQR-1 TA']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,270.000000,90.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=21.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=490000.000000
    dbObj.mfFuelRate_kgps=0.610266
    dbObj.mfToughness=120.000000
    dbObj.damageEffect='Oyashio durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm Japanese Sub Tube','533mm Japanese Sub Tube','533mm Japanese Sub Tube','533mm Japanese Sub Tube','533mm Japanese Sub Tube','533mm Japanese Sub Tube']
    dbObj.maMagazineClass=['Sub 20']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=26.600000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.600000
    airDetectionDBObject.irSignature_dB=18.299999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=5.643000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='JK200'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.500000
    dbObj.surfaceSpeed_kts=13.000000
    dbObj.mfMaxDepth_m=350.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.251800
    dbObj.CalculateParams()
    return dbObj
