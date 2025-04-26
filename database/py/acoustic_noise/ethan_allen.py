# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='ethan allen'
    dbObj.xSpeed_kts=[0.000000,7.000000,16.799999,21.000000]
    dbObj.ySL_dB=[93.599998,114.959999,127.000000,144.000000]
    dbObj.speedMinNL_kts=6.000000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=21.000000
    dbObj.NL_max=101.000000
    dbObj.cavitationOffset_kts=11.350000
    dbObj.cavitationSlope_ktsperft=0.020000
    dbObj.cavitationSL_dB=167.600006
    dbObj.snorkelingSL_dB=156.000000
    dbObj.BuildSLTable()
    return dbObj