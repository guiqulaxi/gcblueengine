# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN160'
    dbObj.xSpeed_kts=[0.000000,6.240000,21.840000,31.200001]
    dbObj.ySL_dB=[98.599998,106.881126,164.849030,181.411285]
    dbObj.speedMinNL_kts=6.545000
    dbObj.NL_min=50.700001
    dbObj.speedMaxNL_kts=31.200001
    dbObj.NL_max=106.199997
    dbObj.cavitationOffset_kts=9.350000
    dbObj.cavitationSlope_ktsperft=0.003975
    dbObj.cavitationSL_dB=199.411285
    dbObj.snorkelingSL_dB=193.411285
    dbObj.BuildSLTable()
    return dbObj