# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK190'
    dbObj.xSpeed_kts=[0.000000,4.726000,16.541000,23.629999]
    dbObj.ySL_dB=[83.120003,87.317360,116.698868,125.093590]
    dbObj.speedMinNL_kts=9.590000
    dbObj.NL_min=46.619999
    dbObj.speedMaxNL_kts=23.629999
    dbObj.NL_max=89.400002
    dbObj.cavitationOffset_kts=13.700000
    dbObj.cavitationSlope_ktsperft=0.012580
    dbObj.cavitationSL_dB=143.093582
    dbObj.snorkelingSL_dB=137.093582
    dbObj.BuildSLTable()
    return dbObj