# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK165'
    dbObj.xSpeed_kts=[0.000000,3.656000,12.796000,18.280001]
    dbObj.ySL_dB=[89.720001,94.144348,125.114784,133.963486]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=49.720001
    dbObj.speedMaxNL_kts=18.280001
    dbObj.NL_max=95.400002
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.009480
    dbObj.cavitationSL_dB=151.963486
    dbObj.snorkelingSL_dB=145.963486
    dbObj.BuildSLTable()
    return dbObj