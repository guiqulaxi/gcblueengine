# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN145'
    dbObj.xSpeed_kts=[0.000000,5.520000,19.320000,27.600000]
    dbObj.ySL_dB=[100.000000,108.279999,166.240005,182.800003]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=27.600000
    dbObj.NL_max=112.199997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=200.800003
    dbObj.snorkelingSL_dB=194.800003
    dbObj.BuildSLTable()
    return dbObj