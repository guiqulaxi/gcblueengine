# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK170'
    dbObj.xSpeed_kts=[0.000000,3.870000,13.545000,19.350000]
    dbObj.ySL_dB=[88.400002,92.802322,123.618584,132.423233]
    dbObj.speedMinNL_kts=8.750000
    dbObj.NL_min=49.099998
    dbObj.speedMaxNL_kts=19.350000
    dbObj.NL_max=94.199997
    dbObj.cavitationOffset_kts=12.500000
    dbObj.cavitationSlope_ktsperft=0.010100
    dbObj.cavitationSL_dB=150.423233
    dbObj.snorkelingSL_dB=144.423233
    dbObj.BuildSLTable()
    return dbObj