# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK185'
    dbObj.xSpeed_kts=[0.000000,4.720000,16.520000,23.600000]
    dbObj.ySL_dB=[89.199997,92.541115,115.928909,122.611137]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=48.200001
    dbObj.speedMaxNL_kts=23.600000
    dbObj.NL_max=84.199997
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.006575
    dbObj.cavitationSL_dB=140.611130
    dbObj.snorkelingSL_dB=134.611130
    dbObj.BuildSLTable()
    return dbObj