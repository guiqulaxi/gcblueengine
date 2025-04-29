# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK145'
    dbObj.xSpeed_kts=[0.000000,2.800000,9.800000,14.000000]
    dbObj.ySL_dB=[98.000000,102.199997,131.600006,140.000000]
    dbObj.speedMinNL_kts=5.600000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=14.000000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=8.000000
    dbObj.cavitationSlope_ktsperft=0.003000
    dbObj.cavitationSL_dB=158.000000
    dbObj.snorkelingSL_dB=152.000000
    dbObj.BuildSLTable()
    return dbObj