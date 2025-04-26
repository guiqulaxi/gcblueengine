# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK205'
    dbObj.xSpeed_kts=[0.000000,5.792000,20.271999,28.959999]
    dbObj.ySL_dB=[77.519997,81.054672,105.797394,112.866745]
    dbObj.speedMinNL_kts=11.480000
    dbObj.NL_min=44.400002
    dbObj.speedMaxNL_kts=28.959999
    dbObj.NL_max=84.599998
    dbObj.cavitationOffset_kts=16.400000
    dbObj.cavitationSlope_ktsperft=0.014680
    dbObj.cavitationSL_dB=130.866745
    dbObj.snorkelingSL_dB=124.866745
    dbObj.BuildSLTable()
    return dbObj