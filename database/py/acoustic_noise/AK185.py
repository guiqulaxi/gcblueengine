# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK185'
    dbObj.xSpeed_kts=[0.000000,4.512000,15.792000,22.559999]
    dbObj.ySL_dB=[83.680000,87.805565,116.684502,124.935623]
    dbObj.speedMinNL_kts=9.940000
    dbObj.NL_min=47.400002
    dbObj.speedMaxNL_kts=22.559999
    dbObj.NL_max=90.599998
    dbObj.cavitationOffset_kts=14.200000
    dbObj.cavitationSlope_ktsperft=0.010400
    dbObj.cavitationSL_dB=142.935623
    dbObj.snorkelingSL_dB=136.935623
    dbObj.BuildSLTable()
    return dbObj