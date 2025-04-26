# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GW'
    dbObj.xSpeed_kts=[0.000000,8.500000,20.000000,25.000000]
    dbObj.ySL_dB=[96.800003,124.879997,146.000000,164.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=51.299999
    dbObj.speedMaxNL_kts=25.000000
    dbObj.NL_max=101.250000
    dbObj.cavitationOffset_kts=10.870000
    dbObj.cavitationSlope_ktsperft=0.020000
    dbObj.cavitationSL_dB=174.800003
    dbObj.snorkelingSL_dB=176.000000
    dbObj.BuildSLTable()
    return dbObj