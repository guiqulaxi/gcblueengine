# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN195'
    dbObj.xSpeed_kts=[0.000000,7.920000,27.719999,39.599998]
    dbObj.ySL_dB=[84.500000,90.492752,132.442032,144.427536]
    dbObj.speedMinNL_kts=8.400000
    dbObj.NL_min=46.099998
    dbObj.speedMaxNL_kts=39.599998
    dbObj.NL_max=89.699997
    dbObj.cavitationOffset_kts=12.000000
    dbObj.cavitationSlope_ktsperft=0.009900
    dbObj.cavitationSL_dB=162.427536
    dbObj.snorkelingSL_dB=156.427536
    dbObj.BuildSLTable()
    return dbObj