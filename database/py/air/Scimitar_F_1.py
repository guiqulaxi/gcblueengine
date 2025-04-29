# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='Scimitar F.1'
    dbObj.natoClass='Scimitar F.1'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=10869.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1957.000000
    dbObj.finalYear=1970.000000
    dbObj.country='UK'
    dbObj.designation='Strike Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoScimitarF1.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Airpass 3','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f','Sky Guardian RWR']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=650.000000
    dbObj.mfAccel_ktsps=22.389999
    dbObj.mfTurnRate_degps=20.000000
    dbObj.mfFuelCapacity_kg=1955.000000
    dbObj.mfFuelRate_kgps=1.409000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='Scimitar F.1 durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['30mm Aden 150rnd','30mm Aden 150rnd','30mm Aden 150rnd','30mm Aden 150rnd','Scimitar 1-2-3-4','Scimitar 1-2-3-4']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[20.000000,20.000000,20.000000,20.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.300000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_1_M0.85'
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
    dbObj.maxTakeoffWeight_kg=15513.000000
    dbObj.maxAltitude_m=14700.000000
    dbObj.climbRate_mps=10.000000
    dbObj.gmax=3.500000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=100200.000000
    dbObj.militaryThrustSpeedSlope=0.002000
    dbObj.mfAfterburnThrust_N=100200.000000
    dbObj.abThrustSpeedSlope=0.002000
    dbObj.mfAfterburnFuelRate_kgps=1.409000
    dbObj.mfCdpsub=0.950000
    dbObj.mfCdptran=1.900000
    dbObj.mfCdpsup=2.850000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=90.000000
    dbObj.stallSpeed_mps=45.000000
    dbObj.thrustTable=[1.000000,1.000000,0.850000,0.700000,0.550000,0.400000,0.050000,0.030000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[0.980000,0.950000,0.900000,0.950000,1.100000,1.500000,3.000000,10.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
