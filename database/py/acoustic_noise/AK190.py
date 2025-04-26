# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK190'
    dbObj.xSpeed_kts=[0.000000,4.726000,16.541000,23.629999]
    dbObj.ySL_dB=[82.389999,86.451958,114.885681,123.009598]
    dbObj.speedMinNL_kts=10.220000
    dbObj.NL_min=46.799999
    dbObj.speedMaxNL_kts=23.629999
    dbObj.NL_max=89.400002
    dbObj.cavitationOffset_kts=14.600000
    dbObj.cavitationSlope_ktsperft=0.010950
    dbObj.cavitationSL_dB=141.009598
    dbObj.snorkelingSL_dB=135.009598
    dbObj.BuildSLTable()
    return dbObj