# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S001.Merchant Small'
    dbObj.xSpeed_kts=[2.000000,9.000000,18.000000,36.000000]
    dbObj.ySL_dB=[109.500000,118.000000,135.500000,144.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=60.000000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj