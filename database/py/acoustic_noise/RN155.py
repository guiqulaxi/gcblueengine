# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN155'
    dbObj.xSpeed_kts=[0.000000,6.000000,21.000000,30.000000]
    dbObj.ySL_dB=[100.400002,108.694397,166.755203,183.343994]
    dbObj.speedMinNL_kts=6.230000
    dbObj.NL_min=51.200001
    dbObj.speedMaxNL_kts=30.000000
    dbObj.NL_max=108.199997
    dbObj.cavitationOffset_kts=8.900000
    dbObj.cavitationSlope_ktsperft=0.003650
    dbObj.cavitationSL_dB=201.343994
    dbObj.snorkelingSL_dB=195.343994
    dbObj.BuildSLTable()
    return dbObj