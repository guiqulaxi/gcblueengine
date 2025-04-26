# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK205'
    dbObj.xSpeed_kts=[0.000000,5.680000,19.879999,28.400000]
    dbObj.ySL_dB=[84.800003,87.976562,110.212509,116.565636]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=46.200001
    dbObj.speedMaxNL_kts=28.400000
    dbObj.NL_max=76.199997
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.011775
    dbObj.cavitationSL_dB=134.565628
    dbObj.snorkelingSL_dB=128.565628
    dbObj.BuildSLTable()
    return dbObj