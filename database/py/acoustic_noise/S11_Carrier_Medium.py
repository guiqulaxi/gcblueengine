# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S11.Carrier Medium'
    dbObj.xSpeed_kts=[3.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[109.500000,115.440002,133.259995,139.199997]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=55.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=95.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj