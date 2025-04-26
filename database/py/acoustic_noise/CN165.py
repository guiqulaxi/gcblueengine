# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN165'
    dbObj.xSpeed_kts=[0.000000,5.290000,18.514999,26.450001]
    dbObj.ySL_dB=[98.849998,107.518990,168.201904,185.539871]
    dbObj.speedMinNL_kts=5.985000
    dbObj.NL_min=51.500000
    dbObj.speedMaxNL_kts=26.450001
    dbObj.NL_max=104.500000
    dbObj.cavitationOffset_kts=8.550000
    dbObj.cavitationSlope_ktsperft=0.003500
    dbObj.cavitationSL_dB=203.539871
    dbObj.snorkelingSL_dB=197.539871
    dbObj.BuildSLTable()
    return dbObj