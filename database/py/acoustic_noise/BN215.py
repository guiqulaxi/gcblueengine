# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN215'
    dbObj.xSpeed_kts=[0.000000,9.160000,32.060001,45.799999]
    dbObj.ySL_dB=[76.199997,80.356842,109.454758,117.768448]
    dbObj.speedMinNL_kts=10.640000
    dbObj.NL_min=43.520000
    dbObj.speedMaxNL_kts=45.799999
    dbObj.NL_max=80.000000
    dbObj.cavitationOffset_kts=15.200000
    dbObj.cavitationSlope_ktsperft=0.014680
    dbObj.cavitationSL_dB=135.768448
    dbObj.snorkelingSL_dB=129.768448
    dbObj.BuildSLTable()
    return dbObj