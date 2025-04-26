# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN200'
    dbObj.xSpeed_kts=[0.000000,8.160000,28.559999,40.799999]
    dbObj.ySL_dB=[82.699997,88.411278,128.390213,139.812759]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=45.490002
    dbObj.speedMaxNL_kts=40.799999
    dbObj.NL_max=87.449997
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.010390
    dbObj.cavitationSL_dB=157.812759
    dbObj.snorkelingSL_dB=151.812759
    dbObj.BuildSLTable()
    return dbObj