# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 641B'
    dbObj.xSpeed_kts=[0.000000,4.500000,12.000000,15.000000]
    dbObj.ySL_dB=[92.699997,102.660004,122.900002,134.699997]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=16.000000
    dbObj.NL_max=102.000000
    dbObj.cavitationOffset_kts=12.040000
    dbObj.cavitationSlope_ktsperft=0.018000
    dbObj.cavitationSL_dB=164.800003
    dbObj.snorkelingSL_dB=146.699997
    dbObj.BuildSLTable()
    return dbObj