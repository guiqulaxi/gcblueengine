# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK175'
    dbObj.xSpeed_kts=[0.000000,4.084000,14.294000,20.420000]
    dbObj.ySL_dB=[86.260002,90.486145,120.069138,128.521423]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=48.599998
    dbObj.speedMaxNL_kts=20.420000
    dbObj.NL_max=93.000000
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.009300
    dbObj.cavitationSL_dB=146.521423
    dbObj.snorkelingSL_dB=140.521423
    dbObj.BuildSLTable()
    return dbObj