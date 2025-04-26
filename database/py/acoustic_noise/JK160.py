# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK160'
    dbObj.xSpeed_kts=[0.000000,3.842000,13.447000,19.209999]
    dbObj.ySL_dB=[91.650002,95.638878,123.561035,131.538803]
    dbObj.speedMinNL_kts=8.330000
    dbObj.NL_min=50.340000
    dbObj.speedMaxNL_kts=19.209999
    dbObj.NL_max=96.599998
    dbObj.cavitationOffset_kts=11.900000
    dbObj.cavitationSlope_ktsperft=0.008860
    dbObj.cavitationSL_dB=149.538803
    dbObj.snorkelingSL_dB=143.538803
    dbObj.BuildSLTable()
    return dbObj