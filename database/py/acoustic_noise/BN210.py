# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN210'
    dbObj.xSpeed_kts=[0.000000,8.900000,31.150000,44.500000]
    dbObj.ySL_dB=[77.900002,82.309235,113.173851,121.992310]
    dbObj.speedMinNL_kts=10.430000
    dbObj.NL_min=44.139999
    dbObj.speedMaxNL_kts=44.500000
    dbObj.NL_max=82.300003
    dbObj.cavitationOffset_kts=14.900000
    dbObj.cavitationSlope_ktsperft=0.014060
    dbObj.cavitationSL_dB=139.992310
    dbObj.snorkelingSL_dB=133.992310
    dbObj.BuildSLTable()
    return dbObj