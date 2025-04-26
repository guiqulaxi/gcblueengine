# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN165'
    dbObj.xSpeed_kts=[0.000000,6.480000,22.680000,32.400002]
    dbObj.ySL_dB=[96.800003,105.055649,162.845184,179.356491]
    dbObj.speedMinNL_kts=6.860000
    dbObj.NL_min=50.200001
    dbObj.speedMaxNL_kts=32.400002
    dbObj.NL_max=104.199997
    dbObj.cavitationOffset_kts=9.800000
    dbObj.cavitationSlope_ktsperft=0.004300
    dbObj.cavitationSL_dB=197.356491
    dbObj.snorkelingSL_dB=191.356491
    dbObj.BuildSLTable()
    return dbObj