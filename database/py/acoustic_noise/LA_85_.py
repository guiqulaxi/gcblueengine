# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='LA(85)'
    dbObj.xSpeed_kts=[0.000000,9.600000,25.600000,32.000000]
    dbObj.ySL_dB=[87.900002,94.230003,106.000000,126.000000]
    dbObj.speedMinNL_kts=9.000000
    dbObj.NL_min=49.500000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=99.500000
    dbObj.cavitationOffset_kts=12.880000
    dbObj.cavitationSlope_ktsperft=0.028000
    dbObj.cavitationSL_dB=162.899994
    dbObj.snorkelingSL_dB=138.000000
    dbObj.BuildSLTable()
    return dbObj