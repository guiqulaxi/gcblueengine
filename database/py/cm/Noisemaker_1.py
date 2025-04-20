import pygcb
def CreateDBObject():
    dbObj=pygcb.tcCounterMeasureDBObject()
    dbObj.mzClass='Noisemaker-1'
    dbObj.natoClass='Noisemaker-1'
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
    dbObj.notes=''
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
    waterDetectionDBObject.TS=0.000000
    waterDetectionDBObject.TS_Model='Isotropic'
    waterDetectionDBObject.acousticModel='Noisemaker 180'
    waterDetectionDBObject.SL_Model='Isotropic'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.subType='Noisemaker'
    dbObj.lifeSpan_s=3000.000000
    dbObj.effectiveness=99.000000
    dbObj.maxSpeed_mps=0.100000
    dbObj.CalculateParams()
    return dbObj
