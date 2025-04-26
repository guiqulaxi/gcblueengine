# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN200'
    dbObj.xSpeed_kts=[0.000000,6.900000,24.150000,34.500000]
    dbObj.ySL_dB=[85.900002,91.512047,130.796402,142.020493]
    dbObj.speedMinNL_kts=8.190000
    dbObj.NL_min=48.000000
    dbObj.speedMaxNL_kts=34.500000
    dbObj.NL_max=90.500000
    dbObj.cavitationOffset_kts=11.700000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=160.020493
    dbObj.snorkelingSL_dB=154.020493
    dbObj.BuildSLTable()
    return dbObj