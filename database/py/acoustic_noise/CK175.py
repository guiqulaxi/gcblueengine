# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK175'
    dbObj.xSpeed_kts=[0.000000,4.030000,14.105000,20.150000]
    dbObj.ySL_dB=[93.379997,98.906502,137.592026,148.645035]
    dbObj.speedMinNL_kts=6.615000
    dbObj.NL_min=50.500000
    dbObj.speedMaxNL_kts=20.150000
    dbObj.NL_max=100.500000
    dbObj.cavitationOffset_kts=9.450000
    dbObj.cavitationSlope_ktsperft=0.004500
    dbObj.cavitationSL_dB=166.645035
    dbObj.snorkelingSL_dB=160.645035
    dbObj.BuildSLTable()
    return dbObj