# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK150'
    dbObj.xSpeed_kts=[0.000000,2.912000,10.192000,14.560000]
    dbObj.ySL_dB=[94.639999,99.166122,130.848969,139.901215]
    dbObj.speedMinNL_kts=7.140000
    dbObj.NL_min=51.590000
    dbObj.speedMaxNL_kts=14.560000
    dbObj.NL_max=99.019997
    dbObj.cavitationOffset_kts=10.200000
    dbObj.cavitationSlope_ktsperft=0.005490
    dbObj.cavitationSL_dB=157.901215
    dbObj.snorkelingSL_dB=151.901215
    dbObj.BuildSLTable()
    return dbObj