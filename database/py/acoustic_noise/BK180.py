# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK180'
    dbObj.xSpeed_kts=[0.000000,4.298000,15.043000,21.490000]
    dbObj.ySL_dB=[85.760002,90.080093,120.320740,128.960922]
    dbObj.speedMinNL_kts=9.170000
    dbObj.NL_min=47.860001
    dbObj.speedMaxNL_kts=21.490000
    dbObj.NL_max=91.800003
    dbObj.cavitationOffset_kts=13.100000
    dbObj.cavitationSlope_ktsperft=0.011340
    dbObj.cavitationSL_dB=146.960922
    dbObj.snorkelingSL_dB=140.960922
    dbObj.BuildSLTable()
    return dbObj