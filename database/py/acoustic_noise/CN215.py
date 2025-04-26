# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN215'
    dbObj.xSpeed_kts=[0.000000,7.590000,26.565001,37.950001]
    dbObj.ySL_dB=[80.349998,85.275070,119.750542,129.600677]
    dbObj.speedMinNL_kts=9.135000
    dbObj.NL_min=46.500000
    dbObj.speedMaxNL_kts=37.950001
    dbObj.NL_max=84.500000
    dbObj.cavitationOffset_kts=13.050000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=147.600677
    dbObj.snorkelingSL_dB=141.600677
    dbObj.BuildSLTable()
    return dbObj