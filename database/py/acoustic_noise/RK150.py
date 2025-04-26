# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK150'
    dbObj.xSpeed_kts=[0.000000,3.040000,10.640000,15.200000]
    dbObj.ySL_dB=[96.900002,101.277603,131.920807,140.675995]
    dbObj.speedMinNL_kts=5.915000
    dbObj.NL_min=51.700001
    dbObj.speedMaxNL_kts=15.200000
    dbObj.NL_max=98.199997
    dbObj.cavitationOffset_kts=8.450000
    dbObj.cavitationSlope_ktsperft=0.003325
    dbObj.cavitationSL_dB=158.675995
    dbObj.snorkelingSL_dB=152.675995
    dbObj.BuildSLTable()
    return dbObj