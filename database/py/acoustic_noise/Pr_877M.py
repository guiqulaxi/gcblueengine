# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 877M'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[91.500000,100.290001,117.800003,126.800003]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=48.500000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=98.500000
    dbObj.cavitationOffset_kts=11.810000
    dbObj.cavitationSlope_ktsperft=0.022000
    dbObj.cavitationSL_dB=163.000000
    dbObj.snorkelingSL_dB=138.800003
    dbObj.BuildSLTable()
    return dbObj