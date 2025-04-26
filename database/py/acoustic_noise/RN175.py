# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN175'
    dbObj.xSpeed_kts=[0.000000,6.960000,24.360001,34.799999]
    dbObj.ySL_dB=[93.199997,101.371994,158.575928,174.919907]
    dbObj.speedMinNL_kts=7.490000
    dbObj.NL_min=49.200001
    dbObj.speedMaxNL_kts=34.799999
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=10.700000
    dbObj.cavitationSlope_ktsperft=0.004950
    dbObj.cavitationSL_dB=192.919907
    dbObj.snorkelingSL_dB=186.919907
    dbObj.BuildSLTable()
    return dbObj