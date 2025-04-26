# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S01.Patrol Craft'
    dbObj.xSpeed_kts=[4.000000,15.000000,30.000000,60.000000]
    dbObj.ySL_dB=[108.000000,112.000000,124.000000,128.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=54.000000
    dbObj.speedMaxNL_kts=60.000000
    dbObj.NL_max=94.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj