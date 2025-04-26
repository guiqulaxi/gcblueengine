# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK210'
    dbObj.xSpeed_kts=[0.000000,5.582000,19.537001,27.910000]
    dbObj.ySL_dB=[77.230003,80.975784,107.196304,114.687881]
    dbObj.speedMinNL_kts=11.340000
    dbObj.NL_min=44.400002
    dbObj.speedMaxNL_kts=27.910000
    dbObj.NL_max=84.599998
    dbObj.cavitationOffset_kts=16.200001
    dbObj.cavitationSlope_ktsperft=0.013150
    dbObj.cavitationSL_dB=132.687881
    dbObj.snorkelingSL_dB=126.687881
    dbObj.BuildSLTable()
    return dbObj