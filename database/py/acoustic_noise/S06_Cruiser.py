# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S06.Cruiser'
    dbObj.xSpeed_kts=[5.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[107.000000,111.400002,124.599998,129.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=54.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=94.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj