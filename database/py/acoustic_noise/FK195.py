# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK195'
    dbObj.xSpeed_kts=[0.000000,4.820000,16.870001,24.100000]
    dbObj.ySL_dB=[82.400002,86.775627,117.404991,126.156242]
    dbObj.speedMinNL_kts=8.400000
    dbObj.NL_min=46.099998
    dbObj.speedMaxNL_kts=24.100000
    dbObj.NL_max=88.400002
    dbObj.cavitationOffset_kts=12.000000
    dbObj.cavitationSlope_ktsperft=0.009900
    dbObj.cavitationSL_dB=144.156235
    dbObj.snorkelingSL_dB=138.156235
    dbObj.BuildSLTable()
    return dbObj