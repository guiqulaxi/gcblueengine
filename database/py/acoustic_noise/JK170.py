# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK170'
    dbObj.xSpeed_kts=[0.000000,4.270000,14.945000,21.350000]
    dbObj.ySL_dB=[88.750000,92.667213,120.087700,127.922127]
    dbObj.speedMinNL_kts=8.750000
    dbObj.NL_min=49.099998
    dbObj.speedMaxNL_kts=21.350000
    dbObj.NL_max=94.199997
    dbObj.cavitationOffset_kts=12.500000
    dbObj.cavitationSlope_ktsperft=0.010100
    dbObj.cavitationSL_dB=145.922134
    dbObj.snorkelingSL_dB=139.922134
    dbObj.BuildSLTable()
    return dbObj