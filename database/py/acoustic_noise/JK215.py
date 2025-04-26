# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK215'
    dbObj.xSpeed_kts=[0.000000,6.196000,21.686001,30.980000]
    dbObj.ySL_dB=[75.699997,78.956955,101.755615,108.269524]
    dbObj.speedMinNL_kts=10.640000
    dbObj.NL_min=43.520000
    dbObj.speedMaxNL_kts=30.980000
    dbObj.NL_max=83.400002
    dbObj.cavitationOffset_kts=15.200000
    dbObj.cavitationSlope_ktsperft=0.015680
    dbObj.cavitationSL_dB=126.269524
    dbObj.snorkelingSL_dB=120.269524
    dbObj.BuildSLTable()
    return dbObj