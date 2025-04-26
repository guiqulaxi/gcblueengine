# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK160'
    dbObj.xSpeed_kts=[0.000000,3.442000,12.047000,17.209999]
    dbObj.ySL_dB=[91.040001,95.471252,126.489990,135.352493]
    dbObj.speedMinNL_kts=8.330000
    dbObj.NL_min=50.340000
    dbObj.speedMaxNL_kts=17.209999
    dbObj.NL_max=96.599998
    dbObj.cavitationOffset_kts=11.900000
    dbObj.cavitationSlope_ktsperft=0.008860
    dbObj.cavitationSL_dB=153.352493
    dbObj.snorkelingSL_dB=147.352493
    dbObj.BuildSLTable()
    return dbObj