# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK200'
    dbObj.xSpeed_kts=[0.000000,5.154000,18.039000,25.770000]
    dbObj.ySL_dB=[79.809998,83.724190,111.123535,118.951912]
    dbObj.speedMinNL_kts=10.780000
    dbObj.NL_min=45.599998
    dbObj.speedMaxNL_kts=25.770000
    dbObj.NL_max=87.000000
    dbObj.cavitationOffset_kts=15.400000
    dbObj.cavitationSlope_ktsperft=0.012050
    dbObj.cavitationSL_dB=136.951920
    dbObj.snorkelingSL_dB=130.951920
    dbObj.BuildSLTable()
    return dbObj