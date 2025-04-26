# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Kobben'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[92.400002,102.089996,121.699997,133.000000]
    dbObj.speedMinNL_kts=6.000000
    dbObj.NL_min=47.000000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=97.000000
    dbObj.cavitationOffset_kts=12.740000
    dbObj.cavitationSlope_ktsperft=0.020000
    dbObj.cavitationSL_dB=164.399994
    dbObj.snorkelingSL_dB=145.000000
    dbObj.BuildSLTable()
    return dbObj