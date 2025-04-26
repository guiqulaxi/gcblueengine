# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Torpedo1'
    dbObj.xSpeed_kts=[0.000000,5.000000,10.000000,50.000000]
    dbObj.ySL_dB=[130.000000,130.000000,132.000000,152.000000]
    dbObj.speedMinNL_kts=20.000000
    dbObj.NL_min=70.000000
    dbObj.speedMaxNL_kts=50.000000
    dbObj.NL_max=90.000000
    dbObj.cavitationOffset_kts=99.000000
    dbObj.cavitationSlope_ktsperft=0.050000
    dbObj.cavitationSL_dB=100.000000
    dbObj.snorkelingSL_dB=100.000000
    dbObj.BuildSLTable()
    return dbObj