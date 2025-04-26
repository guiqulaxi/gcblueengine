# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='A Generic Diesel'
    dbObj.xSpeed_kts=[0.000000,5.300000,13.300000,21.000000]
    dbObj.ySL_dB=[98.000000,104.800003,116.800003,127.099998]
    dbObj.speedMinNL_kts=6.100000
    dbObj.NL_min=48.599998
    dbObj.speedMaxNL_kts=21.000000
    dbObj.NL_max=98.599998
    dbObj.cavitationOffset_kts=6.500000
    dbObj.cavitationSlope_ktsperft=0.032397
    dbObj.cavitationSL_dB=155.199997
    dbObj.snorkelingSL_dB=158.199997
    dbObj.BuildSLTable()
    return dbObj