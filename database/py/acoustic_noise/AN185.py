# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN185'
    dbObj.xSpeed_kts=[0.000000,7.440000,26.040001,37.200001]
    dbObj.ySL_dB=[86.400002,92.127525,132.220184,143.675232]
    dbObj.speedMinNL_kts=9.940000
    dbObj.NL_min=47.400002
    dbObj.speedMaxNL_kts=37.200001
    dbObj.NL_max=94.599998
    dbObj.cavitationOffset_kts=14.200000
    dbObj.cavitationSlope_ktsperft=0.010400
    dbObj.cavitationSL_dB=161.675232
    dbObj.snorkelingSL_dB=155.675232
    dbObj.BuildSLTable()
    return dbObj