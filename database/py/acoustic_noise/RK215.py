# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK215'
    dbObj.xSpeed_kts=[0.000000,6.160000,21.559999,30.799999]
    dbObj.ySL_dB=[82.599998,85.647644,106.981133,113.076416]
    dbObj.speedMinNL_kts=10.010000
    dbObj.NL_min=45.200001
    dbObj.speedMaxNL_kts=30.799999
    dbObj.NL_max=72.199997
    dbObj.cavitationOffset_kts=14.300000
    dbObj.cavitationSlope_ktsperft=0.014375
    dbObj.cavitationSL_dB=131.076416
    dbObj.snorkelingSL_dB=125.076416
    dbObj.BuildSLTable()
    return dbObj