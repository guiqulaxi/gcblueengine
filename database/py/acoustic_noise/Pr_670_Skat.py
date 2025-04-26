# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 670 Skat'
    dbObj.xSpeed_kts=[0.000000,7.200000,19.200001,24.000000]
    dbObj.ySL_dB=[97.000000,113.050003,147.500000,164.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=53.500000
    dbObj.speedMaxNL_kts=24.000000
    dbObj.NL_max=103.500000
    dbObj.cavitationOffset_kts=10.540000
    dbObj.cavitationSlope_ktsperft=0.018000
    dbObj.cavitationSL_dB=174.800003
    dbObj.snorkelingSL_dB=176.000000
    dbObj.BuildSLTable()
    return dbObj