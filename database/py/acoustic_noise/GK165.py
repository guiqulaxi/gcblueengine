# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK165'
    dbObj.xSpeed_kts=[0.000000,4.064000,14.224000,20.320000]
    dbObj.ySL_dB=[85.839996,89.840065,117.840538,125.840675]
    dbObj.speedMinNL_kts=8.960000
    dbObj.NL_min=49.599998
    dbObj.speedMaxNL_kts=20.320000
    dbObj.NL_max=95.000000
    dbObj.cavitationOffset_kts=12.800000
    dbObj.cavitationSlope_ktsperft=0.009560
    dbObj.cavitationSL_dB=143.840668
    dbObj.snorkelingSL_dB=137.840668
    dbObj.BuildSLTable()
    return dbObj