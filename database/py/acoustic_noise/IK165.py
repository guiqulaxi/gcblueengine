# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK165'
    dbObj.xSpeed_kts=[0.000000,3.548000,12.418000,17.740000]
    dbObj.ySL_dB=[90.639999,95.002907,125.543228,134.269028]
    dbObj.speedMinNL_kts=8.372000
    dbObj.NL_min=49.759998
    dbObj.speedMaxNL_kts=17.740000
    dbObj.NL_max=95.360001
    dbObj.cavitationOffset_kts=11.960000
    dbObj.cavitationSlope_ktsperft=0.007280
    dbObj.cavitationSL_dB=152.269028
    dbObj.snorkelingSL_dB=146.269028
    dbObj.BuildSLTable()
    return dbObj