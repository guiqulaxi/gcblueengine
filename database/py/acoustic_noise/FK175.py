# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK175'
    dbObj.xSpeed_kts=[0.000000,3.972000,13.902000,19.860001]
    dbObj.ySL_dB=[87.839996,92.419296,124.474358,133.632950]
    dbObj.speedMinNL_kts=7.840000
    dbObj.NL_min=48.540001
    dbObj.speedMaxNL_kts=19.860001
    dbObj.NL_max=93.120003
    dbObj.cavitationOffset_kts=11.200000
    dbObj.cavitationSlope_ktsperft=0.007940
    dbObj.cavitationSL_dB=151.632950
    dbObj.snorkelingSL_dB=145.632950
    dbObj.BuildSLTable()
    return dbObj