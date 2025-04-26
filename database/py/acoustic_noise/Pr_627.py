# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 627'
    dbObj.xSpeed_kts=[0.000000,10.000000,24.000000,30.000000]
    dbObj.ySL_dB=[98.500000,129.100006,159.000000,172.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=51.500000
    dbObj.speedMaxNL_kts=30.000000
    dbObj.NL_max=102.000000
    dbObj.cavitationOffset_kts=8.550000
    dbObj.cavitationSlope_ktsperft=0.015000
    dbObj.cavitationSL_dB=177.800003
    dbObj.snorkelingSL_dB=184.000000
    dbObj.BuildSLTable()
    return dbObj