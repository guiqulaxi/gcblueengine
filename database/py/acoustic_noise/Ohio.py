# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Ohio'
    dbObj.xSpeed_kts=[0.000000,7.500000,20.000000,25.000000]
    dbObj.ySL_dB=[82.599998,87.220001,95.000000,114.000000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=50.000000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=12.700000
    dbObj.cavitationSlope_ktsperft=0.028000
    dbObj.cavitationSL_dB=161.300003
    dbObj.snorkelingSL_dB=126.000000
    dbObj.BuildSLTable()
    return dbObj