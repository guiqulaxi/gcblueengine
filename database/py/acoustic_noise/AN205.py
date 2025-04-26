# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN205'
    dbObj.xSpeed_kts=[0.000000,8.400000,29.400000,42.000000]
    dbObj.ySL_dB=[79.599998,84.232597,116.660774,125.925964]
    dbObj.speedMinNL_kts=11.060000
    dbObj.NL_min=45.000000
    dbObj.speedMaxNL_kts=42.000000
    dbObj.NL_max=85.800003
    dbObj.cavitationOffset_kts=15.800000
    dbObj.cavitationSlope_ktsperft=0.012600
    dbObj.cavitationSL_dB=143.925964
    dbObj.snorkelingSL_dB=137.925964
    dbObj.BuildSLTable()
    return dbObj