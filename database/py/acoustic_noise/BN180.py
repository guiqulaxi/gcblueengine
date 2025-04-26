# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN180'
    dbObj.xSpeed_kts=[0.000000,7.340000,25.690001,36.700001]
    dbObj.ySL_dB=[88.099998,94.255966,137.347717,149.659637]
    dbObj.speedMinNL_kts=9.170000
    dbObj.NL_min=47.860001
    dbObj.speedMaxNL_kts=36.700001
    dbObj.NL_max=96.099998
    dbObj.cavitationOffset_kts=13.100000
    dbObj.cavitationSlope_ktsperft=0.010340
    dbObj.cavitationSL_dB=167.659637
    dbObj.snorkelingSL_dB=161.659637
    dbObj.BuildSLTable()
    return dbObj