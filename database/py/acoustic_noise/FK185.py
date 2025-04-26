# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK185'
    dbObj.xSpeed_kts=[0.000000,4.396000,15.386000,21.980000]
    dbObj.ySL_dB=[85.120003,89.617271,121.098152,130.092682]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=47.320000
    dbObj.speedMaxNL_kts=21.980000
    dbObj.NL_max=90.760002
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.008920
    dbObj.cavitationSL_dB=148.092682
    dbObj.snorkelingSL_dB=142.092682
    dbObj.BuildSLTable()
    return dbObj