# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Pr 885 Yasen'
    dbObj.natoClass='Graney'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=5900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2012.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='SSGN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','MGK-540 Active','MGK-540 Bow Passive','MRK-50 SS','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Pr 885 Yasen durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['SS-N-27 x8 VLS Launcher','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube','533mm Russian sub tube']
    dbObj.maMagazineClass=['Russian Torpedo Racking']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[360.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[90.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.900000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=5.900000
    airDetectionDBObject.irSignature_dB=9.900000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=11.313000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='RN210'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=10.000000
    dbObj.surfaceSpeed_kts=21.000000
    dbObj.mfMaxDepth_m=460.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=16.000000
    dbObj.CalculateParams()
    return dbObj
