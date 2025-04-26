# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN190'
    dbObj.xSpeed_kts=[0.000000,7.680000,26.879999,38.400002]
    dbObj.ySL_dB=[87.800003,93.200897,131.007202,141.809006]
    dbObj.speedMinNL_kts=8.435000
    dbObj.NL_min=47.700001
    dbObj.speedMaxNL_kts=38.400002
    dbObj.NL_max=94.199997
    dbObj.cavitationOffset_kts=12.050000
    dbObj.cavitationSlope_ktsperft=0.007875
    dbObj.cavitationSL_dB=159.809006
    dbObj.snorkelingSL_dB=153.809006
    dbObj.BuildSLTable()
    return dbObj