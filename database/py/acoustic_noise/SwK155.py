# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK155'
    dbObj.xSpeed_kts=[0.000000,3.224000,11.284000,16.120001]
    dbObj.ySL_dB=[92.300003,96.625839,126.906731,135.558411]
    dbObj.speedMinNL_kts=8.190000
    dbObj.NL_min=50.959999
    dbObj.speedMaxNL_kts=16.120001
    dbObj.NL_max=97.699997
    dbObj.cavitationOffset_kts=11.700000
    dbObj.cavitationSlope_ktsperft=0.008360
    dbObj.cavitationSL_dB=153.558411
    dbObj.snorkelingSL_dB=147.558411
    dbObj.BuildSLTable()
    return dbObj