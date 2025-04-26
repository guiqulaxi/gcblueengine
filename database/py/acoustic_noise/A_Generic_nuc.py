# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='A Generic nuc'
    dbObj.xSpeed_kts=[0.000000,9.600000,21.600000,33.000000]
    dbObj.ySL_dB=[101.400002,109.099998,121.099998,132.100006]
    dbObj.speedMinNL_kts=7.300000
    dbObj.NL_min=50.799999
    dbObj.speedMaxNL_kts=33.000000
    dbObj.NL_max=100.800003
    dbObj.cavitationOffset_kts=5.300000
    dbObj.cavitationSlope_ktsperft=0.028751
    dbObj.cavitationSL_dB=166.000000
    dbObj.snorkelingSL_dB=169.000000
    dbObj.BuildSLTable()
    return dbObj