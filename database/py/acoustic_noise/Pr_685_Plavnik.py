# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 685 Plavnik'
    dbObj.xSpeed_kts=[0.000000,9.000000,24.000000,30.000000]
    dbObj.ySL_dB=[97.300003,113.709999,149.000000,164.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=102.000000
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.020000
    dbObj.cavitationSL_dB=174.800003
    dbObj.snorkelingSL_dB=176.000000
    dbObj.BuildSLTable()
    return dbObj