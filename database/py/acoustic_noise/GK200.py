# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK200'
    dbObj.xSpeed_kts=[0.000000,5.576000,19.516001,27.879999]
    dbObj.ySL_dB=[78.559998,82.172371,107.458992,114.683739]
    dbObj.speedMinNL_kts=11.165000
    dbObj.NL_min=45.049999
    dbObj.speedMaxNL_kts=27.879999
    dbObj.NL_max=85.900002
    dbObj.cavitationOffset_kts=15.950000
    dbObj.cavitationSlope_ktsperft=0.014040
    dbObj.cavitationSL_dB=132.683746
    dbObj.snorkelingSL_dB=126.683739
    dbObj.BuildSLTable()
    return dbObj