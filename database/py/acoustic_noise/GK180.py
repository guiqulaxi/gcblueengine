# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK180'
    dbObj.xSpeed_kts=[0.000000,4.712000,16.492001,23.559999]
    dbObj.ySL_dB=[82.720001,86.596786,113.734276,121.487839]
    dbObj.speedMinNL_kts=9.905000
    dbObj.NL_min=47.650002
    dbObj.speedMaxNL_kts=23.559999
    dbObj.NL_max=91.099998
    dbObj.cavitationOffset_kts=14.150000
    dbObj.cavitationSlope_ktsperft=0.011480
    dbObj.cavitationSL_dB=139.487839
    dbObj.snorkelingSL_dB=133.487839
    dbObj.BuildSLTable()
    return dbObj