# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 671RTMK'
    dbObj.xSpeed_kts=[0.000000,9.000000,24.000000,30.000000]
    dbObj.ySL_dB=[93.599998,104.519997,127.000000,144.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=53.000000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=103.000000
    dbObj.cavitationOffset_kts=10.540000
    dbObj.cavitationSlope_ktsperft=0.021000
    dbObj.cavitationSL_dB=167.600006
    dbObj.snorkelingSL_dB=156.000000
    dbObj.BuildSLTable()
    return dbObj