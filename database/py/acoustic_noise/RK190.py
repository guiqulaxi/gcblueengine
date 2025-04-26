# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK190'
    dbObj.xSpeed_kts=[0.000000,4.960000,17.360001,24.799999]
    dbObj.ySL_dB=[88.099998,91.414330,114.614632,121.243286]
    dbObj.speedMinNL_kts=8.435000
    dbObj.NL_min=47.700001
    dbObj.speedMaxNL_kts=24.799999
    dbObj.NL_max=82.199997
    dbObj.cavitationOffset_kts=12.050000
    dbObj.cavitationSlope_ktsperft=0.007875
    dbObj.cavitationSL_dB=139.243286
    dbObj.snorkelingSL_dB=133.243286
    dbObj.BuildSLTable()
    return dbObj