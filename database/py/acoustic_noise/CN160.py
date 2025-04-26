# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN160'
    dbObj.xSpeed_kts=[0.000000,5.060000,17.709999,25.299999]
    dbObj.ySL_dB=[100.699997,109.428497,170.528000,187.985001]
    dbObj.speedMinNL_kts=5.670000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=25.299999
    dbObj.NL_max=106.500000
    dbObj.cavitationOffset_kts=8.100000
    dbObj.cavitationSlope_ktsperft=0.003000
    dbObj.cavitationSL_dB=205.985001
    dbObj.snorkelingSL_dB=199.985001
    dbObj.BuildSLTable()
    return dbObj