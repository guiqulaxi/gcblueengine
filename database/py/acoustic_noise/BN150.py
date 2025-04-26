# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN150'
    dbObj.xSpeed_kts=[0.000000,5.780000,20.230000,28.900000]
    dbObj.ySL_dB=[98.300003,106.506447,163.951553,180.364441]
    dbObj.speedMinNL_kts=7.910000
    dbObj.NL_min=51.580002
    dbObj.speedMaxNL_kts=28.900000
    dbObj.NL_max=109.900002
    dbObj.cavitationOffset_kts=11.300000
    dbObj.cavitationSlope_ktsperft=0.006620
    dbObj.cavitationSL_dB=198.364441
    dbObj.snorkelingSL_dB=192.364441
    dbObj.BuildSLTable()
    return dbObj