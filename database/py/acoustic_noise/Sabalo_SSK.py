# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Sabalo SSK'
    dbObj.xSpeed_kts=[0.000000,6.000000,16.000000,20.000000]
    dbObj.ySL_dB=[91.900002,101.050003,119.400002,129.000000]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=47.500000
    dbObj.speedMaxNL_kts=24.000000
    dbObj.NL_max=97.500000
    dbObj.cavitationOffset_kts=12.880000
    dbObj.cavitationSlope_ktsperft=0.016000
    dbObj.cavitationSL_dB=163.500000
    dbObj.snorkelingSL_dB=141.000000
    dbObj.BuildSLTable()
    return dbObj