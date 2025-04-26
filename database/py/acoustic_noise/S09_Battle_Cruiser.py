# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S09.Battle Cruiser'
    dbObj.xSpeed_kts=[4.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[109.000000,113.839996,128.360001,133.199997]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=55.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=95.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj