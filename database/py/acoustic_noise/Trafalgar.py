# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Trafalgar'
    dbObj.xSpeed_kts=[0.000000,9.600000,25.600000,32.000000]
    dbObj.ySL_dB=[87.699997,93.940002,105.500000,125.000000]
    dbObj.speedMinNL_kts=10.000000
    dbObj.NL_min=48.000000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=98.000000
    dbObj.cavitationOffset_kts=13.020000
    dbObj.cavitationSlope_ktsperft=0.027000
    dbObj.cavitationSL_dB=162.699997
    dbObj.snorkelingSL_dB=137.000000
    dbObj.BuildSLTable()
    return dbObj