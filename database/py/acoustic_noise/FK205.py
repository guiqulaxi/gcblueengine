# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK205'
    dbObj.xSpeed_kts=[0.000000,5.244000,18.354000,26.219999]
    dbObj.ySL_dB=[79.680000,83.904327,113.474609,121.923264]
    dbObj.speedMinNL_kts=8.680000
    dbObj.NL_min=44.880001
    dbObj.speedMaxNL_kts=26.219999
    dbObj.NL_max=86.040001
    dbObj.cavitationOffset_kts=12.400000
    dbObj.cavitationSlope_ktsperft=0.010880
    dbObj.cavitationSL_dB=139.923264
    dbObj.snorkelingSL_dB=133.923264
    dbObj.BuildSLTable()
    return dbObj