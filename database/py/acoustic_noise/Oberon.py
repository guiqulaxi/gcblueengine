# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Oberon'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[90.199997,97.910004,112.900002,134.600006]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=50.500000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=100.500000
    dbObj.cavitationOffset_kts=12.270000
    dbObj.cavitationSlope_ktsperft=0.022000
    dbObj.cavitationSL_dB=164.800003
    dbObj.snorkelingSL_dB=146.600006
    dbObj.BuildSLTable()
    return dbObj