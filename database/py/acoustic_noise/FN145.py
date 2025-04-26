# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN145'
    dbObj.xSpeed_kts=[0.000000,5.520000,19.320000,27.600000]
    dbObj.ySL_dB=[102.500000,111.608002,175.363998,193.580002]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=27.600000
    dbObj.NL_max=112.199997
    dbObj.cavitationOffset_kts=10.000000
    dbObj.cavitationSlope_ktsperft=0.005000
    dbObj.cavitationSL_dB=211.580002
    dbObj.snorkelingSL_dB=205.580002
    dbObj.BuildSLTable()
    return dbObj