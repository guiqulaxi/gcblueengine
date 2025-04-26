# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN180'
    dbObj.xSpeed_kts=[0.000000,7.200000,25.200001,36.000000]
    dbObj.ySL_dB=[89.900002,96.783485,144.967911,158.734879]
    dbObj.speedMinNL_kts=7.980000
    dbObj.NL_min=47.930000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=96.449997
    dbObj.cavitationOffset_kts=11.400000
    dbObj.cavitationSlope_ktsperft=0.008430
    dbObj.cavitationSL_dB=176.734879
    dbObj.snorkelingSL_dB=170.734879
    dbObj.BuildSLTable()
    return dbObj