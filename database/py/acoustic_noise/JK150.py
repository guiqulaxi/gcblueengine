# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK150'
    dbObj.xSpeed_kts=[0.000000,3.414000,11.949000,17.070000]
    dbObj.ySL_dB=[94.550003,98.561447,126.641602,134.664505]
    dbObj.speedMinNL_kts=7.910000
    dbObj.NL_min=51.580002
    dbObj.speedMaxNL_kts=17.070000
    dbObj.NL_max=99.000000
    dbObj.cavitationOffset_kts=11.300000
    dbObj.cavitationSlope_ktsperft=0.007620
    dbObj.cavitationSL_dB=152.664505
    dbObj.snorkelingSL_dB=146.664505
    dbObj.BuildSLTable()
    return dbObj