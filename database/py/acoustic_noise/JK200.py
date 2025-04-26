# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK200'
    dbObj.xSpeed_kts=[0.000000,5.554000,19.438999,27.770000]
    dbObj.ySL_dB=[80.050003,83.564972,108.169800,115.199753]
    dbObj.speedMinNL_kts=10.010000
    dbObj.NL_min=45.380001
    dbObj.speedMaxNL_kts=27.770000
    dbObj.NL_max=87.000000
    dbObj.cavitationOffset_kts=14.300000
    dbObj.cavitationSlope_ktsperft=0.013820
    dbObj.cavitationSL_dB=133.199753
    dbObj.snorkelingSL_dB=127.199753
    dbObj.BuildSLTable()
    return dbObj