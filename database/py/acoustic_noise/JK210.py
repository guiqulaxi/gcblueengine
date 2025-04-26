# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK210'
    dbObj.xSpeed_kts=[0.000000,5.982000,20.937000,29.910000]
    dbObj.ySL_dB=[77.150002,80.495171,103.911377,110.601723]
    dbObj.speedMinNL_kts=10.430000
    dbObj.NL_min=44.139999
    dbObj.speedMaxNL_kts=29.910000
    dbObj.NL_max=84.599998
    dbObj.cavitationOffset_kts=14.900000
    dbObj.cavitationSlope_ktsperft=0.015060
    dbObj.cavitationSL_dB=128.601730
    dbObj.snorkelingSL_dB=122.601723
    dbObj.BuildSLTable()
    return dbObj