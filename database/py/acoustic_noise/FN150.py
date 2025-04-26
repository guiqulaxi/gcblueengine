# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN150'
    dbObj.xSpeed_kts=[0.000000,5.760000,20.160000,28.799999]
    dbObj.ySL_dB=[100.699997,109.491203,171.029602,188.612000]
    dbObj.speedMinNL_kts=7.140000
    dbObj.NL_min=51.590000
    dbObj.speedMaxNL_kts=28.799999
    dbObj.NL_max=109.949997
    dbObj.cavitationOffset_kts=10.200000
    dbObj.cavitationSlope_ktsperft=0.005490
    dbObj.cavitationSL_dB=206.612000
    dbObj.snorkelingSL_dB=200.612000
    dbObj.BuildSLTable()
    return dbObj