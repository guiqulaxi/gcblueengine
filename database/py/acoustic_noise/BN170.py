# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN170'
    dbObj.xSpeed_kts=[0.000000,6.820000,23.870001,34.099998]
    dbObj.ySL_dB=[91.500000,98.317001,146.036026,159.670029]
    dbObj.speedMinNL_kts=8.750000
    dbObj.NL_min=49.099998
    dbObj.speedMaxNL_kts=34.099998
    dbObj.NL_max=100.699997
    dbObj.cavitationOffset_kts=12.500000
    dbObj.cavitationSlope_ktsperft=0.009100
    dbObj.cavitationSL_dB=177.670029
    dbObj.snorkelingSL_dB=171.670029
    dbObj.BuildSLTable()
    return dbObj