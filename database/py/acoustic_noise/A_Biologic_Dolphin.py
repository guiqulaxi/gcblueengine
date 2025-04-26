# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='A Biologic Dolphin'
    dbObj.xSpeed_kts=[4.000000,12.000000,24.000000,36.000000]
    dbObj.ySL_dB=[92.300003,96.919998,104.000000,112.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=0.000000
    dbObj.speedMaxNL_kts=0.000000
    dbObj.NL_max=0.000000
    dbObj.cavitationOffset_kts=0.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj