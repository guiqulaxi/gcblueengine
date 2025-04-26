# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK205'
    dbObj.xSpeed_kts=[0.000000,5.368000,18.788000,26.840000]
    dbObj.ySL_dB=[79.160004,83.119850,110.838776,118.758476]
    dbObj.speedMinNL_kts=10.220000
    dbObj.NL_min=44.759998
    dbObj.speedMaxNL_kts=26.840000
    dbObj.NL_max=85.800003
    dbObj.cavitationOffset_kts=14.600000
    dbObj.cavitationSlope_ktsperft=0.014440
    dbObj.cavitationSL_dB=136.758469
    dbObj.snorkelingSL_dB=130.758469
    dbObj.BuildSLTable()
    return dbObj