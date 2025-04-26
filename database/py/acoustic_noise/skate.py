# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='skate'
    dbObj.xSpeed_kts=[0.000000,5.400000,14.400000,18.000000]
    dbObj.ySL_dB=[98.099998,128.460007,155.000000,171.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=51.900002
    dbObj.speedMaxNL_kts=18.000000
    dbObj.NL_max=101.500000
    dbObj.cavitationOffset_kts=9.770000
    dbObj.cavitationSlope_ktsperft=0.019000
    dbObj.cavitationSL_dB=177.500000
    dbObj.snorkelingSL_dB=183.000000
    dbObj.BuildSLTable()
    return dbObj