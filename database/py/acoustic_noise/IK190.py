# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK190'
    dbObj.xSpeed_kts=[0.000000,4.608000,16.128000,23.040001]
    dbObj.ySL_dB=[83.940002,88.098564,117.208534,125.525673]
    dbObj.speedMinNL_kts=9.212000
    dbObj.NL_min=46.709999
    dbObj.speedMaxNL_kts=23.040001
    dbObj.NL_max=89.309998
    dbObj.cavitationOffset_kts=13.160000
    dbObj.cavitationSlope_ktsperft=0.010130
    dbObj.cavitationSL_dB=143.525665
    dbObj.snorkelingSL_dB=137.525665
    dbObj.BuildSLTable()
    return dbObj