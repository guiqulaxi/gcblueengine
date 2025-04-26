# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK155'
    dbObj.xSpeed_kts=[0.000000,3.124000,10.934000,15.620000]
    dbObj.ySL_dB=[93.320000,97.667580,128.100616,136.795776]
    dbObj.speedMinNL_kts=8.036000
    dbObj.NL_min=50.980000
    dbObj.speedMaxNL_kts=15.620000
    dbObj.NL_max=97.779999
    dbObj.cavitationOffset_kts=11.480000
    dbObj.cavitationSlope_ktsperft=0.006140
    dbObj.cavitationSL_dB=154.795776
    dbObj.snorkelingSL_dB=148.795776
    dbObj.BuildSLTable()
    return dbObj