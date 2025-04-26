# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='thresher'
    dbObj.xSpeed_kts=[0.000000,8.500000,20.000000,25.000000]
    dbObj.ySL_dB=[94.900002,118.940002,134.000000,152.000000]
    dbObj.speedMinNL_kts=6.000000
    dbObj.NL_min=51.099998
    dbObj.speedMaxNL_kts=25.000000
    dbObj.NL_max=101.250000
    dbObj.cavitationOffset_kts=11.260000
    dbObj.cavitationSlope_ktsperft=0.020000
    dbObj.cavitationSL_dB=170.300003
    dbObj.snorkelingSL_dB=164.000000
    dbObj.BuildSLTable()
    return dbObj