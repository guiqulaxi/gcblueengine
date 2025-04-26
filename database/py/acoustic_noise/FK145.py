# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK145'
    dbObj.xSpeed_kts=[0.000000,2.700000,9.450000,13.500000]
    dbObj.ySL_dB=[96.000000,100.455002,131.639999,140.550003]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=13.500000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=10.000000
    dbObj.cavitationSlope_ktsperft=0.005000
    dbObj.cavitationSL_dB=158.550003
    dbObj.snorkelingSL_dB=152.550003
    dbObj.BuildSLTable()
    return dbObj