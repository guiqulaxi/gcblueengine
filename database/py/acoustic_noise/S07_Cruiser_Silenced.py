# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S07.Cruiser Silenced'
    dbObj.xSpeed_kts=[7.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[104.000000,108.400002,121.599998,126.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=53.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=93.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj