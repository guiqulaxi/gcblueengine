# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Rubis'
    dbObj.xSpeed_kts=[0.000000,7.500000,20.000000,25.000000]
    dbObj.ySL_dB=[90.699997,98.889999,115.000000,149.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=50.500000
    dbObj.speedMaxNL_kts=24.000000
    dbObj.NL_max=103.000000
    dbObj.cavitationOffset_kts=12.520000
    dbObj.cavitationSlope_ktsperft=0.021000
    dbObj.cavitationSL_dB=169.199997
    dbObj.snorkelingSL_dB=161.000000
    dbObj.BuildSLTable()
    return dbObj