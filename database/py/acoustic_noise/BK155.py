# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK155'
    dbObj.xSpeed_kts=[0.000000,3.228000,11.298000,16.139999]
    dbObj.ySL_dB=[92.360001,96.781006,127.728035,136.570038]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=50.959999
    dbObj.speedMaxNL_kts=16.139999
    dbObj.NL_max=97.800003
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.008240
    dbObj.cavitationSL_dB=154.570038
    dbObj.snorkelingSL_dB=148.570038
    dbObj.BuildSLTable()
    return dbObj