# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Tornado ADV (Saudi Arabia)'
    dbObj.natoClass='Tornado ADV (Saudi Arabia)'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=15000000.000000
    dbObj.weight_kg=14091.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1985.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Saudi Arabia'
    dbObj.designation='Fighter'
    dbObj.imageList='tornado_f3.jpg'
    dbObj.iconFileName='air/AdvicoTornadoADV.jpg'
    dbObj.mz3DModelFileName='f-4.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Airpass 24','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','ARI 18241 RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=1312.000000
    dbObj.mfAccel_ktsps=9.950000
    dbObj.mfTurnRate_degps=26.150000
    dbObj.mfFuelCapacity_kg=5090.000000
    dbObj.mfFuelRate_kgps=2.100000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Tornado ADV durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Tornado ADVs wing shoulder','Tornado F2 wing','Tornado F3 fuselage','27mm BK27-Cannon(180)','ALE-40 FD','ALE-40 CD']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=11.300000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=7.310000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_2_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_2_M0.85'
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
    dbObj.maxTakeoffWeight_kg=27951.000000
    dbObj.maxAltitude_m=18000.000000
    dbObj.climbRate_mps=170.500000
    dbObj.gmax=7.500000
    dbObj.minimumRunway_m=2500.000000
    dbObj.isCarrierCompatible=False
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=76800.000000
    dbObj.militaryThrustSpeedSlope=0.000000
    dbObj.mfAfterburnThrust_N=143000.000000
    dbObj.abThrustSpeedSlope=0.002500
    dbObj.mfAfterburnFuelRate_kgps=8.000000
    dbObj.mfCdpsub=1.100000
    dbObj.mfCdptran=2.000000
    dbObj.mfCdpsup=1.700000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=119.519997
    dbObj.stallSpeed_mps=50.000000
    dbObj.thrustTable=[1.000000,0.930000,0.850000,0.800000,0.760000,0.580000,0.300000,0.050000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[1.000000,1.000000,1.000000,0.750000,0.800000,1.000000,2.000000,5.000000,5.000000,5.000000]
    dbObj.CalculateParams()
    return dbObj
