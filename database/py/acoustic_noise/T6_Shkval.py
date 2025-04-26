# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='T6:Shkval'
    dbObj.xSpeed_kts=[10.000000,40.000000,80.000000,120.000000]
    dbObj.ySL_dB=[114.000000,114.000000,158.000000,202.000000]
    dbObj.speedMinNL_kts=30.000000
    dbObj.NL_min=70.000000
    dbObj.speedMaxNL_kts=180.000000
    dbObj.NL_max=71.000000
    dbObj.cavitationOffset_kts=999.000000
    dbObj.cavitationSlope_ktsperft=999.000000
    dbObj.cavitationSL_dB=202.000000
    dbObj.snorkelingSL_dB=202.000000
    dbObj.BuildSLTable()
    return dbObj