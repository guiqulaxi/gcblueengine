# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN170'
    dbObj.xSpeed_kts=[0.000000,6.720000,23.520000,33.599998]
    dbObj.ySL_dB=[91.500000,98.143539,144.648331,157.935425]
    dbObj.speedMinNL_kts=9.100000
    dbObj.NL_min=49.200001
    dbObj.speedMaxNL_kts=33.599998
    dbObj.NL_max=101.199997
    dbObj.cavitationOffset_kts=13.000000
    dbObj.cavitationSlope_ktsperft=0.008750
    dbObj.cavitationSL_dB=175.935425
    dbObj.snorkelingSL_dB=169.935425
    dbObj.BuildSLTable()
    return dbObj