# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN160'
    dbObj.xSpeed_kts=[0.000000,6.240000,21.840000,31.200001]
    dbObj.ySL_dB=[97.099998,105.248802,162.290405,178.588013]
    dbObj.speedMinNL_kts=7.420000
    dbObj.NL_min=50.369999
    dbObj.speedMaxNL_kts=31.200001
    dbObj.NL_max=105.449997
    dbObj.cavitationOffset_kts=10.600000
    dbObj.cavitationSlope_ktsperft=0.006470
    dbObj.cavitationSL_dB=196.588013
    dbObj.snorkelingSL_dB=190.588013
    dbObj.BuildSLTable()
    return dbObj