# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK180'
    dbObj.xSpeed_kts=[0.000000,4.284000,14.994000,21.420000]
    dbObj.ySL_dB=[85.550003,89.723869,118.940979,127.288727]
    dbObj.speedMinNL_kts=9.415000
    dbObj.NL_min=47.860001
    dbObj.speedMaxNL_kts=21.420000
    dbObj.NL_max=91.449997
    dbObj.cavitationOffset_kts=13.450000
    dbObj.cavitationSlope_ktsperft=0.011760
    dbObj.cavitationSL_dB=145.288727
    dbObj.snorkelingSL_dB=139.288727
    dbObj.BuildSLTable()
    return dbObj