# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK205'
    dbObj.xSpeed_kts=[0.000000,5.768000,20.188000,28.840000]
    dbObj.ySL_dB=[78.599998,82.031387,106.051086,112.913857]
    dbObj.speedMinNL_kts=10.220000
    dbObj.NL_min=44.759998
    dbObj.speedMaxNL_kts=28.840000
    dbObj.NL_max=85.800003
    dbObj.cavitationOffset_kts=14.600000
    dbObj.cavitationSlope_ktsperft=0.014440
    dbObj.cavitationSL_dB=130.913849
    dbObj.snorkelingSL_dB=124.913857
    dbObj.BuildSLTable()
    return dbObj