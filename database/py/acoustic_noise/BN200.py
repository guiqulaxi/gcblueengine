# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN200'
    dbObj.xSpeed_kts=[0.000000,8.380000,29.330000,41.900002]
    dbObj.ySL_dB=[81.300003,86.247955,120.883659,130.779572]
    dbObj.speedMinNL_kts=10.010000
    dbObj.NL_min=45.380001
    dbObj.speedMaxNL_kts=41.900002
    dbObj.NL_max=86.900002
    dbObj.cavitationOffset_kts=14.300000
    dbObj.cavitationSlope_ktsperft=0.012820
    dbObj.cavitationSL_dB=148.779572
    dbObj.snorkelingSL_dB=142.779572
    dbObj.BuildSLTable()
    return dbObj