# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 667'
    dbObj.xSpeed_kts=[0.000000,7.800000,20.799999,26.000000]
    dbObj.ySL_dB=[98.500000,117.519997,158.899994,165.000000]
    dbObj.speedMinNL_kts=6.000000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=27.000000
    dbObj.NL_max=101.000000
    dbObj.cavitationOffset_kts=11.510000
    dbObj.cavitationSlope_ktsperft=0.017000
    dbObj.cavitationSL_dB=175.199997
    dbObj.snorkelingSL_dB=177.000000
    dbObj.BuildSLTable()
    return dbObj