# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK170'
    dbObj.xSpeed_kts=[0.000000,4.280000,14.980000,21.400000]
    dbObj.ySL_dB=[84.800003,88.768333,116.546677,124.483345]
    dbObj.speedMinNL_kts=9.275000
    dbObj.NL_min=48.950001
    dbObj.speedMaxNL_kts=21.400000
    dbObj.NL_max=93.699997
    dbObj.cavitationOffset_kts=13.250000
    dbObj.cavitationSlope_ktsperft=0.010200
    dbObj.cavitationSL_dB=142.483353
    dbObj.snorkelingSL_dB=136.483353
    dbObj.BuildSLTable()
    return dbObj