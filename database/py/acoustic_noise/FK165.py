# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK165'
    dbObj.xSpeed_kts=[0.000000,3.548000,12.418000,17.740000]
    dbObj.ySL_dB=[90.559998,95.169685,127.437469,136.656845]
    dbObj.speedMinNL_kts=7.560000
    dbObj.NL_min=49.759998
    dbObj.speedMaxNL_kts=17.740000
    dbObj.NL_max=95.480003
    dbObj.cavitationOffset_kts=10.800000
    dbObj.cavitationSlope_ktsperft=0.006960
    dbObj.cavitationSL_dB=154.656845
    dbObj.snorkelingSL_dB=148.656845
    dbObj.BuildSLTable()
    return dbObj