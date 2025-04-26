# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK150'
    dbObj.xSpeed_kts=[0.000000,3.416000,11.956000,17.080000]
    dbObj.ySL_dB=[88.959999,92.982338,121.138718,129.183395]
    dbObj.speedMinNL_kts=8.015000
    dbObj.NL_min=51.549999
    dbObj.speedMaxNL_kts=17.080000
    dbObj.NL_max=98.900002
    dbObj.cavitationOffset_kts=11.450000
    dbObj.cavitationSlope_ktsperft=0.007640
    dbObj.cavitationSL_dB=147.183395
    dbObj.snorkelingSL_dB=141.183395
    dbObj.BuildSLTable()
    return dbObj