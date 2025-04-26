# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK210'
    dbObj.xSpeed_kts=[0.000000,5.456000,19.096001,27.280001]
    dbObj.ySL_dB=[78.580002,82.424301,109.334381,117.022980]
    dbObj.speedMinNL_kts=9.884000
    dbObj.NL_min=44.270000
    dbObj.speedMaxNL_kts=27.280001
    dbObj.NL_max=84.470001
    dbObj.cavitationOffset_kts=14.120000
    dbObj.cavitationSlope_ktsperft=0.012410
    dbObj.cavitationSL_dB=135.022980
    dbObj.snorkelingSL_dB=129.022980
    dbObj.BuildSLTable()
    return dbObj