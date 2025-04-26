# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK145'
    dbObj.xSpeed_kts=[0.000000,2.800000,9.800000,14.000000]
    dbObj.ySL_dB=[95.000000,99.339996,129.720001,138.399994]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=14.000000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.007000
    dbObj.cavitationSL_dB=156.399994
    dbObj.snorkelingSL_dB=150.399994
    dbObj.BuildSLTable()
    return dbObj