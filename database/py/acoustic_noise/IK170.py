# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK170'
    dbObj.xSpeed_kts=[0.000000,3.760000,13.160000,18.799999]
    dbObj.ySL_dB=[89.300003,93.646179,124.069435,132.761795]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=49.150002
    dbObj.speedMaxNL_kts=18.799999
    dbObj.NL_max=94.150002
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.007850
    dbObj.cavitationSL_dB=150.761795
    dbObj.snorkelingSL_dB=144.761795
    dbObj.BuildSLTable()
    return dbObj