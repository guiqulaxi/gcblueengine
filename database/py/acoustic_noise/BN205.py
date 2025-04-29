# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN205'
    dbObj.xSpeed_kts=[0.000000,8.640000,30.240000,43.200001]
    dbObj.ySL_dB=[79.599998,84.272949,116.983597,126.329498]
    dbObj.speedMinNL_kts=10.220000
    dbObj.NL_min=44.759998
    dbObj.speedMaxNL_kts=43.200001
    dbObj.NL_max=84.599998
    dbObj.cavitationOffset_kts=14.600000
    dbObj.cavitationSlope_ktsperft=0.013440
    dbObj.cavitationSL_dB=144.329498
    dbObj.snorkelingSL_dB=138.329498
    dbObj.BuildSLTable()
    return dbObj