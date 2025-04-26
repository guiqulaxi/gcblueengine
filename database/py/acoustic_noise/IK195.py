# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK195'
    dbObj.xSpeed_kts=[0.000000,4.820000,16.870001,24.100000]
    dbObj.ySL_dB=[82.599998,86.688896,115.311172,123.488968]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=46.099998
    dbObj.speedMaxNL_kts=24.100000
    dbObj.NL_max=88.099998
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.010700
    dbObj.cavitationSL_dB=141.488968
    dbObj.snorkelingSL_dB=135.488968
    dbObj.BuildSLTable()
    return dbObj