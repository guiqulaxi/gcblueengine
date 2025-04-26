# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK185'
    dbObj.xSpeed_kts=[0.000000,4.928000,17.247999,24.639999]
    dbObj.ySL_dB=[81.680000,85.499336,112.234695,119.873367]
    dbObj.speedMinNL_kts=10.220000
    dbObj.NL_min=47.000000
    dbObj.speedMaxNL_kts=24.639999
    dbObj.NL_max=89.800003
    dbObj.cavitationOffset_kts=14.600000
    dbObj.cavitationSlope_ktsperft=0.012120
    dbObj.cavitationSL_dB=137.873367
    dbObj.snorkelingSL_dB=131.873367
    dbObj.BuildSLTable()
    return dbObj