# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Yushio'
    dbObj.xSpeed_kts=[0.000000,6.000000,16.000000,20.000000]
    dbObj.ySL_dB=[91.500000,100.349998,118.000000,127.099998]
    dbObj.speedMinNL_kts=6.000000
    dbObj.NL_min=47.000000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=97.000000
    dbObj.cavitationOffset_kts=13.180000
    dbObj.cavitationSlope_ktsperft=0.025000
    dbObj.cavitationSL_dB=163.100006
    dbObj.snorkelingSL_dB=139.100006
    dbObj.BuildSLTable()
    return dbObj