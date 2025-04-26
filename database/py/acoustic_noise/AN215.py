# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN215'
    dbObj.xSpeed_kts=[0.000000,8.880000,31.080000,44.400002]
    dbObj.ySL_dB=[76.199997,80.345085,109.360710,117.650887]
    dbObj.speedMinNL_kts=11.620000
    dbObj.NL_min=43.799999
    dbObj.speedMaxNL_kts=44.400002
    dbObj.NL_max=81.400002
    dbObj.cavitationOffset_kts=16.600000
    dbObj.cavitationSlope_ktsperft=0.013700
    dbObj.cavitationSL_dB=135.650879
    dbObj.snorkelingSL_dB=129.650879
    dbObj.BuildSLTable()
    return dbObj