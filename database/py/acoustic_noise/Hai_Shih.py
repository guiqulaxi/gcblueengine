# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Hai Shih'
    dbObj.xSpeed_kts=[0.000000,4.500000,12.000000,15.000000]
    dbObj.ySL_dB=[91.900002,101.080002,119.500000,129.199997]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=16.000000
    dbObj.NL_max=101.000000
    dbObj.cavitationOffset_kts=10.740000
    dbObj.cavitationSlope_ktsperft=0.015000
    dbObj.cavitationSL_dB=163.500000
    dbObj.snorkelingSL_dB=141.199997
    dbObj.BuildSLTable()
    return dbObj