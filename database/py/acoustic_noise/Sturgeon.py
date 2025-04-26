# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Sturgeon'
    dbObj.xSpeed_kts=[0.000000,8.400000,22.400000,28.000000]
    dbObj.ySL_dB=[94.199997,105.839996,130.000000,146.000000]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=50.750000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=100.750000
    dbObj.cavitationOffset_kts=11.810000
    dbObj.cavitationSlope_ktsperft=0.022000
    dbObj.cavitationSL_dB=168.199997
    dbObj.snorkelingSL_dB=158.000000
    dbObj.BuildSLTable()
    return dbObj