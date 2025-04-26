# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN205'
    dbObj.xSpeed_kts=[0.000000,8.400000,29.400000,42.000000]
    dbObj.ySL_dB=[82.400002,87.196594,120.772766,130.365967]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=46.200001
    dbObj.speedMaxNL_kts=42.000000
    dbObj.NL_max=88.199997
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.011775
    dbObj.cavitationSL_dB=148.365967
    dbObj.snorkelingSL_dB=142.365967
    dbObj.BuildSLTable()
    return dbObj