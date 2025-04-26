# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Collins SSK'
    dbObj.xSpeed_kts=[0.000000,7.500000,20.000000,25.000000]
    dbObj.ySL_dB=[90.599998,98.669998,114.500000,122.900002]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=46.500000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=96.500000
    dbObj.cavitationOffset_kts=13.540000
    dbObj.cavitationSlope_ktsperft=0.030000
    dbObj.cavitationSL_dB=162.300003
    dbObj.snorkelingSL_dB=134.899994
    dbObj.BuildSLTable()
    return dbObj