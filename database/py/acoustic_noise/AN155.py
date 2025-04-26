# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN155'
    dbObj.xSpeed_kts=[0.000000,6.000000,21.000000,30.000000]
    dbObj.ySL_dB=[96.599998,104.217598,157.540802,172.776001]
    dbObj.speedMinNL_kts=8.260000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=30.000000
    dbObj.NL_max=107.800003
    dbObj.cavitationOffset_kts=11.800000
    dbObj.cavitationSlope_ktsperft=0.007100
    dbObj.cavitationSL_dB=190.776001
    dbObj.snorkelingSL_dB=184.776001
    dbObj.BuildSLTable()
    return dbObj