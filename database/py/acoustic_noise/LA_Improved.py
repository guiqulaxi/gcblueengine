# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='LA Improved'
    dbObj.xSpeed_kts=[0.000000,9.600000,25.600000,32.000000]
    dbObj.ySL_dB=[86.699997,92.489998,103.000000,123.000000]
    dbObj.speedMinNL_kts=10.000000
    dbObj.NL_min=48.500000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=98.500000
    dbObj.cavitationOffset_kts=13.180000
    dbObj.cavitationSlope_ktsperft=0.029000
    dbObj.cavitationSL_dB=162.300003
    dbObj.snorkelingSL_dB=135.000000
    dbObj.BuildSLTable()
    return dbObj