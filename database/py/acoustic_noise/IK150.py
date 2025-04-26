# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK150'
    dbObj.xSpeed_kts=[0.000000,2.912000,10.192000,14.560000]
    dbObj.ySL_dB=[94.660004,98.971214,129.149734,137.772156]
    dbObj.speedMinNL_kts=7.868000
    dbObj.NL_min=51.590000
    dbObj.speedMaxNL_kts=14.560000
    dbObj.NL_max=98.989998
    dbObj.cavitationOffset_kts=11.240000
    dbObj.cavitationSlope_ktsperft=0.005570
    dbObj.cavitationSL_dB=155.772156
    dbObj.snorkelingSL_dB=149.772156
    dbObj.BuildSLTable()
    return dbObj