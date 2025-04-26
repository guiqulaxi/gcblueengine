# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN160'
    dbObj.xSpeed_kts=[0.000000,6.300000,22.049999,31.500000]
    dbObj.ySL_dB=[94.900002,102.405136,154.941101,169.951370]
    dbObj.speedMinNL_kts=8.330000
    dbObj.NL_min=50.340000
    dbObj.speedMaxNL_kts=31.500000
    dbObj.NL_max=105.300003
    dbObj.cavitationOffset_kts=11.900000
    dbObj.cavitationSlope_ktsperft=0.007860
    dbObj.cavitationSL_dB=187.951370
    dbObj.snorkelingSL_dB=181.951370
    dbObj.BuildSLTable()
    return dbObj