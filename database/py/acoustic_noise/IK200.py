# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK200'
    dbObj.xSpeed_kts=[0.000000,5.032000,17.612000,25.160000]
    dbObj.ySL_dB=[81.260002,85.272614,113.360924,121.386162]
    dbObj.speedMinNL_kts=9.548000
    dbObj.NL_min=45.490002
    dbObj.speedMaxNL_kts=25.160000
    dbObj.NL_max=86.889999
    dbObj.cavitationOffset_kts=13.640000
    dbObj.cavitationSlope_ktsperft=0.011270
    dbObj.cavitationSL_dB=139.386154
    dbObj.snorkelingSL_dB=133.386154
    dbObj.BuildSLTable()
    return dbObj