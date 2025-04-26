# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 885 Yasen'
    dbObj.xSpeed_kts=[0.000000,8.400000,22.400000,28.000000]
    dbObj.ySL_dB=[85.400002,90.680000,100.000000,117.000000]
    dbObj.speedMinNL_kts=10.000000
    dbObj.NL_min=49.000000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=99.000000
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.029000
    dbObj.cavitationSL_dB=161.500000
    dbObj.snorkelingSL_dB=129.000000
    dbObj.BuildSLTable()
    return dbObj