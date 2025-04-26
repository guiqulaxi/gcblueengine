# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='La Fayette'
    dbObj.xSpeed_kts=[0.000000,8.500000,20.000000,25.000000]
    dbObj.ySL_dB=[92.000000,110.800003,120.000000,136.000000]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=50.750000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=100.750000
    dbObj.cavitationOffset_kts=11.610000
    dbObj.cavitationSlope_ktsperft=0.024000
    dbObj.cavitationSL_dB=165.199997
    dbObj.snorkelingSL_dB=148.000000
    dbObj.BuildSLTable()
    return dbObj