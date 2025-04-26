# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK215'
    dbObj.xSpeed_kts=[0.000000,5.796000,20.285999,28.980000]
    dbObj.ySL_dB=[76.519997,80.297897,106.743172,114.298965]
    dbObj.speedMinNL_kts=10.640000
    dbObj.NL_min=43.520000
    dbObj.speedMaxNL_kts=28.980000
    dbObj.NL_max=83.400002
    dbObj.cavitationOffset_kts=15.200000
    dbObj.cavitationSlope_ktsperft=0.015680
    dbObj.cavitationSL_dB=132.298965
    dbObj.snorkelingSL_dB=126.298965
    dbObj.BuildSLTable()
    return dbObj