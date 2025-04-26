# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN195'
    dbObj.xSpeed_kts=[0.000000,7.920000,27.719999,39.599998]
    dbObj.ySL_dB=[83.000000,88.160538,124.284279,134.605347]
    dbObj.speedMinNL_kts=10.500000
    dbObj.NL_min=46.200001
    dbObj.speedMaxNL_kts=39.599998
    dbObj.NL_max=90.199997
    dbObj.cavitationOffset_kts=15.000000
    dbObj.cavitationSlope_ktsperft=0.011500
    dbObj.cavitationSL_dB=152.605347
    dbObj.snorkelingSL_dB=146.605347
    dbObj.BuildSLTable()
    return dbObj