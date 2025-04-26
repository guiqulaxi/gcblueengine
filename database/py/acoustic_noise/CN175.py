# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN175'
    dbObj.xSpeed_kts=[0.000000,5.750000,20.125000,28.750000]
    dbObj.ySL_dB=[95.150002,103.654091,163.182709,180.190887]
    dbObj.speedMinNL_kts=6.615000
    dbObj.NL_min=50.500000
    dbObj.speedMaxNL_kts=28.750000
    dbObj.NL_max=100.500000
    dbObj.cavitationOffset_kts=9.450000
    dbObj.cavitationSlope_ktsperft=0.004500
    dbObj.cavitationSL_dB=198.190887
    dbObj.snorkelingSL_dB=192.190887
    dbObj.BuildSLTable()
    return dbObj