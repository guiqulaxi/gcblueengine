# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK215'
    dbObj.xSpeed_kts=[0.000000,5.768000,20.188000,28.840000]
    dbObj.ySL_dB=[76.099998,79.690331,104.822670,112.003342]
    dbObj.speedMinNL_kts=11.130000
    dbObj.NL_min=43.520000
    dbObj.speedMaxNL_kts=28.840000
    dbObj.NL_max=82.699997
    dbObj.cavitationOffset_kts=15.900000
    dbObj.cavitationSlope_ktsperft=0.016520
    dbObj.cavitationSL_dB=130.003342
    dbObj.snorkelingSL_dB=124.003342
    dbObj.BuildSLTable()
    return dbObj