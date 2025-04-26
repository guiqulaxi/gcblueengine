# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN180'
    dbObj.xSpeed_kts=[0.000000,7.200000,25.200001,36.000000]
    dbObj.ySL_dB=[88.099998,94.124741,136.297943,148.347427]
    dbObj.speedMinNL_kts=9.660000
    dbObj.NL_min=48.000000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=96.800003
    dbObj.cavitationOffset_kts=13.800000
    dbObj.cavitationSlope_ktsperft=0.009850
    dbObj.cavitationSL_dB=166.347427
    dbObj.snorkelingSL_dB=160.347427
    dbObj.BuildSLTable()
    return dbObj