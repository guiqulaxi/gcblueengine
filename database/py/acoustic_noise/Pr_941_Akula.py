# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 941 Akula'
    dbObj.xSpeed_kts=[0.000000,7.500000,20.000000,25.000000]
    dbObj.ySL_dB=[92.900002,103.129997,124.000000,140.000000]
    dbObj.speedMinNL_kts=6.000000
    dbObj.NL_min=51.500000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=101.500000
    dbObj.cavitationOffset_kts=11.120000
    dbObj.cavitationSlope_ktsperft=0.022000
    dbObj.cavitationSL_dB=166.300003
    dbObj.snorkelingSL_dB=152.000000
    dbObj.BuildSLTable()
    return dbObj