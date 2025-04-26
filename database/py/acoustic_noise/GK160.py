# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK160'
    dbObj.xSpeed_kts=[0.000000,3.848000,13.468000,19.240000]
    dbObj.ySL_dB=[86.879997,90.900665,119.045311,127.086639]
    dbObj.speedMinNL_kts=8.645000
    dbObj.NL_min=50.250000
    dbObj.speedMaxNL_kts=19.240000
    dbObj.NL_max=96.300003
    dbObj.cavitationOffset_kts=12.350000
    dbObj.cavitationSlope_ktsperft=0.008920
    dbObj.cavitationSL_dB=145.086639
    dbObj.snorkelingSL_dB=139.086639
    dbObj.BuildSLTable()
    return dbObj