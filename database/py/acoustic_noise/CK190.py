# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK190'
    dbObj.xSpeed_kts=[0.000000,4.720000,16.520000,23.600000]
    dbObj.ySL_dB=[90.019997,94.346657,124.633247,133.286560]
    dbObj.speedMinNL_kts=7.560000
    dbObj.NL_min=49.000000
    dbObj.speedMaxNL_kts=23.600000
    dbObj.NL_max=94.500000
    dbObj.cavitationOffset_kts=10.800000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=151.286560
    dbObj.snorkelingSL_dB=145.286560
    dbObj.BuildSLTable()
    return dbObj