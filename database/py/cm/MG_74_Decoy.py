# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcCounterMeasureDBObject()
    dbObj.mzClass='MG-74 Decoy'
    dbObj.natoClass='MG-74 Decoy'
    dbObj.mnModelType=22
    dbObj.mnType=136
    dbObj.cost=10000.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.500000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='cm.jpg'
    dbObj.mz3DModelFileName='buoy.xml'
    dbObj.notes='operating depth is 20 m to 250 m but no currently no depth fields in CM table. Described as noise simulation decoy'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-99.000000
    airDetectionDBObject.RCS_Model='Isotropic'
    airDetectionDBObject.opticalCrossSection_dBsm=0.000000
    airDetectionDBObject.irSignature_dB=20.000000
    airDetectionDBObject.IR_ModelA='Isotropic'
    airDetectionDBObject.IR_ModelB='Isotropic'
    airDetectionDBObject.IR_ModelC='Isotropic'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Noisemaker 130'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.subType='Decoy'
    dbObj.lifeSpan_s=1800.000000
    dbObj.effectiveness=0.100000
    dbObj.maxSpeed_mps=14.000000
    dbObj.CalculateParams()
    return dbObj
