# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcCounterMeasureDBObject()
    dbObj.mzClass='Mk-53 Nulka Hovering Decoy'
    dbObj.natoClass='Mk-53 Nulka Hovering Decoy'
    dbObj.mnModelType=16
    dbObj.mnType=36
    dbObj.cost=275000.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='nulkaico.jpg'
    dbObj.mz3DModelFileName='flare.xml'
    dbObj.notes='Contributed by greengills'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=40.000000
    airDetectionDBObject.RCS_Model='Isotropic'
    airDetectionDBObject.opticalCrossSection_dBsm=1.000000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='Isotropic'
    airDetectionDBObject.IR_ModelB='Isotropic'
    airDetectionDBObject.IR_ModelC='Isotropic'
    airDetectionDBObject.effectiveHeight_m=5.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-99.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.subType='Chaff'
    dbObj.lifeSpan_s=60.000000
    dbObj.effectiveness=0.600000
    dbObj.maxSpeed_mps=0.100000
    dbObj.CalculateParams()
    return dbObj
