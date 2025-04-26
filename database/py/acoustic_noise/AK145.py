# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK145'
    dbObj.xSpeed_kts=[0.000000,2.800000,9.800000,14.000000]
    dbObj.ySL_dB=[94.000000,98.199997,127.599998,136.000000]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=14.000000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=154.000000
    dbObj.snorkelingSL_dB=148.000000
    dbObj.BuildSLTable()
    return dbObj