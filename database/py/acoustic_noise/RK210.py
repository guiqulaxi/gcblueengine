# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK210'
    dbObj.xSpeed_kts=[0.000000,5.920000,20.719999,29.600000]
    dbObj.ySL_dB=[83.699997,86.815170,108.621346,114.851685]
    dbObj.speedMinNL_kts=9.695000
    dbObj.NL_min=45.700001
    dbObj.speedMaxNL_kts=29.600000
    dbObj.NL_max=74.199997
    dbObj.cavitationOffset_kts=13.850000
    dbObj.cavitationSlope_ktsperft=0.013075
    dbObj.cavitationSL_dB=132.851685
    dbObj.snorkelingSL_dB=126.851685
    dbObj.BuildSLTable()
    return dbObj