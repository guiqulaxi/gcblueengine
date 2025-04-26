# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK195'
    dbObj.xSpeed_kts=[0.000000,4.940000,17.290001,24.700001]
    dbObj.ySL_dB=[81.800003,85.924179,114.793404,123.041756]
    dbObj.speedMinNL_kts=9.800000
    dbObj.NL_min=46.000000
    dbObj.speedMaxNL_kts=24.700001
    dbObj.NL_max=88.199997
    dbObj.cavitationOffset_kts=14.000000
    dbObj.cavitationSlope_ktsperft=0.013200
    dbObj.cavitationSL_dB=141.041763
    dbObj.snorkelingSL_dB=135.041763
    dbObj.BuildSLTable()
    return dbObj