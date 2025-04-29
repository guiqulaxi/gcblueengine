# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN165'
    dbObj.xSpeed_kts=[0.000000,6.560000,22.959999,32.799999]
    dbObj.ySL_dB=[93.199997,100.358421,150.467392,164.784241]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=49.720001
    dbObj.speedMaxNL_kts=32.799999
    dbObj.NL_max=103.000000
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.008480
    dbObj.cavitationSL_dB=182.784241
    dbObj.snorkelingSL_dB=176.784241
    dbObj.BuildSLTable()
    return dbObj