# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN210'
    dbObj.xSpeed_kts=[0.000000,8.640000,30.240000,43.200001]
    dbObj.ySL_dB=[80.599998,85.197853,117.382812,126.578514]
    dbObj.speedMinNL_kts=9.695000
    dbObj.NL_min=45.700001
    dbObj.speedMaxNL_kts=43.200001
    dbObj.NL_max=86.199997
    dbObj.cavitationOffset_kts=13.850000
    dbObj.cavitationSlope_ktsperft=0.013075
    dbObj.cavitationSL_dB=144.578522
    dbObj.snorkelingSL_dB=138.578522
    dbObj.BuildSLTable()
    return dbObj