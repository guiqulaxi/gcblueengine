# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK205'
    dbObj.xSpeed_kts=[0.000000,5.244000,18.354000,26.219999]
    dbObj.ySL_dB=[79.919998,83.850769,111.366150,119.227684]
    dbObj.speedMinNL_kts=9.716000
    dbObj.NL_min=44.880001
    dbObj.speedMaxNL_kts=26.219999
    dbObj.NL_max=85.680000
    dbObj.cavitationOffset_kts=13.880000
    dbObj.cavitationSlope_ktsperft=0.011840
    dbObj.cavitationSL_dB=137.227692
    dbObj.snorkelingSL_dB=131.227692
    dbObj.BuildSLTable()
    return dbObj